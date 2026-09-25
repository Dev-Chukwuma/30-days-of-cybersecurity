# Day 02 - How the Internet Works

## Topics Covered
- How data actually travels from your device to a website and back
- DNS (Domain Name System) — how domain names become IP addresses
- Routers and ISPs — the path data takes across networks
- Packet switching — how the internet breaks data into pieces
- HTTP/HTTPS request-response basics

## What I Learned

### The internet is a network of networks
The internet isn't one single network — it's millions of smaller networks (ISPs, companies, 
data centers) all interconnected and agreeing to route each other's traffic. When you visit 
a website, your request hops across multiple networks before reaching its destination.

### DNS — the internet's phonebook
Humans use domain names (`google.com`) because they're memorable, but computers route 
traffic using IP addresses. DNS is the system that translates a domain name into the IP 
address of the server hosting it.

The basic flow when you type a URL:
1. Your device checks its local DNS cache first
2. If not cached, it queries a DNS resolver (often provided by your ISP or a public one 
   like `8.8.8.8`)
3. The resolver queries a chain of DNS servers (root → TLD → authoritative) until it finds 
   the IP address for that domain
4. Your device now has the IP and can connect directly to that server

This matters for security because DNS can be abused — DNS spoofing/poisoning redirects 
users to malicious servers by lying about which IP a domain maps to, and malware often uses 
DGA (Domain Generation Algorithms) to generate throwaway domains for command-and-control, 
which is why unusual/randomly-generated-looking domains are a red flag in log analysis.

### Packet Switching
Data isn't sent as one continuous stream — it's broken into small chunks called packets. 
Each packet is sent independently, potentially via different paths across the network, and 
reassembled in the correct order at the destination. This is more efficient and resilient 
than a single dedicated connection (if one path fails, packets can reroute).

Each packet carries:
- Source and destination IP addresses
- A piece of the actual data
- Sequencing information so it can be reassembled correctly

### HTTP/HTTPS — how a webpage actually loads
1. Your browser resolves the domain via DNS
2. Your browser sends an HTTP(S) **request** to the server's IP on port 80 (HTTP) or 443 
   (HTTPS)
3. The server processes the request and sends back an HTTP **response** — status code, 
   headers, and the actual content (HTML/CSS/JS/data)
4. HTTPS adds TLS encryption on top of this exchange, so the request/response can't be read 
   or tampered with in transit — this is exactly what was missing in the plaintext FTP 
   traffic investigated later in this challenge (Day 20)

### Routers and ISPs
A **router** directs packets toward their destination based on IP address, hop by hop. Your 
home router connects your local network to your **ISP** (Internet Service Provider), who 
connects you to the wider internet backbone — a mesh of interconnected networks maintained 
by many providers globally.

## Hands-On
- Ran `nslookup`/`dig` against a domain to manually perform DNS resolution and see the 
  returned IP address
- Used `traceroute` again, this time specifically to observe how many hops and different 
  networks a request crosses to reach an external site
- Inspected browser dev tools (Network tab) to observe an actual HTTP request/response cycle

## Key Insight
Every website visit is really a small relay race: DNS resolution → routing across multiple 
networks → a request/response exchange with a server, all happening in milliseconds. 
Understanding this flow is what makes later concepts (DNS-based attacks, packet capture, 
traffic analysis) make sense instead of feeling abstract.

## Next
Day 03 - Ports & Protocols