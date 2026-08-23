# Day 14 — Week 2 Mini Project: Linux Security Audit Tool

## 📅 Overview
Day 14 wraps up Week 2 (Linux Users & Permissions, Processes & Services, Linux Logs, Bash Scripting, Python for Cybersecurity) with a combined project: a Python-based Linux Security Audit script.

---

## 🎯 Goal
Build a Python tool that runs a security "health check" on a Linux machine — combining Week 2's skills into one script that generates a single audit report, similar in spirit to the Day 7 Windows recon project.

---

## 🧰 New Skill: The `subprocess` Module

- `subprocess.run([...])` — runs a terminal command from within Python
- `capture_output=True` — captures the command's output instead of printing it live
- `text=True` — returns output as readable text instead of raw bytes
- `result.stdout` — holds the captured output

Unlike `socket` (used to talk over a network connection in Days 12-13), `subprocess` is used to run and capture the result of terminal commands — the same commands typed manually, but callable from Python.

---

## 🛠️ Tool: `security_audit.py`

### Report sections
| Section | Command Used | From |
|---|---|---|
| Current User | `whoami` | Day 8 |
| Running Processes | `ps aux` | Day 9 |
| Active Services | `systemctl list-units --type=service` | Day 9 |
| Recent Errors | `journalctl -p err -b` | Day 10 |

### Structure
- One function per check (`get_current_user()`, `get_running_processes()`, etc.) — each runs a command and returns its output as text
- `generate_report()` — combines all sections into one labeled report string
- `save_report()` — writes the report to `security_audit_report.txt`
- `main()` — orchestrates the whole process

---

## 🧠 Why This Matters
This mirrors real Blue Team tooling — automating the collection of system state (user, processes, services, errors) into a single reviewable report instead of running each check manually. Combining `subprocess` with the modular function structure from Day 13 shows how individual skills compound into a genuinely useful tool.

---

## ➡️ Next
**Day 15 — Authentication & Password Security**
