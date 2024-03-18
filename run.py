import subprocess
import sys
import time

def run_main_infinite():
    while True:
        try:
            # Run main.py
            subprocess.run(['python', 'main.py'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("Script execution stopped.")
            sys.exit(0)
        
        # Adjust sleep duration as needed
        time.sleep(1)

if __name__ == "__main__":
    run_main_infinite()
