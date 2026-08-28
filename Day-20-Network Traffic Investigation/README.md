# 🔎 Day 20 — Network Traffic Investigation

## 🎯 Objective

Today I focused on **network traffic investigation using Wireshark**.

The goal was to move beyond simply capturing packets and start understanding what the traffic means — who is communicating, what protocols are being used, and whether anything looks unusual.

---

## 🧠 What I Learned

### 1. Following TCP Streams

TCP communication is made up of multiple packets.

Wireshark's **Follow TCP Stream** feature allows me to reconstruct communication between two hosts and view the conversation as a continuous stream.

This is useful for investigating:

- Client/server communication
- Suspicious connections
- Data being transferred
- Application-level communication

---

### 2. DNS Investigation

DNS translates domain names into IP addresses.

I investigated:

- DNS queries
- DNS responses
- Requested domains
- Source and destination IP addresses
- The relationship between devices and domains

Useful filter:

`dns`

Specific domain:

`dns.qry.name == "example.com"`

---

### 3. HTTP Traffic

HTTP traffic can reveal useful information because it is generally unencrypted.

Useful filter:

`http`

Things to investigate include:

- HTTP requests
- HTTP responses
- Requested URLs
- Hosts
- GET and POST requests

---

### 4. HTTPS Traffic

HTTPS encrypts application data, making the contents of communication harder to inspect directly.

However, useful metadata can still be observed, including:

- Source and destination IPs
- Ports
- Connection timing
- TLS information
- Servers being contacted

Useful filter:

`tls`

---

### 5. Network Conversations

Wireshark can help identify which hosts are communicating with each other.

Important information includes:

- Source IP
- Destination IP
- Source port
- Destination port
- Protocol
- Packet count
- Amount of data transferred

This helps establish what normal network communication looks like and makes unusual activity easier to identify.

---

## 🚨 Looking for Suspicious Traffic

During an investigation, I learned to look for traffic that doesn't fit the expected pattern.

Examples include:

- Unexpected external connections
- Repeated connections to the same destination
- Unusual ports
- Large amounts of unexpected data
- Strange DNS requests
- Communication with unfamiliar hosts
- Repeated failed connection attempts

The goal isn't to immediately label something as malicious.

The goal is to **identify anomalies and investigate them further**.

---

## 🛠️ Useful Wireshark Filters

`ip` — Display IP traffic.

`tcp` — Display TCP traffic.

`udp` — Display UDP traffic.

`dns` — Display DNS traffic.

`http` — Display HTTP traffic.

`tls` — Display TLS traffic.

`tcp.port == 443` — Display TCP traffic using port 443.

`ip.addr == 192.168.1.10` — Display traffic involving a specific IP address.

---

## 🔬 Investigation Workflow

1. Capture network traffic.
2. Identify the communicating hosts.
3. Identify the protocols being used.
4. Apply display filters.
5. Investigate DNS requests.
6. Examine HTTP/HTTPS traffic.
7. Follow relevant TCP streams.
8. Analyze conversations.
9. Look for unusual behaviour.
10. Document the findings.

---

## 💡 Key Takeaway

Day 20 helped me understand that **network investigation is about connecting the dots**.

A single packet might not mean much.

But when packets are grouped into conversations, streams, DNS requests, and protocol activity, they can reveal what is actually happening on a network.

> Don't just look at packets. Investigate the story they tell.

---

## 🛠️ Tools Used

- Wireshark
- Windows networking tools
- Local network traffic

---

## 🚀 Progress

**Day 20 / 30 — Completed ✅**

Next: **Day 21 — 🔥 Wireshark Investigation**
