 # 🛡️ Day 3 — Ports & Protocols

## 📚 What I Learned

Today I learned how devices communicate over networks using ports and protocols.

### 🔌 What is a Port?

A port is a logical number used to identify a specific service or application on a device.

Think of it as:

> IP address = Device
> Port = Service

Ports range from 0–65535.

### ⭐ Common Ports

| Port | Service | Purpose |
|---:|---|---|
| 22 | SSH | Secure remote access |
| 23 | Telnet | Remote access |
| 53 | DNS | Domain name resolution |
| 80 | HTTP | Web traffic |
| 443 | HTTPS | Secure web traffic |
| 3389 | RDP | Windows Remote Desktop |

---

## 🌐 Protocols

A protocol is a set of rules that determines how devices communicate.

### TCP

- Connection-oriented
- Reliable
- Delivers data in order

### UDP

- Connectionless
- Lightweight
- Faster for many use cases
- Does not provide TCP's reliability mechanisms

---

## 🤝 TCP 3-Way Handshake

TCP establishes a connection using:

**SYN → SYN-ACK → ACK**

This establishes the connection before data is exchanged.

---

# 🔎 Practical Exercises

## 1. `netstat -ano`

I used:

\`\`\`cmd
netstat -ano
\`\`\`

to view active network connections, listening ports, connection states, and Process IDs (PIDs).

### Important States

**LISTENING**
A service is waiting for incoming connections.

**ESTABLISHED**
An active TCP connection exists.

**TIME_WAIT**
A recently closed TCP connection is being kept temporarily before the connection state is fully removed.

---

## 2. PID Investigation

I investigated a listening port using its Process ID.

The `netstat` output showed:

- Port 902 → PID 5476
- Port 912 → PID 5476

I then used:

\`\`\`cmd
tasklist /FI "PID eq 5476"
\`\`\`

The result showed:

\`\`\`
vmware-authd.exe
\`\`\`

This allowed me to trace:

**Port → PID → Process**

The ports were associated with a VMware service running on my computer.

---

## 3. Testing Port 443

I used PowerShell:

\`\`\`powershell
Test-NetConnection google.com -Port 443
\`\`\`

Port 443 is commonly used for HTTPS traffic. This test helped me check whether my computer could establish a TCP connection to Google's port 443.

---

## 4. Testing Port 80

I also tested:

\`\`\`powershell
Test-NetConnection google.com -Port 80
\`\`\`

Port 80 is commonly used for HTTP traffic. This allowed me to compare connectivity to two commonly used web ports.

---

## 🧠 Key Takeaway

Network ports help direct traffic to specific services on a device.

During today's practical work, I learned how to investigate network activity using:

**Port → PID → Process**

I also learned that seeing a listening port does not automatically mean the system is compromised. The service behind the port needs to be investigated and understood.

---

## 🧰 Tools Used

- Windows Command Prompt
- PowerShell
- `netstat -ano`
- `tasklist`
- `Test-NetConnection`