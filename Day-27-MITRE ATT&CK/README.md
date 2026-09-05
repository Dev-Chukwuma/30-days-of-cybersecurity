# Day 27 - MITRE ATT&CK Framework

## Topics Covered
- What MITRE ATT&CK is and why it exists
- Tactics vs Techniques (the why vs the how)
- The 14 ATT&CK Tactics
- Mapping own past work to real technique IDs

## What I Learned
MITRE ATT&CK is a knowledge base of real-world adversary behavior, broken into 14 Tactics 
(the attacker's goal at each stage, e.g. Initial Access, Credential Access) and Techniques 
(the specific method used to achieve that goal, e.g. Phishing, Brute Force).

Before a framework like this, incident reports were vague ("the hacker used malware"). 
ATT&CK gives every action a shared ID, so analysts across the industry can describe an 
attack precisely and unambiguously — e.g. "T1110.002 was observed" instead of "he cracked 
a password."

## Hands-On: Mapping My Own Work
- **Day 15 (John the Ripper hash cracking)** → Tactic: Credential Access 
  → Technique: T1110.002 - Brute Force: Password Cracking (offline)
- **Day 20 (FTP plaintext password sniffed in Wireshark)** → Tactic: Credential Access 
  → Technique: T1040 - Network Sniffing (capturing credentials in transit)
- Explored both technique pages on attack.mitre.org, including their Mitigations and 
  Detection sections — the part SOC analysts use for defense, not just attack reference.

## Key Insight
ATT&CK groups techniques by *attacker goal*, not by tool. Two very different methods 
(offline cracking vs live traffic sniffing) both land under Credential Access because 
they achieve the same objective.

## Next
Day 28 - SOC Investigation
