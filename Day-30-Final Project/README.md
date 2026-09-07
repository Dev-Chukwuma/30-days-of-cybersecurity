# Day 30 - Final Project: Full Incident Report

## Overview
The capstone for the 30 Days of Cybersecurity challenge — a full simulated attack chain 
report ("Operation Loose Thread") that ties together tools, techniques, and skills built 
across the entire month into one coherent security narrative.

## What This Project Does
Rather than a single isolated exercise, this project reconstructs a realistic incident from 
initial reconnaissance through credential compromise, detection, investigation, and response 
— using real artifacts produced during the challenge as evidence at each stage:

- **Reconnaissance** → Day 13's custom Python port scanner
- **Credential Access** → Day 20's Wireshark FTP capture + Day 15's offline password cracking
- **Automated Detection** → `credential_sniffer.py`, built for this capstone, validated 
  against the Day 20 capture
- **SIEM Detection** → Day 24's Splunk pipeline
- **Investigation** → Day 28's SOC investigation process
- **MITRE ATT&CK Mapping** → full technique chain across all stages
- **Response** → Day 25's 6-phase incident response lifecycle applied end-to-end

## Full Report
See [FINAL_REPORT.md](./FINAL_REPORT.md) for the complete incident writeup.

## What This Demonstrates
The ability to connect reconnaissance, exploitation, detection, investigation, and response 
into one coherent story — the core skill a SOC analyst or detection engineer applies to 
every real alert, rather than treating security skills as isolated, disconnected exercises.

## Challenge Complete 🎉
This marks the completion of all 30 days — from Linux/networking fundamentals through 
Python tooling, offensive security, packet investigation, SIEM work, incident response, 
MITRE ATT&CK, and this final full-chain capstone.
