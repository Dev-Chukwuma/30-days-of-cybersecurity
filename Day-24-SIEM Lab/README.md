# Day 24 — SIEM Lab

## 📅 Overview
Day 24 was a hands-on SIEM deployment exercise. What started as a Wazuh installation on Kali turned into a genuine troubleshooting journey — resource constraints, package repo failures, and licensing restrictions — before pivoting successfully to Splunk Enterprise on Windows.

---

## 🎯 Goal
Deploy a working SIEM platform and begin feeding it real log data, building hands-on experience directly on top of Day 23's SIEM Fundamentals theory.

---

## 🛠️ Attempt 1: Wazuh (Kali VM)

- Increased VM RAM (2GB → 4GB) and resized virtual disk to meet Wazuh's requirements
- Hit repeated Kali package repository sync failures (`curl`, `libxml2`, `debhelper` all failed with 404 errors at different points)
- An accidental interrupt during a long install triggered a clean rollback, requiring a restart
- Attempted Wazuh Cloud trial as a fallback — **rejected**: requires a business/company email, personal Gmail not accepted. Wazuh's support team confirmed personal users should use the on-premises install instead
- Local install ultimately did not complete successfully within the session

## 🛠️ Attempt 2: Splunk Enterprise (Windows Host) — Success

Given the repeated Kali-side friction, pivoted to installing Splunk directly on the Windows host machine instead.

- Downloaded and installed Splunk Enterprise (Free tier — 500MB/day indexing) via the official `.msi` installer
- Confirmed the service running at `http://localhost:8000`
- Configured **Local Event Log Collections** (Settings → Data Inputs) to monitor Windows Security, System, and Application logs
- Learned basic **SPL** (Search Processing Language) — Splunk's query syntax:
  - `index=*` — search all indexed data
  - `index=* EventCode=4625` — search specifically for failed Windows login attempts
  - `index=* source="WinEventLog:Security"` — filter to Security log events only
- Generated a real test event (deliberate failed login) and confirmed it appeared in a Splunk search

---

## 🧠 Why This Matters
Real infrastructure work rarely goes smoothly the first time — resource sizing, dependency conflicts, and vendor licensing terms are all genuine, common obstacles in real SOC/DevOps environments. Pivoting from a blocked approach (Wazuh) to a working alternative (Splunk) — and documenting both — reflects an authentic troubleshooting process, not just a clean tutorial walkthrough.

---

## ➡️ Next
**Day 25 — Incident Response**

*(Note: connecting the Kali VM to Splunk via the Universal Forwarder, for cross-platform log monitoring, is planned for a future session.)*
