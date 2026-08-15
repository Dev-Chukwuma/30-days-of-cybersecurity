# Day 06 — Cybersecurity Fundamentals

## 📅 Overview
Day 6 of the **30 Days of Cybersecurity** challenge. This day builds the core vocabulary and mental models that every other topic in the roadmap (Blue Team, SOC, incident response, threat intel, MITRE ATT&CK, etc.) builds on. Rather than just listing terms, this README explains *how* and *why* each concept and attack works.

---

## 🎯 The CIA Triad

Every security decision, control, and attack maps back to one (or more) of these three pillars:

- **Confidentiality** — Only authorized people/systems can access data.
  Broken by: data leaks, eavesdropping, weak access controls, unencrypted traffic.

- **Integrity** — Data hasn't been altered without authorization.
  Broken by: man-in-the-middle tampering, unauthorized file edits, malware modifying system files, database corruption.

- **Availability** — Systems and data are accessible when needed.
  Broken by: DDoS attacks, ransomware locking files, hardware failure, power outages.

**Why it matters:** When analyzing any incident, the first question a security professional asks is "which part of the CIA triad was violated?" This shapes the entire response.

---

## ⚖️ Threat vs Vulnerability vs Risk

These three terms get confused constantly, so here's the breakdown with the formula:

**Risk = Threat × Vulnerability × Impact**

- **Threat** — Anything with the *potential* to cause harm (a hacker, malware, a disgruntled employee, even a natural disaster). The threat exists whether or not it ever acts.
- **Vulnerability** — A weakness that a threat could exploit (unpatched software, a weak password, an open port, a misconfigured firewall rule).
- **Risk** — The actual likelihood and potential impact of a threat successfully exploiting a vulnerability.

**Analogy:** A burglar (threat) walking past a house with an unlocked door (vulnerability) creates risk. If the door is locked, the threat still exists, but the risk drops sharply.

---

## 🧨 Common Attacks — Explained in Detail

### 1. Phishing
An attacker sends a fraudulent message (usually email) disguised as a trustworthy source to trick the victim into revealing sensitive information (passwords, card numbers) or clicking a malicious link/attachment. It works by exploiting human trust and urgency rather than a technical flaw — e.g. a fake "your account is locked, click here to verify" email that leads to a spoofed login page which harvests credentials.

### 2. Malware
Short for "malicious software" — any program designed to damage, disrupt, or gain unauthorized access to a system. Sub-types include:
- **Virus** — attaches itself to legitimate files/programs and spreads when that file runs.
- **Worm** — self-replicates and spreads across networks without needing a host file or user action.
- **Trojan** — disguises itself as legitimate software to trick users into installing it, then delivers a malicious payload.
- **Ransomware** — encrypts a victim's files and demands payment for the decryption key, directly attacking **availability**.

### 3. Brute Force
An attacker systematically tries every possible password (or a large list of likely ones — a "dictionary attack") against a login system until one works. It exploits weak or short passwords and the absence of protections like account lockouts, rate limiting, or MFA.

### 4. DDoS (Distributed Denial of Service)
An attacker floods a target system/server with overwhelming traffic from many compromised devices (a "botnet") simultaneously, exhausting its resources (bandwidth, CPU, memory) so legitimate users can't access it. This is a direct attack on **availability** — no data is stolen, the service is just knocked offline.

### 5. Man-in-the-Middle (MITM)
An attacker secretly intercepts and potentially alters communication between two parties who believe they're communicating directly with each other. Common on unsecured public Wi-Fi, where an attacker positions themselves between a victim and the router to read or modify traffic — attacking both **confidentiality** and **integrity**.

### 6. SQL Injection
An attacker inserts malicious SQL code into an input field (like a login form or search box) that gets executed by the backend database because the application fails to properly sanitize user input. This can let an attacker bypass authentication, read, modify, or delete database records — a classic example of a vulnerability at the application layer rather than the network layer.

---

## 🌐 Attack Surface
The **attack surface** is the total sum of all points where an unauthorized user could try to enter or extract data from a system — every open port, every input field, every user account, every exposed service. The larger the attack surface, the more opportunities an attacker has. Reducing attack surface (closing unused ports, removing unnecessary software, disabling unused accounts) is a core defensive strategy.

---

## 🛡️ Security Controls

Controls are grouped by **when** they act:

- **Preventive** — Stops an attack before it happens.
  Examples: firewalls (block unauthorized traffic before it reaches a system), MFA (blocks login even if a password is stolen).

- **Detective** — Identifies that an attack is happening or already happened.
  Examples: Intrusion Detection Systems (IDS) that alert on suspicious traffic patterns, logging/monitoring that reveals unusual login times or locations.

- **Corrective** — Repairs damage after an attack.
  Examples: restoring from backups after ransomware, patching the vulnerability that was exploited so it can't be used again.

And by **type**:
- **Technical** — firewalls, encryption, antivirus, IDS
- **Administrative** — policies, security awareness training, procedures
- **Physical** — locks, badges, security guards, server room access control

---

## 🧱 Defense in Depth
A strategy of layering multiple, independent security controls so that if one layer fails, another still protects the system. Example: even if an attacker gets past the firewall, antivirus might catch the malware; even if that fails, monitoring/logging might catch the unusual activity; even if that fails, backups allow recovery. No single control is ever assumed to be perfect.

---

## 🔵🔴 Blue Team vs Red Team

- **Blue Team** — The defenders. Their job is to detect, respond to, and prevent attacks — monitoring logs, hardening systems, responding to incidents. (This is the long-term direction of this 30-day challenge.)
- **Red Team** — The attackers (ethical hackers). Their job is to simulate real-world attacks against an organization to find weaknesses before real attackers do.

Both teams exist to strengthen the same organization's security from opposite angles.

---

## 🚨 Incident Response Lifecycle

When a security incident happens, responders follow a structured process:

1. **Detect** — Identify that something suspicious/malicious is happening (via alerts, logs, user reports).
2. **Investigate** — Determine what happened, how, and the scope of impact.
3. **Contain** — Stop the incident from spreading further (isolate affected systems).
4. **Eradicate** — Remove the root cause (malware, unauthorized access, vulnerability).
5. **Recover** — Restore affected systems to normal operation.
6. **Learn** — Conduct a post-incident review to prevent recurrence.

---

## 🧪 Practical Exercise
Applied the framework below to real-world security scenarios to connect theory to practice:

**Asset → Threat → Vulnerability → Risk → Security Control**

For each scenario, identified the asset at stake, the relevant threat, the vulnerability being exploited, the resulting risk, and which control(s) would mitigate it.

---

## 🧠 Key Takeaway
Every tool, attack, and defense in cybersecurity ultimately maps back to protecting **Confidentiality, Integrity, and Availability**. Understanding *why* each attack works — not just its name — is what separates memorizing terms from actually thinking like a security professional.

---

## ➡️ Next
**Day 07 — Week 1 Mini Project:** Windows Security Recon Report/Tool
