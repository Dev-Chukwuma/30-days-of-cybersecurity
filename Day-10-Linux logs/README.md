# Day 10 — Linux Logs

## 📅 Overview
Day 10 covers where Linux stores system activity records and how to read/filter them — the foundation of detection and investigation work in a Blue Team/SOC role.

---

## 🎯 Topics Covered

### Key Log Locations
- `/var/log/auth.log` (or `/var/log/secure`) — authentication events: logins, sudo, SSH attempts
- `/var/log/syslog` (or `/var/log/messages`) — general system activity

### Viewing & Filtering Logs
- `cat file` — view entire log file
- `tail file` — view last 10 lines
- `tail -f file` — follow a log in real-time as new entries arrive
- `grep "pattern" file` — search a file for lines matching specific text (e.g. failed logins)
- `grep -i` — case-insensitive search
- `grep -c` — count matching lines instead of showing them

### journalctl (systemd)
- Centralized, structured log viewer on modern Linux — filters on real fields (service, time, priority) instead of text patterns
- `journalctl -u servicename` — logs for a specific service
- `journalctl --since "1 hour ago"` — filter by time
- `journalctl -p err -b` — filter by priority level (errors) since last boot

---

## 🧠 Why This Matters
Logs are the evidence trail for any security investigation. Repeated "Failed password" entries indicate a brute force attempt; unusual sudo activity or new user creation can indicate compromise. Reading and filtering logs effectively — whether with grep on text logs or journalctl on structured ones — is a core, daily Blue Team/SOC skill.

---

## ➡️ Next
**Day 11 — Bash Scripting**
