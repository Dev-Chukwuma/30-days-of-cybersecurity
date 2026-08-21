# Day 11 — Bash Scripting

## 📅 Overview
Day 11 introduces Bash scripting — automating sequences of Linux commands, building on the batch scripting concepts from Day 7.

---

## 🎯 Topics Covered

### Creating a Script
- `#!/bin/bash` — the shebang line; tells the system which interpreter should run the script
- `chmod +x script.sh` — makes the script executable
- `./script.sh` — runs the script (the `./` tells Linux to look in the current directory)

### Variables
- `name="value"` — no spaces around `=`
- `$name` — used to reference/output a variable's value

### User Input
- `read variablename` — pauses the script and stores typed input into a variable

### Conditionals
- `if [ "$var" == "value" ]; then ... else ... fi`
- Spacing inside `[ ]` is required syntax
- Every `if` must be closed with `fi`

---

## 🧠 Why This Matters
Bash scripting is the automation backbone of Linux security work — writing reusable scripts to check system state, parse logs, or respond to conditions automatically instead of running commands manually one at a time. This is the foundation Days 12-13 (Python for Cybersecurity) will build further on.

---

## ➡️ Next
**Day 12 — Python for Cybersecurity**
