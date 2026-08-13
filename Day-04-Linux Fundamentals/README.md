# 🐧 Day 4 — Linux Fundamentals

## 📚 Overview

Today I installed Linux and started getting hands-on with the Linux terminal.

The goal was to become comfortable navigating the Linux filesystem, managing files, understanding permissions, working with processes, and performing basic network operations.

---

## 🐧 What I Learned

### 📂 Linux Filesystem

Linux uses `/` as the root of its filesystem.

Some important directories include:

| Directory | Purpose |
|---|---|
| `/` | Root of the filesystem |
| `/home` | Users' personal files |
| `/etc` | System configuration files |
| `/var` | Variable data and logs |
| `/tmp` | Temporary files |
| `/usr` | Programs and system resources |

---

## 🧭 Basic Navigation

I practiced:

\`\`\`bash
pwd
ls
cd
\`\`\`

- `pwd` — Shows the current working directory
- `ls` — Lists files and directories
- `cd` — Changes directories

---

## 📁 File & Directory Management

I practiced creating and managing files and directories.

\`\`\`bash
mkdir
touch
cat
cp
mv
rm
\`\`\`

### Examples

Create a directory:
\`\`\`bash
mkdir security
\`\`\`

Create a file:
\`\`\`bash
touch commands.txt
\`\`\`

Read a file:
\`\`\`bash
cat commands.txt
\`\`\`

Copy a file:
\`\`\`bash
cp notes.txt backup.txt
\`\`\`

Move or rename a file:
\`\`\`bash
mv backup.txt linux-notes.txt
\`\`\`

Remove a file:
\`\`\`bash
rm linux-notes.txt
\`\`\`

---

## ✍️ Writing to Files

I also practiced using `echo`.

Overwrite a file:
\`\`\`bash
echo "Linux is essential for cybersecurity" > commands.txt
\`\`\`

Add to an existing file:
\`\`\`bash
echo "I am learning Linux fundamentals" >> commands.txt
\`\`\`

**Difference:**
- `>` = Overwrite
- `>>` = Append

---

## 🔐 Linux File Permissions

I learned about Linux permissions:

- `r` = Read
- `w` = Write
- `x` = Execute

Permissions are divided into:

**Owner | Group | Others**

For example:
\`\`\`
rwxr-xr--
\`\`\`

means:
- Owner  → `rwx`
- Group  → `r-x`
- Others → `r--`

I also practiced changing permissions with:
\`\`\`bash
chmod
\`\`\`

Example:
\`\`\`bash
chmod 600 security.txt
\`\`\`

This gives the owner read and write permissions while removing permissions for the group and others.

---

## 👤 Users & Groups

I learned how to identify the current user and view user/group information.

\`\`\`bash
whoami
\`\`\`
Shows the current username.

\`\`\`bash
id
\`\`\`
Shows information such as:
- User ID (UID)
- Group ID (GID)
- Groups the user belongs to

---

## ⚙️ Processes

A process is a program currently running on the system.

I used:
\`\`\`bash
ps
\`\`\`
and:
\`\`\`bash
ps aux
\`\`\`
to view running processes.

I also learned that processes have unique Process IDs (PIDs).

I used:
\`\`\`bash
ps aux | grep bash
\`\`\`
to search for processes containing bash.

The `|` symbol is a **pipe**, which sends the output of one command into another command.

---

## 🌐 Linux Networking

I practiced several basic networking commands.

**Check IP addresses**
\`\`\`bash
ip a
\`\`\`
This displays network interfaces and IP addresses.

**Check routing information**
\`\`\`bash
ip route
\`\`\`
This displays the system's routing table and default gateway.

**Test connectivity**
\`\`\`bash
ping -c 4 google.com
\`\`\`
This sends four ICMP packets to test connectivity and measure response time.

**View listening network ports**
\`\`\`bash
ss -tuln
\`\`\`
I used this to view listening TCP and UDP ports. The options mean:
- `-t` = TCP
- `-u` = UDP
- `-l` = Listening
- `-n` = Numeric output

**Make an HTTP request**
\`\`\`bash
curl -I https://example.com
\`\`\`
I used curl to make a request to a web server and view its HTTP response headers.

---

## 🧠 Cybersecurity Connection

Today's practical work helped me understand how Linux can be investigated from the command line.

I learned how to move from:

\`\`\`
User
  ↓
Files & Permissions
  ↓
Processes & PIDs
  ↓
Network Interfaces
  ↓
Listening Ports
  ↓
Network Connections
\`\`\`

This is important for cybersecurity because Linux is widely used for servers, security tools, cloud systems, and security investigations.

---

## 🧰 Commands Practiced

`pwd` · `ls` · `cd` · `mkdir` · `touch` · `cat` · `echo` · `cp` · `mv` · `rm` · `chmod` · `whoami` · `id` · `ps` · `grep` · `ip` · `ping` · `ss` · `curl`

---

## 🎯 Key Takeaways

- Linux uses `/` as the root of its filesystem.
- Files and directories can be managed directly from the terminal.
- Linux uses permissions to control access to files.
- Processes have unique PIDs.
- Linux provides powerful command-line networking tools.
- The terminal is an important tool for cybersecurity work.
