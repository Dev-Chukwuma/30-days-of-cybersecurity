#!/usr/bin/env python3
"""
credential_sniffer.py
Day 30 Final Project - Automated Plaintext Credential Detector

Scans a pcap file for plaintext credentials exposed over insecure protocols:
FTP (USER/PASS), HTTP Basic Auth, and Telnet.

Usage: python3 credential_sniffer.py <path_to_pcap>
"""

import sys
import base64
from scapy.all import rdpcap, TCP, Raw


def extract_ftp_credentials(packets):
    """Scan for FTP USER/PASS commands in plaintext."""
    findings = []
    for pkt in packets:
        if pkt.haslayer(TCP) and pkt.haslayer(Raw):
            payload = pkt[Raw].load.decode(errors="ignore").strip()
            src = pkt[0][1].src if pkt.haslayer("IP") else "unknown"
            dst = pkt[0][1].dst if pkt.haslayer("IP") else "unknown"

            if payload.upper().startswith("USER "):
                username = payload[5:].strip()
                findings.append({
                    "protocol": "FTP",
                    "type": "Username",
                    "value": username,
                    "src": src,
                    "dst": dst
                })
            elif payload.upper().startswith("PASS "):
                password = payload[5:].strip()
                findings.append({
                    "protocol": "FTP",
                    "type": "Password",
                    "value": password,
                    "src": src,
                    "dst": dst
                })
    return findings


def extract_http_basic_auth(packets):
    """Scan for HTTP Basic Authentication headers and decode them."""
    findings = []
    for pkt in packets:
        if pkt.haslayer(Raw):
            try:
                payload = pkt[Raw].load.decode(errors="ignore")
            except Exception:
                continue

            if "Authorization: Basic" in payload:
                for line in payload.split("\r\n"):
                    if line.startswith("Authorization: Basic"):
                        b64_creds = line.split(" ")[-1].strip()
                        try:
                            decoded = base64.b64decode(b64_creds).decode(errors="ignore")
                        except Exception:
                            decoded = "(decode failed)"
                        src = pkt[0][1].src if pkt.haslayer("IP") else "unknown"
                        dst = pkt[0][1].dst if pkt.haslayer("IP") else "unknown"
                        findings.append({
                            "protocol": "HTTP",
                            "type": "Basic Auth",
                            "value": decoded,
                            "src": src,
                            "dst": dst
                        })
    return findings


def extract_telnet_data(packets):
    """
    Telnet sends data char-by-char across many packets, so this does a
    best-effort flag: any Telnet-port (23) traffic carrying printable
    payload is flagged for manual review rather than auto-parsed.
    """
    findings = []
    for pkt in packets:
        if pkt.haslayer(TCP) and pkt.haslayer(Raw):
            if pkt[TCP].dport == 23 or pkt[TCP].sport == 23:
                payload = pkt[Raw].load.decode(errors="ignore")
                if payload.strip():
                    src = pkt[0][1].src if pkt.haslayer("IP") else "unknown"
                    dst = pkt[0][1].dst if pkt.haslayer("IP") else "unknown"
                    findings.append({
                        "protocol": "Telnet",
                        "type": "Raw Data (manual review)",
                        "value": payload.strip(),
                        "src": src,
                        "dst": dst
                    })
    return findings


def print_report(all_findings):
    if not all_findings:
        print("[-] No plaintext credentials detected in this capture.")
        return

    print(f"[!] {len(all_findings)} plaintext credential exposure(s) detected:\n")
    for i, f in enumerate(all_findings, 1):
        print(f"--- Finding {i} ---")
        print(f"Protocol : {f['protocol']}")
        print(f"Type     : {f['type']}")
        print(f"Value    : {f['value']}")
        print(f"Source   : {f['src']}")
        print(f"Dest     : {f['dst']}")
        print()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 credential_sniffer.py <path_to_pcap>")
        sys.exit(1)

    pcap_path = sys.argv[1]
    print(f"[*] Loading pcap: {pcap_path}")

    try:
        packets = rdpcap(pcap_path)
    except Exception as e:
        print(f"[!] Failed to read pcap: {e}")
        sys.exit(1)

    print(f"[*] {len(packets)} packets loaded. Scanning...\n")

    findings = []
    findings += extract_ftp_credentials(packets)
    findings += extract_http_basic_auth(packets)
    findings += extract_telnet_data(packets)

    print_report(findings)


if __name__ == "__main__":
    main()
