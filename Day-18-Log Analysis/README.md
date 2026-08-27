# Day 18 — Log Analysis

## 📅 Overview
Day 18 builds on Day 10's log basics, shifting from reading/filtering logs to actually analyzing them — spotting patterns, anomalies, and building a timeline of events like an investigator would.

---

## 🎯 Topics Covered

### What to Look For
- **Frequency anomalies** — spikes in failed logins/repeated requests signal automation (brute force, scanning)
- **Timing patterns** — activity outside normal hours is worth investigating
- **Sequence of events** — a single log line means little; the sequence tells the story
- **Source correlation** — the same IP appearing across multiple log types builds a fuller picture

### Worked Example
A sequence of 50 rapid failed SSH logins from one IP, followed by a success, followed by reading `/etc/shadow`, all at 3 AM — read together, this is a clear brute-force-then-credential-harvest pattern, not just isolated log lines.

### False Positives
Not every anomaly is malicious — legitimate travel logins, scheduled cron jobs, or misconfigured services can all look unusual without being attacks. Real analysis requires context, not just pattern matching.

### Alert Fatigue
Over-alerting on every anomaly causes analysts to start ignoring warnings — a real, recognized problem in SOC environments.

---

## 🧠 Why This Matters
This connects directly to Days 15-17: understanding hashing, common attacks, and attack techniques is what allows an analyst to recognize a real pattern in raw log data, not just read isolated lines.

---

## ➡️ Next
**Day 19 — Wireshark**
