# Day 08 — Linux Users & Permissions

## 📅 Overview
Day 8 goes deeper into Linux users and permissions, building on Day 4 fundamentals. Focus: understanding not just the commands, but why permission misconfigurations are a real, common attack vector in security work.

---

## 🎯 Topics Covered

### Users, UID & GID
- **UID (User ID)** — unique number identifying a user; root is always UID 0
- **GID (Group ID)** — unique number identifying a group
- Linux tracks users/groups internally by number, not name

### Renaming a Linux User
- Must not be actively logged into the account being renamed (switch to a TTY session first: `Ctrl+Alt+F3`)
- `sudo usermod -l newname -d /home/newname -m oldname` — renames user and moves home directory
- `sudo groupmod -n newname oldname` — renames matching group
- `sudo hostnamectl set-hostname newhostname` — renames the machine itself

### File Permissions
- Three permission types: `r` (read), `w` (write), `x` (execute)
- Three categories: owner, group, others
- `ls -l` breaks down permissions per file

### chmod — Changing Permissions
- Symbolic method: `chmod u+x file` (u=user, g=group, o=others, a=all)
- Numeric method: `r=4, w=2, x=1`, summed per category
  - Example: `chmod 750 file` → owner: rwx, group: r-x, others: none

### chown — Changing Ownership
- `sudo chown owner:group file` — changes who owns a file/who its group is
- Permissions (chmod) define *what's allowed*; ownership (chown) defines *who it applies to*
- Real security risk: a world-writable file owned by root is a privilege escalation path

### Special Permissions
- **SUID** — executable runs with the file owner's privileges instead of the runner's (e.g. `passwd`)
- **SGID** — on directories, new files inherit the directory's group automatically
- **Sticky Bit** — in a shared writable directory (e.g. `/tmp`), only a file's owner can delete/rename it
- In `ls -l`: lowercase `s`/`t` = special bit + execute both on; uppercase `S`/`T` = special bit on, execute missing (unusual/misconfigured)

---

## 🧠 Why This Matters
Permission and ownership misconfigurations are one of the most common real-world privilege escalation paths. Knowing how to read `ls -l` output and spot a dangerous SUID binary or an overly-open file is a practical Blue Team skill, not just Linux trivia.

---

## ➡️ Next
**Day 09 — Processes & Services**
