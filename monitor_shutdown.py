import os
import time

# Specify the restricted file path
RESTRICTED_FILE = "restricted_file.txt"

def monitor_restricted_file(file_path):
    print(f"Monitoring access to: {file_path}")
    
    # Ensure the restricted file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("This is a restricted file.")
        print(f"Restricted file created at: {file_path}")

    # Get the initial file access time
    initial_access_time = os.path.getatime(file_path)

    try:
        while True:
            # Get the current access time of the file
            current_access_time = os.path.getatime(file_path)
            
            if current_access_time != initial_access_time:
                print("Unauthorized access detected! Initiating shutdown...")
                os.system("shutdown /s /t 10")  # Shutdown in 10 seconds
                break
            
            time.sleep(2)  # Check every 2 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_restricted_file(RESTRICTED_FILE)
