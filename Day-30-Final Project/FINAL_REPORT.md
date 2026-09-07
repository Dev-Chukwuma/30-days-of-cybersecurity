# Day 30 - Final Project: Full Incident Report
## "Operation Loose Thread" — A Simulated Attack Chain Across the 30-Day Challenge

---

## Executive Summary

This report documents a simulated attack chain that ties together tools, techniques, and 
investigative skills built across all 30 days of this challenge. Rather than a single 
isolated exercise, this project reconstructs a realistic incident from initial 
reconnaissance through credential compromise, detection, investigation, and response — 
using real artifacts produced during the challenge as evidence at each stage.

**Scenario:** An external attacker targets a small internal network. They scan for open 
services, intercept a credential transmitted in plaintext, and use it to gain unauthorized 
access. The SOC (myself) detects the anomaly, investigates, confirms compromise, and 
responds according to the incident response lifecycle.

---

## Attack Chain & Evidence Map

### Stage 1: Reconnaissance
**MITRE ATT&CK: T1046 - Network Service Scanning**

The attacker begins by scanning the target network for open ports and running services, 
using a custom-built Python tool.

- **Evidence:** [Day 13 — Python Security Tool](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity/tree/main/Day-13-Python%20Security%20tool) 
  — `port_scanner.py`, built from scratch to enumerate open ports on a target host.
- **Finding:** Scan reveals an open FTP service — an unencrypted protocol, immediately 
  flagged as a high-value target for credential interception.

---

### Stage 2: Credential Access
**MITRE ATT&CK: T1040 - Network Sniffing**

With FTP identified as active, the attacker positions to intercept traffic on the network 
and captures a live authentication session.

- **Evidence:** [Day 20 — Network Traffic Investigation](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity/tree/main/Day-20-Network%20Traffic%20Investigation) 
  — Wireshark capture showing an FTP login transmitted entirely in plaintext.
- **Finding:** A valid username and password captured in cleartext — no encryption in 
  transit, a critical exposure.

**Automated Detection Tool (built for this capstone):**
To formalize this manual finding into a reusable capability, I built `credential_sniffer.py`, 
which scans a pcap file and automatically flags plaintext credentials across FTP, HTTP Basic 
Auth, and Telnet — without requiring a human to inspect packets by eye.

- Validated against the Day 20 capture — it successfully and automatically detected the 
  exact same exposed credential found manually, proving the tool works as a real detection 
  capability, not just a one-off script.

*(For comparison, offline credential attacks were also explored on Day 15 — [Authentication 
& Password Security](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity/tree/main/Day-15-Authentication%20and%20password%20security) 
— cracking an MD5 hash via John the Ripper, mapped separately to **T1110.002 - Password 
Cracking**. Both Day 15 and Day 20 represent different routes to the same tactic: 
**Credential Access**.)*

---

### Stage 3: Detection
**Tooling: Splunk SIEM**

Using the compromised credential, the attacker authenticates. In a real environment, this 
generates login event logs — which is exactly what was built and tested during the 
challenge's SIEM work.

- **Evidence:** [Day 24 — SIEM Lab](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity/tree/main/Day-24-SIEM%20Lab) 
  — Local Event Log Collections configured in Splunk, capturing Windows Security event logs 
  queryable via SPL (`EventCode=4625` for failed logons, `EventCode=4624` for successful ones).
- **Finding:** A cluster of failed login attempts (`4625`) immediately followed by a 
  successful login (`4624`) for the same account — a textbook brute-force-then-breach 
  signature, and exactly the pattern a SOC analyst is trained to catch.

---

### Stage 4: Investigation
**MITRE ATT&CK: T1110.001 - Password Guessing**

The alert is triaged and investigated following a structured SOC process.

- **Evidence:** [Day 28 — SOC Investigation](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity/tree/main/Day-27-MITRE%20ATT%26CK) 
  — full investigation lifecycle applied: Triage → Gather Context → Correlate → Scope → 
  Classify → Escalate.
- **Finding:** Classified as a **true positive**. The failed-login burst followed by a 
  successful logon for the same account, same source, confirms credential compromise 
  consistent with the intercepted FTP password from Stage 2.

**MITRE ATT&CK Mapping Summary (full chain):**

| Stage | Technique | ID |
|-------|-----------|-----|
| Reconnaissance | Network Service Scanning | T1046 |
| Credential Access (sniffing) | Network Sniffing | T1040 |
| Credential Access (offline cracking, related work) | Password Cracking | T1110.002 |
| Access via compromised credential | Password Guessing / Valid Accounts | T1110.001 |

---

### Stage 5: Response
**Framework: 6-Phase Incident Response Lifecycle**

With the compromise confirmed, the full IR process is applied.

- **Evidence:** [Day 25 — Incident Response](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity/tree/main/Day-25-Incident%20Response)

| Phase | Action Taken |
|-------|--------------|
| Preparation | SIEM and logging already in place prior to incident (Day 22-24 groundwork) |
| Detection & Analysis | Alert triaged and confirmed true positive (Stage 4) |
| Containment | Disable the compromised account; block the source IP at the firewall |
| Eradication | Force password reset; remove any unauthorized changes made under the account |
| Recovery | Re-enable account with new credentials; monitor closely for repeat activity |
| Lessons Learned | Recommend disabling plaintext FTP in favor of SFTP/FTPS; add a standing 
Splunk alert for the failed-then-successful login pattern; deploy `credential_sniffer.py` 
as a recurring check against network captures |

---

## Conclusion

This incident, while simulated, was built entirely from real hands-on artifacts produced 
across the 30-day challenge — a custom Python scanning tool, a live packet capture, a working 
SIEM pipeline, a structured investigation process, MITRE ATT&CK mapping, and a full incident 
response plan. Rather than treating each day's work as an isolated exercise, this project 
demonstrates the ability to connect reconnaissance, exploitation, detection, investigation, 
and response into one coherent security narrative — the core skill a SOC analyst or 
detection engineer applies to every real alert.

**Full portfolio and daily breakdown:** [30 Days of Cybersecurity](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity)
