# Setup Guide – Persistence Detection Lab

## Requirements

* Wazuh Server (Ubuntu)
* Windows 10 endpoint with Wazuh agent
* Python 3

---

## Step 1 – Enable Windows Auditing

Run in PowerShell (Administrator):
```
auditpol /set /subcategory:"Registry" /success:enable /failure:enable
auditpol /set /subcategory:"Other Object Access Events" /success:enable /failure:enable
```

---

## Step 2 – Enable Registry Key Auditing

1. Open regedit
2. Navigate to:
   HKCU\Software\Microsoft\Windows\CurrentVersion\Run
3. Right click -> Permissions -> Advanced -> Auditing
4. Add "Everyone"
5. Enable:

   * Set Value
   * Create Subkey

---

## Step 3 – Restart Windows

---

## Step 4 – Run Detection Script

```
sudo python3 persistence_detector.py
```

---

## Step 5 – Simulate Persistence

### Registry
```
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v updater /t REG_SZ /d "powershell.exe"
```
### Scheduled Task
```
schtasks /create /sc minute /mo 5 /tn "UpdaterTask" /tr "powershell.exe"
```
### Service (run in CMD as Administrator)
```
cmd.exe /c sc create MyService binPath= "cmd.exe /c powershell.exe"
```
---

## Step 6 – Observe Detection

Expected:

* Registry persistence detected
* Scheduled task detected
* Service creation detected

---

## Troubleshooting

* Ensure logs are visible in /var/ossec/logs/archives/archives.json
* Ensure command is run as Administrator
* Verify Wazuh agent is active
