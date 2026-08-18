# Day 09 — Processes & Services

## 📅 Overview
Day 9 covers how Linux tracks running programs (processes) and background system services — key knowledge for spotting malicious or unexpected activity on a system.

---

## 🎯 Topics Covered

### Processes
- Every running program has a unique **PID** (Process ID)
- Processes can spawn child processes, tracked via **PPID** (Parent Process ID)
- `ps aux` — snapshot of all running processes
- `top` / `htop` — live, real-time process monitoring
- `kill PID` — request a process to terminate
- `kill -9 PID` — force-terminate a process (SIGKILL)

### Services
- Background processes (daemons) managed mostly by **systemd**
- `systemctl status servicename` — check a service's state
- `systemctl start/stop/restart servicename` — control a service
- `systemctl enable/disable servicename` — control auto-start on boot
- `systemctl list-units --type=service` — list all active services

---

## 🧠 Why This Matters
Malware commonly disguises itself as a legitimate process or installs itself as a persistent service to survive reboots. Knowing what processes/services *should* be running on a healthy system is what makes spotting something abnormal possible — a core Blue Team skill.

---

## ➡️ Next
**Day 10 — Linux Logs**
