# Day 17 — Common Attack Techniques

## 📅 Overview
Day 17 goes deeper into attack types first introduced on Day 6, focusing on the actual technical mechanisms behind each one.

---

## 🎯 Topics Covered

### Phishing Variants
- Spear phishing (targeted), whaling (targets executives), vishing (voice), smishing (SMS)
- Technical mechanism: lookalike domains, URL shorteners, spoofed sender addresses (why SPF/DKIM/DMARC exist)

### Malware Types
- Trojan, worm, ransomware (weaponized encryption), rootkit (hides at OS level for persistence)

### Credential Attacks
- Brute force, dictionary attack, credential stuffing (reusing leaked credentials across sites)

### Man-in-the-Middle (MITM)
- ARP spoofing: attacker sends fake ARP messages to reroute local network traffic through their machine

### SQL Injection
- Example: `' OR '1'='1` injected into unsanitized input can make a login query always evaluate true, bypassing authentication

### DDoS Types
- Volumetric (bandwidth flooding), protocol attacks (e.g. SYN flood), application-layer attacks (targeting expensive app operations)

### Social Engineering
- Pretexting, baiting, tailgating — targets human trust rather than technical systems

### Zero-Day Attacks
- Exploits an unknown/unpatched vulnerability — no signature-based detection exists yet, which is why behavior-based detection matters in SOC/SIEM work

---

## 🧠 Why This Matters
Understanding the technical mechanics behind each attack type — not just the name — is what lets a Blue Team analyst actually recognize and investigate these patterns in logs and network traffic, rather than just knowing buzzwords.

---

## ➡️ Next
**Day 18 — Log Analysis**
