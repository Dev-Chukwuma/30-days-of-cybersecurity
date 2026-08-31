# Day 22 — SOC Fundamentals

## 📅 Overview
Day 22 introduces the Security Operations Center (SOC) — the organizational structure and workflow that ties together nearly every skill covered so far in this roadmap (logs, permissions, network traffic, cryptography, attack techniques).

---

## 🎯 Topics Covered

### What a SOC Is
A team/facility responsible for continuously monitoring, detecting, and responding to security threats across an organization, 24/7.

### SOC Tiers
- **Tier 1 (Triage)** — monitors alerts, initial investigation, decides on escalation (typical entry point)
- **Tier 2 (Investigation)** — handles escalated alerts, deeper investigation
- **Tier 3 (Threat Hunter/Senior)** — proactively hunts for missed threats, handles complex incidents
- **SOC Manager** — oversees team, process, reporting

### The SOC Alert Workflow
1. Detection (SIEM, IDS, EDR flags something)
2. Triage (real or false positive?)
3. Investigation (what happened, how, scope)
4. Escalation (if serious, hand off)
5. Response (contain, eradicate, recover)
6. Documentation (write-up for reference/reporting)

### Key SOC Tools
- **SIEM** — centralizes logs across the organization
- **IDS/IPS** — flags/blocks suspicious network activity
- **EDR** — monitors individual devices
- **Threat Intelligence feeds** — external data on known threats

---

## 🧠 Why This Matters
This day connects nearly everything learned so far (Days 8-21) into a real organizational context — logs, permissions, network traffic investigation, and cryptography are the actual daily tools of a Tier 1/2 SOC analyst, the role this roadmap is building toward.

---

## ➡️ Next
**Day 23 — SIEM Fundamentals**
