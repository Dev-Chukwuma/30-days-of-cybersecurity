# Day 25 — Incident Response

## 📅 Overview
Day 25 goes deeper into the Incident Response (IR) lifecycle first introduced on Day 6, covering each phase in detail and applying it to a real-style attack scenario built from Day 24's Windows Event ID knowledge.

---

## 🎯 Topics Covered

### The 6 Phases of Incident Response
1. **Preparation** — IR plan, trained staff, logging/monitoring already in place before anything happens
2. **Detection & Analysis** — confirming an alert is real and understanding its scope
3. **Containment** — short-term (stop the bleeding immediately) vs long-term (temporary fixes while planning full remediation)
4. **Eradication** — removing the root cause (malware, backdoor accounts, the exploited vulnerability)
5. **Recovery** — carefully restoring systems to normal operation, with close monitoring
6. **Lessons Learned** — documenting what happened and updating processes, feeding back into Preparation

### Incident Response Plan (IRP)
A written organizational document defining response team roles, communication protocols, escalation paths, and playbooks for common incident types.

### Worked Example
Applied the 6-phase cycle to a brute-force attack scenario using the exact Event ID pattern from Day 24 (4625 × many → 4624 → 4672 → 4720), showing how SIEM detection feeds directly into structured containment, eradication, and recovery actions.

---

## 🧠 Why This Matters
IR is a continuous cycle, not a one-time linear process — "Lessons Learned" feeding back into "Preparation" is what makes an organization's security posture improve over time rather than repeating the same mistakes.

---

## ➡️ Next
**Day 26 — Threat Intelligence**
