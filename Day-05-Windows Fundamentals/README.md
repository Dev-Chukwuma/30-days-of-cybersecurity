# 🖥️ Day 5/30 — Windows System Investigation

## 🧾 System Information
I used:
```
systeminfo
```
to display important information about the Windows system, including:
- Windows version
- OS build
- Computer name
- System manufacturer
- System type
- Installed memory
- System configuration

I also used:
```
hostname
```
to identify the computer's hostname.

## 👤 Users
I used:
```
whoami
```
to identify the currently logged-in Windows user.

I also used:
```
net user
```
to view local user accounts.

To check members of the local Administrators group:
```
net localgroup administrators
```
This helped me understand which accounts have administrative privileges.

## ⚙️ Processes & PIDs
I used:
```
tasklist
```
to view running processes.

I learned that every running process has a unique PID (Process ID).

I also investigated specific processes using:
```
tasklist /FI "PID eq YOUR_PID"
```
This connected with what I learned earlier about `netstat -ano`.

The investigation flow is:
```
Network Connection
        ↓
       PID
        ↓
    Process
```

## 🌐 Network Configuration
I used:
```
ipconfig
```
to inspect my Windows network configuration.

I looked at:
- IPv4 Address
- Subnet Mask
- Default Gateway

I also used:
```
netstat -ano
```
to inspect network connections and their associated PIDs.

To focus on listening ports:
```
netstat -ano | findstr LISTENING
```
This helped me identify ports that were listening for incoming connections.

## 🔐 Windows File Permissions
I used:
```
icacls "%USERPROFILE%\Desktop"
```
to inspect file and folder permissions.

I learned some common Windows permission levels:
| Level | Meaning |
|-------|---------|
| F | Full Control |
| M | Modify |
| RX | Read & Execute |
| R | Read |
| W | Write |

Permissions determine what users and groups are allowed to do with files and folders.

## ⚙️ Windows Services
I used:
```
sc query state= running
```
to view running Windows services.

I also checked the Windows Defender service with:
```
sc query WinDefend
```
I learned that services run in the background and can provide important functionality to Windows and applications.

From a cybersecurity perspective, services are important because they can also be investigated during security incidents.

## 🛡️ Windows Defender
I checked the Windows Defender service using:
```
sc query WinDefend
```
This helped me understand how Windows security components can be checked from the command line.

## 📋 Windows Event Viewer
I opened Event Viewer using:
```
eventvwr.msc
```
I explored:
```
Windows Logs
    ↓
Security
```
I learned that Windows Security logs contain information that can be useful when investigating authentication and other security-related activity.

## 🧠 Key Takeaways
Today I learned how to:
- Inspect Windows system information
- Identify the current user
- View local users and administrators
- Investigate running processes
- Understand PIDs
- Check network configuration
- Investigate listening ports
- Inspect file permissions
- View running services
- Check Windows Defender
- Explore Windows Security logs

## 🧰 Commands Practiced
```
systeminfo
hostname
whoami
net user
net localgroup administrators
tasklist
tasklist /FI "PID eq YOUR_PID"
ipconfig
netstat -ano
netstat -ano | findstr LISTENING
icacls
sc query
sc query WinDefend
eventvwr.msc
```

## 📸 Evidence
Screenshots from today's practical exercises are included in this folder.

## ✅ Progress
**Day 5/30 — Completed**
