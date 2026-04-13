# Findings – Persistence Detection Lab

## Summary
Multiple persistence techniques were successfully simulated and detected on a Windows endpoint.

## Observations
- Modification of the registry execution key was detected after enabling auditing.
- Scheduled task creation successfully detected
- Service creation detected after executing command with elevated privileges

## Analysis
The simulated techniques represent common attacker behavior during post-exploitation to maintain long-term access.

## Behavioral Indicators
- Unauthorized modification of startup registry keys
- Creation of scheduled tasks executing PowerShell
- Installation of suspicious services

## Privilege Insights
- Service creation required administrative privileges
- This indicates a higher level of compromise and attacker capability

## Limitations
- Registry detection required manual auditing configuration
- Without proper logging, this activity would not be visible

## Recommendations
- Enable advanced auditing policies
- Monitor persistence-related events continuously
- Alert on PowerShell-based persistence mechanisms
