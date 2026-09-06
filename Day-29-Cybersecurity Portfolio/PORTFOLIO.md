# 🎯 Cybersecurity Portfolio Highlights

Curated highlights from my [30 Days of Cybersecurity](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity) 
challenge — a self-directed program covering networking, systems, offensive security, and 
Blue Team / SOC fundamentals. Below are the projects I'm proudest of, each demonstrating a 
different core skill.

---

## 🖥️ Operating Systems & Networking Foundations
**[Days 1-10 — Networking, Linux & Windows Fundamentals](./Day-01-Networking%20Basics)**

**What I did:** Built up core systems and networking knowledge hands-on — how the internet 
actually works, ports/protocols, Linux fundamentals (filesystem navigation, users/groups, 
permissions via chmod/chown, SUID/SGID), Windows fundamentals, process and service management 
(ps/top/kill/systemctl), and Linux logging (journalctl, since Kali has no rsyslog by default).

**What I built:** A Week 1 mini project (`security_recon.bat`) applying early networking/OS 
concepts into a working recon script, plus a documented command reference for Linux 
administration tasks.

**What it demonstrates:** The systems-level fluency that everything else in this portfolio 
depends on — you can't investigate an attack, read a log, or secure a host without first 
understanding how the OS and network actually behave under the hood.

---

## 🔧 Python Port Scanner
**[Day 13 — Python Security Tool](./Day-13-Python%20Security%20Tool)**

**What I did:** Built a modular, socket-based TCP port scanner in Python from scratch — 
extending a basic Day 12 script into a proper tool with functions, configurable port range 
scanning, file output, and input validation via try/except.

**What I built:** `port_scanner.py` — takes a target and port range, scans for open ports, 
and writes results to a file.

**What it demonstrates:** Python fundamentals applied to real security tooling — not just 
scripting, but structuring code for reuse and handling bad input gracefully.

---

## 🔐 Password Cracking (Offensive Security)
**[Day 15 — Authentication & Password Security](./Day-15-Authentication%20and%20password%20security)**

**What I did:** Cracked an MD5 hash using John the Ripper, working through the wordlist 
attack chain (default wordlist → incremental mode → rockyou.txt) after early attempts failed. 
Also generated and cracked an NTLM hash for comparison.

**What I found:** Successfully recovered the plaintext password, and documented how hash 
type affects cracking difficulty (NTLM vs MD5).

**What it demonstrates:** Practical offensive security skills — understanding how attackers 
actually break weak credentials, not just the theory of "use strong passwords."

---

## 🦈 Network Traffic Investigation (Wireshark)
**[Day 20-21 — Network Traffic & Wireshark Investigation](./Day-20-Network%20Traffic%20Investigation)**

**What I did:** Captured live network traffic and identified a plaintext password transmitted 
over FTP — a real, visible example of why unencrypted protocols are a security risk. Followed 
up with a mixed-protocol capture (ICMP/HTTP/DNS/FTP), filtering and documenting each traffic type.

**What I found:** A credential exposed in cleartext, plus a full breakdown of packet structure 
across multiple protocols.

**What it demonstrates:** Packet-level investigative skill — the ability to read raw traffic 
and pull out a security-relevant finding, a core Tier 1/2 SOC analyst skill.

---

## 🧪 SIEM Lab (Splunk)
**[Day 24 — SIEM Lab](./Day-24-SIEM%20Lab)**

**What I did:** Attempted a Wazuh install on Kali (hit repeated repo/dependency issues — 
documented as troubleshooting rather than abandoning), then pivoted to Splunk Enterprise. 
Set up Local Event Log Collections for Security/System/Application logs and learned SPL 
search syntax, including `EventCode=4625` for failed logins.

**What I built:** A working local SIEM pipeline capturing Windows event logs, queryable via SPL.

**What it demonstrates:** Real SOC tooling experience, plus the ability to troubleshoot and 
pivot when a tool doesn't cooperate — a very real day-in-the-life SOC skill.

---

## 🧯 Incident Response Lifecycle
**[Day 25 — Incident Response](./Day-25-Incident%20Response)**

**What I did:** Studied the 6-phase IR lifecycle in depth — Preparation, Detection & Analysis, 
Containment, Eradication, Recovery, Lessons Learned — then applied all six phases to a real 
pattern from my own lab: a brute-force login attempt followed by suspicious account creation 
(Event ID sequence from Day 24's Splunk work).

**What I built:** A phase-by-phase written response plan mapping each IR stage to concrete 
actions for that specific incident pattern (e.g. containment = disable the account, 
eradication = remove the newly created account, lessons learned = alert on that Event ID 
combination going forward).

**What it demonstrates:** The ability to go beyond "detecting" a problem to actually 
responding to it in a structured, repeatable way — the difference between an analyst who 
flags alerts and one who can own an incident end-to-end.

---

## 🎯 MITRE ATT&CK Mapping + SOC Investigation
**[Day 27-28 — MITRE ATT&CK & SOC Investigation](./Day-27-MITRE%20ATT%26CK)**

**What I did:** Mapped my own earlier work to official MITRE ATT&CK technique IDs — Day 15's 
offline hash cracking → **T1110.002 (Password Cracking)**, Day 20's sniffed FTP credential → 
**T1040 (Network Sniffing)**. Then ran a full SOC investigation: simulated a failed-login 
burst (`EventCode=4625`) followed by a successful logon (`EventCode=4624`) for the same 
account in Splunk, correlated the pattern, classified it as a true positive, and mapped it 
to **T1110.001 (Password Guessing)**.

**What it demonstrates:** The ability to connect hands-on technical findings to industry-standard 
threat frameworks — turning "I found something" into "here's what this means and how I'd 
report it." This is the skill that separates a hobbyist from someone ready for a SOC analyst role.

---

## 🧠 What This Challenge Proves

Across these seven highlights: I understand systems and networking at a fundamental level, 
can write functional security tooling, break weak credentials, investigate raw network 
traffic, stand up and query a SIEM, run a structured incident response, and translate 
findings into industry-standard threat intelligence language. Full daily breakdown of all 
30 days available in the [main repo](https://github.com/Dev-Chukwuma/30-days-of-cybersecurity).
