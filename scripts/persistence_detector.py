import json
import time

LOG_FILE = "/var/ossec/logs/archives/archives.json"

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

def analyze():
    with open(LOG_FILE, "r") as f:
        loglines = follow(f)

        print(" Monitoring persistence activity...\n")

        for line in loglines:
            try:
                log = json.loads(line)

                event_id = log.get("data", {}).get("win", {}).get("system", {}).get("eventID")
                event_data = log.get("data", {}).get("win", {}).get("eventdata", {})

                # Registry
                if event_id == "4657":
                    print("\n Registry Persistence Detected")
                    print(event_data)

                # Scheduled Task
                if event_id == "4698":
                    print("\n Scheduled Task Persistence Detected")
                    print(event_data)

                # Suspicious Service
                if event_id == "7045":
                    print("\n Service Persistence Detected")
                    print(event_data)

            except:
                continue

if __name__ == "__main__":
    analyze()
