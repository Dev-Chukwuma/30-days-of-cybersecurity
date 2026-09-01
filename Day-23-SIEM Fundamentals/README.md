# Day 23 — SIEM Fundamentals

## 📅 Overview
Day 23 introduces SIEM (Security Information and Event Management) — the centralized platform that automates and scales the manual log analysis skills built in Day 18, across an entire organization.

---

## 🎯 Topics Covered

### Core SIEM Functions
- **Log Aggregation** — pulls logs from many sources (Windows, Linux, firewalls, cloud) into one place
- **Normalization** — converts different log formats into a consistent structure
- **Correlation** — connects events across different sources to reveal patterns invisible in any single log (the automated version of Day 18's "building a story from logs")
- **Alerting** — automatically flags matched suspicious patterns for analyst triage
- **Dashboards & Reporting** — visual summaries for monitoring and compliance

### Real-World SIEM Platforms
- Splunk (industry leader, commercial)
- Elastic Security / ELK Stack (free, open-source)
- Wazuh (free, open-source, security-focused)
- Microsoft Sentinel (cloud-native, Azure/M365 integration)

### Conceptual Detection Rule
IF (failed_logins > 5 within 1 minute)
AND (same source IP)
AND (same target account)
THEN generate_alert("Possible brute force attempt")

---

## 🧠 Why This Matters
A SIEM automates exactly what was done manually in Day 18 (spotting suspicious sequences in logs) — but across an entire organization's infrastructure simultaneously, correlating events a human could never catch by reading logs one at a time. This is the tool a Tier 1/2 SOC analyst lives in daily.

---

## ➡️ Next
**Day 24 — SIEM Lab**
