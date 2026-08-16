# Day 07 — Week 1 Mini Project: Windows Security Recon Report/Tool

## 📅 Overview
Day 7 marks the end of Week 1 in the **30 Days of Cybersecurity** challenge. This mini project combines the Windows fundamentals from Day 5 and the security concepts from Day 6 into a working, hands-on tool: a batch script that collects security-relevant information from a Windows machine and outputs it into a single readable report.

---

## 🎯 Goal
Build a lightweight recon tool that pulls key security information off a Windows machine — the same kind of quick snapshot a SOC analyst or sysadmin might run to get a fast read on a system's state.

---

## 🧰 New Skill: Batch File Scripting (.bat)

Before building the tool, I learned the basics of Windows batch scripting — writing a plain text file with a `.bat` extension that runs a sequence of commands automatically instead of typing them one by one.

### Concepts learned
- **What a `.bat` file is** — a script Windows executes line by line, same as typing commands manually in Command Prompt
- **`REM`** — comment lines, ignored by Windows, used to document what the script does
- **`>`** — writes a command's output to a file, creating it (or overwriting it if it exists)
- **`>>`** — appends a command's output to an existing file without erasing what's already there
- **`echo`** — prints text; combined with `>>`, used to write labeled section headers into the report
- **`echo.`** — prints a blank line, used for spacing/readability in the output file
- **Saving correctly** — in Notepad, "Save as type" must be set to "All Files," otherwise the file saves as `filename.bat.txt` instead of a real batch file

### The core pattern
echo ===== SECTION NAME ===== >> report.txt
command >> report.txt

First write to the file uses `>` to create it; every write after that uses `>>` to append, so each section stacks on top of the last instead of overwriting it.

---

## 🛠️ Tool: `security_recon.bat`

Applied the batch scripting basics above to build a script that pulls key security information off a Windows machine.

### Report sections included
| Section | Command | What it reveals |
|---|---|---|
| System Info | `systeminfo` | OS version, patch level, uptime |
| Hostname | `hostname` | Machine identity |
| Current User | `whoami` | Who ran the scan |
| Admin Check | `net localgroup administrators` | Who has admin rights — a key risk indicator |
| Network Config | `ipconfig` | IP address and network adapters |
| Listening Ports | `netstat -ano`  | findstr LISTENING` | Open attack surface on the machine |
| Running Processes | `tasklist` | What's actively running |



---

## 🧠 Why This Matters
This mirrors real-world security recon work — quickly gathering system, user, network, and process information to build a baseline understanding of a machine's security posture. Reading the report like an analyst (not just running commands) means asking: *Is this user an admin? Are there unexpected open ports? Are there unfamiliar processes running?*

It also introduced a genuinely new skill — batch scripting — which is the foundation for automating security tasks, something that comes back repeatedly later in the roadmap (Bash and Python scripting on Days 11-13).

---

## ➡️ Next
**Day 08 — Linux Users & Permissions**