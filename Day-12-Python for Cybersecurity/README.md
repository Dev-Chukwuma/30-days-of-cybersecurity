# Day 12 — Python for Cybersecurity

## 📅 Overview
Day 12 moves from Bash into Python, focusing specifically on the modules and patterns used in security scripting — building on existing Python fundamentals rather than starting from scratch.

---

## 🎯 Topics Covered

### The `socket` Module
- `import socket` — Python's built-in toolkit for network connections
- `socket.AF_INET` — IPv4 addressing (`socket.AF_INET6` for IPv6)
- `socket.SOCK_STREAM` — TCP (connection-based, reliable)
- `socket.SOCK_DGRAM` — UDP (connectionless — no reliable open/closed check like TCP has)

### Checking If a Port Is Open
- `sock.connect_ex((target, port))` — attempts a connection, returns `0` on success (open), non-zero on failure (closed)
- `sock.settimeout(1)` — prevents the script from hanging indefinitely on filtered ports that never respond
- `sock.close()` — releases the connection once done

### Building a Multi-Port Scanner
- Used a `for` loop to check a list of ports against one target
- Used `input()` to let the user type the target IP at runtime
- Used a counter variable (`open_count += 1`) to tally how many open ports were found, printed as a summary at the end

---

## 🛠️ Tool: Mini TCP Port Scanner

```python
import socket

target = input("Enter target IP: ")
ports_to_scan = [21, 22, 80, 443, 3306]
open_count = 0

for port in ports_to_scan:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
        open_count += 1
    else:
        print(f"Port {port} is closed")
    
    sock.close()

print(f"\nScan complete. {open_count} open port(s) found.")
