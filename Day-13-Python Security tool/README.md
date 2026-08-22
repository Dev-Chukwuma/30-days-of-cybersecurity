# Day 13 — Python Security Tool

## 📅 Overview
Day 13 builds on Day 12's socket basics to create a complete, modular port scanning tool — organized into functions, capable of scanning a full port range, and saving results to a file as proof of work.

---

## 🎯 Topics Covered

### Scanning a Range
- `range(start_port, end_port + 1)` — scans every port in a given range instead of a hardcoded list

### Modular Functions
- `scan_port(target, port, timeout)` — checks a single port, returns True/False only (no printing — separates logic from output)
- `scan_target(target, start_port, end_port)` — loops through a port range, calls scan_port on each, collects open ports into a list
- `save_results(target, open_ports)` — writes scan results to a text file
- `main()` — handles user input and orchestrates the other functions

### File Writing
- `with open(filename, "w") as f:` — safely opens a file for writing; automatically closes it even if an error occurs

### Input Conversion
- `int(input(...))` — converts user input (always text by default) into a usable integer for range()

### Python Convention
- `if __name__ == "__main__":` — ensures `main()` only runs when the file is executed directly, not when imported elsewhere

---

## 🛠️ Tool: `port_scanner.py`
A modular TCP port scanner that takes a target IP and port range as input, prints open ports as it finds them, and saves results to a `.txt` file.

---

## 🧠 Why This Matters
This mirrors how real security tools are structured — modular, reusable functions rather than one long script, with results saved as evidence rather than just printed and lost. This is the foundation for Day 14's Week 2 Mini Project.

---

## ➡️ Next
**Day 14 — Week 2 Mini Project**
