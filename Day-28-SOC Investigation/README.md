# Day 28 - SOC Investigation

## Topics Covered
- The SOC investigation lifecycle: Triage → Gather Context → Correlate → Scope → Classify → Escalate
- Turning a raw SIEM alert into a documented decision
- Simulating and investigating a real brute-force-then-breach pattern in Splunk

## What I Learned
A SOC investigation is the process of taking a raw alert and turning it into a decision: 
is this a real threat, a false positive, or something worth escalating? A single event 
(like one failed login) usually isn't enough to act on — real alerts trigger on thresholds, 
like multiple failed logins in a short window from the same source.

The investigation flow ties together everything from earlier in the challenge: log analysis 
(Day 18) to spot patterns, SIEM search skills (Day 23-24) to correlate events, and incident 
response phases (Day 25) to know what happens after classification.

## Hands-On
- Simulated a failed-login burst (EventCode=4625) on the Windows host, same username/source, 
  clustered in time
- Followed with a successful logon (EventCode=4624) for the same account right after
- Correlated the two in Splunk — confirmed a classic brute-force-then-breach signature
- Classified it as a true positive and mapped it to MITRE ATT&CK: T1110.001 - Password Guessing 
  (online guessing, as opposed to Day 15's offline cracking - T1110.002)

## Key Insight
Investigation isn't just "did an alert fire" — it's connecting multiple events into a story. 
One failed login is noise. A burst of failures immediately followed by a success is a 
signature worth escalating.

## Next
Day 29 - [upcoming topic]
