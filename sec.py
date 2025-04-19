import datetime
import json
import os
import sys

# Initialize expiry date
EXPIRY_DATE = datetime.datetime(2025, 2, 28)
LAST_RUN_FILE = "last_run.json"

def is_expired():
    """
    Check if the program has expired.
    """
    return datetime.datetime.now() > EXPIRY_DATE

def detect_date_tampering():
    """
    Detect if the system date has been tampered with.
    """
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, 'r') as file:
            data = json.load(file)
            last_run_date = datetime.datetime.strptime(data['last_run'], '%Y-%m-%d %H:%M:%S')
            if datetime.datetime.now() < last_run_date:
                return True
    return False

def update_last_run_date():
    """
    Update the last run date in the JSON file.
    """
    with open(LAST_RUN_FILE, 'w') as file:
        data = {'last_run': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        json.dump(data, file)

def days_remaining():
    """
    Calculate the number of days remaining until expiry.
    """
    remaining = (EXPIRY_DATE - datetime.datetime.now()).days
    return remaining

def self_destruct():
    """
    Self-destruct the program by deleting its own script.
    """
    print("\033[91m\033[1mThis program has expired and will now self-destruct.\033[0m")
    script_path = os.path.abspath(sys.argv[0])
    try:
        os.remove(script_path)
    except Exception as e:
        print(f"Error during self-destruction: {e}")
    sys.exit(1)

def main():
    """
    Main function to handle program execution.
    """
    if is_expired():
        self_destruct()

    if detect_date_tampering():
        print("\033[91mDate tampering detected. Exiting...\033[0m")
        sys.exit(1)

    print(f"Program is running. Days remaining until expiry: {days_remaining()}")
    update_last_run_date()

if __name__ == "__main__":
    main()