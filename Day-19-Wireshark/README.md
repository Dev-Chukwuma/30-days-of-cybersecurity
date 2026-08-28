# Day 19 — Wireshark

## 📅 Overview
Day 19 introduces Wireshark — a packet analyzer that captures and inspects live network traffic in full detail, going beyond what tools like `netstat` show.

---

## 🎯 Topics Covered

### Core Concepts
- Wireshark captures every packet on a chosen network interface, showing source/destination, protocol, and full packet content — unlike `netstat`, which only summarizes that a connection exists
- **Interfaces**: `lo` (loopback, traffic that stays on the machine), `eth0` (actual network traffic), among others
- **Display filters** narrow a live capture down to what matters (e.g. `icmp`, `tcp.port == 443`)

### Hands-On Capture
- Captured on `eth0` with an `icmp` display filter applied
- Generated traffic with `ping -c 4 8.8.8.8`
- Confirmed a key distinction: pinging `127.0.0.1` doesn't appear when capturing on `eth0`, since loopback traffic never leaves the machine via the actual network interface — it only appears when capturing on `lo`

### Packet Layer Breakdown
Expanding a captured packet reveals it stacked layer by layer: Frame → Ethernet → IP → protocol (e.g. ICMP) — a direct, visual version of the network layering concepts from Days 1-3.

---

## 🧠 Why This Matters
Wireshark is a core Blue Team/SOC tool for investigating network traffic during an incident — understanding interfaces and filters is the foundation for the deeper traffic investigation work coming in Day 20.

---

## ➡️ Next
**Day 20 — Network Traffic Investigation**
