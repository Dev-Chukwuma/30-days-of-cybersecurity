# Day 16 — Cryptography Basics

## 📅 Overview
Day 16 covers the two main types of encryption — symmetric and asymmetric — with full hands-on demos of both, building on Day 15's hashing concepts.

---

## 🎯 Topics Covered

### Symmetric Encryption
- Same key encrypts and decrypts
- Algorithm: AES (used in Wi-Fi WPA2/3, BitLocker)
- Weakness: the key distribution problem — both parties need the same key, safely shared in advance

### Asymmetric Encryption (Public-Key Cryptography)
- Two mathematically linked keys: public (shareable) and private (secret, never shared)
- Algorithm: RSA
- Solves the key distribution problem — the public key can be shared openly
- Real-world use: SSH key-based login, HTTPS/TLS

---

## 🛠️ Hands-On: Symmetric Encryption (AES)

openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.txt -out secret.enc -k test123
openssl enc -d -aes-256-cbc -pbkdf2 -in secret.enc -out decrypted.txt -k test123

Same key (test123) used for both encrypt and decrypt.

**Troubleshooting note:** older OpenSSL key derivation is deprecated — added `-pbkdf2` for stronger key derivation, which resolved a warning about weak defaults.

---

## 🛠️ Hands-On: Asymmetric Encryption (RSA)

ssh-keygen -t rsa -b 2048 -f test_key
ssh-keygen -f test_key.pub -e -m PKCS8 > test_key_public.pem
openssl pkeyutl -encrypt -pubin -inkey test_key_public.pem -in secret2.txt -out secret2.enc
openssl rsa -in test_key -out test_key_openssl.pem
openssl pkeyutl -decrypt -inkey test_key_openssl.pem -in secret2.enc -out decrypted2.txt

**Troubleshooting note:** ssh-keygen's default private key format (OpenSSH) isn't directly compatible with OpenSSL's pkeyutl — had to convert it to PEM format first with `openssl rsa -in test_key -out test_key_openssl.pem` before decryption would work.

**Key observation:** encryption used one file (public key), decryption used a completely different file (private key) — no shared secret between them, unlike the AES demo.

---

## 🧠 Why This Matters
Cryptography underlies nearly all secure communication — HTTPS, SSH, VPNs, disk encryption. Understanding symmetric vs asymmetric, and troubleshooting real format/compatibility issues between tools, builds practical skills beyond just theory.

---

## ➡️ Next
**Day 17 — Common Attack Techniques**
