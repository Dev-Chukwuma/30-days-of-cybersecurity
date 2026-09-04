# Day 26 - Threat Intelligence

## Topics Covered
- Threat Intelligence levels: Strategic, Tactical, Operational
- Indicators of Compromise (IoCs): hashes, IPs, domains
- Free Threat Intelligence sources: VirusTotal, AbuseIPDB, AlienVault OTX

## What I Learned
Threat Intelligence isn't just data — it's data with context. Strategic TI helps leadership 
understand trends (e.g. "ransomware attacks on our sector are up 30%"), Tactical TI tells 
defenders how attackers operate (TTPs, tools, infrastructure), and Operational TI is about 
specific, active campaigns or threat actors.

IoCs are the fingerprints attackers leave behind — a malicious file hash, a C2 server IP, 
a phishing domain. On their own they're just data points, but cross-referenced against 
sources like VirusTotal, they tell you whether something is known-bad, and often reveal 
related infrastructure or malware families.

## Hands-On
- Looked up an IoC on VirusTotal and reviewed the detection results across multiple AV engines

## Next
Day 27 - MITRE ATT&CK Framework
