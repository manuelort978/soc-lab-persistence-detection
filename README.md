# SOC Lab – Persistence Detection (Windows and Wazuh)

## Overview

This project simulates persistence techniques used by attackers after initial compromise to maintain access to a Windows system.

The lab focuses on detecting registry modifications, scheduled tasks, and service creation using Wazuh SIEM and a custom Python detection script.

---

## Objectives

* Simulate post-exploitation persistence techniques
* Detect registry-based persistence (Run Keys)
* Detect scheduled task creation
* Detect malicious service installation
* Analyze security logs using Wazuh

---

## Techniques (MITRE ATT&CK)

* T1547 – Registry Run Keys / Startup Folder
* T1053 – Scheduled Tasks
* T1543 – Create or Modify System Process (Services)

---

## Simulated Attacks

### Registry Persistence
```
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v updater /t REG_SZ /d "powershell.exe"
```

### Scheduled Task
```
schtasks /create /sc minute /mo 5 /tn "UpdaterTask" /tr "powershell.exe"
```
### Service Persistence
```
cmd.exe /c sc create MyService binPath= "cmd.exe /c powershell.exe"
```

---

## Detection Logic

* Event ID 4657 -> Registry modification
* Event ID 4698 -> Scheduled task creation
* Event ID 7045 -> Service installation

---

## Features

* Real-time log monitoring
* Detection of persistence mechanisms
* Behavioral-based detection approach

---

## Example Output
```
 Registry Persistence Detected
 Scheduled Task Persistence Detected
 Service Persistence Detected
```
---

## Skills Demonstrated

* Threat detection (post-exploitation)
* Windows event log analysis
* SIEM monitoring (Wazuh)
* Python automation
* Security investigation

---

## Important Note

Registry persistence required additional auditing configuration to generate Event ID 4657.

This highlights the importance of proper log visibility in detecting advanced threats.

---

## Future Improvements

* Correlate persistence + execution
* Add alert scoring
* Automate response actions
