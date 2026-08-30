# Day 21 — Week 3 Mini Project: Wireshark Investigation

## 📅 Overview
Day 21 wraps up Week 3 (Authentication & Password Security, Cryptography Basics, Common Attack Techniques, Log Analysis, Wireshark, Network Traffic Investigation) with a hands-on investigation project — capturing mixed traffic and identifying each type using filters, mimicking a real "here's a pcap, tell me what happened" SOC exercise.

---

## 🎯 Goal
Build a single packet capture containing multiple traffic types, then use Wireshark's display filters to isolate and document each one individually.

---

## 🛠️ Investigation Process

### Step 1 — Captured mixed traffic (no filter) on `eth0`
Generated four distinct traffic types in sequence:
- `ping -c 4 8.8.8.8` → ICMP
- `curl http://example.com` → HTTP
- `nslookup github.com` → DNS
- `ftp ftp.dlptest.com` (login + quit) → FTP

### Step 2 — Saved the full capture
Saved as `week3_capture.pcapng` for reference/documentation.

### Step 3 — Investigated using filters
| Filter | Traffic Found | Encrypted? |
|---|---|---|
| `icmp` | Ping request/reply to 8.8.8.8 | N/A (not credential-based) |
| `http` | Plaintext HTTP request to example.com | ❌ No — fully readable |
| `dns` | Query/response for github.com | N/A (not credential-based) |
| `ftp` | Login sequence, including `PASS` command | ❌ No — password visible in cleartext |

---

## 🧠 Why This Matters
This mirrors real SOC investigation work: given a packet capture, an analyst filters and isolates traffic types to understand what happened, and flags anything transmitted insecurely. The exposed FTP credential and plaintext HTTP traffic are direct, hands-on proof of why encrypted protocols (HTTPS, SFTP, SSH) are non-negotiable in real systems.

---

## ➡️ Next
**Day 22 — SOC Fundamentals**
