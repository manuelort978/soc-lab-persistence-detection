# Persistence Techniques Detection

## Techniques Covered

### Registry Run Keys
- Location: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
- Purpose: Execute programs at user login

---

### Scheduled Tasks
- Allows execution at defined intervals
- Common for maintaining periodic access

---

### Services
- Persistent system-level execution
- Requires elevated privileges

---

## Detection Strategy

- Monitor Event ID: 4657 (registry)
- Monitor Event ID: 4698 (scheduled tasks)
- Monitor Event ID: 7045 (services)
- Analyze command content: (PowerShell usage)

---

## MITRE ATT&CK Mapping

- T1547 – Registry Run Keys
- T1053 – Scheduled Tasks
- T1543 – Services

---

## Results
Successful detection of persistence mechanisms commonly used by attackers after initial compromise
