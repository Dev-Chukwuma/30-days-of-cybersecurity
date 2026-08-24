# Day 15 — Authentication & Password Security

## 📅 Overview
Day 15 covers how authentication works, how Linux stores passwords securely via hashing, and a hands-on demo cracking a weak password hash with John the Ripper.

---

## 🎯 Topics Covered

### Authentication Factors
- Something you know (password/PIN)
- Something you have (phone, security key)
- Something you are (fingerprint, face)
- MFA combines factors so a stolen password alone isn't enough

### Linux Password Storage
- `/etc/passwd` — account info (username, UID, home dir), readable by anyone
- `/etc/shadow` — actual password hashes, root-only
- Hashing is one-way (irreversible) — unlike encryption, there's no key to steal that could reverse every password at once

### Cracking a Weak Hash (John the Ripper)
- Generated an MD5 hash of a test password
- Used `john --format=raw-md5` to crack it via wordlist attack
- Confirmed the crack with `john --show`
- Weak/common passwords crack fast because they're in standard wordlists; strong random passphrases are not

### Windows Comparison (NTLM)
- Windows stores hashes in the SAM file, locked while the OS runs
- NTLM is Windows' hash format (built on MD4)
- Generated and cracked a test NTLM hash for comparison with Linux's approach

---

## 🧠 Why This Matters
Understanding how password hashing and cracking work — even at a basic level — is core "know your enemy" knowledge for Blue Team work: it explains why weak password policies are a real risk, and informs how to evaluate password security in an audit or incident.

---

## ➡️ Next
**Day 16 — Cryptography Basics**
