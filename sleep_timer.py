#!/usr/bin/env python3
"""
Sleep Timer for macOS
Puts the computer to sleep after a specified delay (default: 120 minutes)
"""

import time
import subprocess
import sys
from datetime import datetime, timedelta


def put_computer_to_sleep():
    """Execute the macOS sleep command."""
    try:
        subprocess.run(["pmset", "sleepnow"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error putting computer to sleep: {e}")
        sys.exit(1)
    except PermissionError:
        print("Permission denied. You may need to run this script with sudo.")
        sys.exit(1)


def main():
    # Sleep duration in minutes
    sleep_minutes = 120
    sleep_seconds = sleep_minutes * 60
    
    # Calculate sleep time
    sleep_time = datetime.now() + timedelta(minutes=sleep_minutes)
    
    print(f"🕐 Sleep timer started at {datetime.now().strftime('%H:%M:%S')}")
    print(f"💤 Computer will sleep in {sleep_minutes} minutes")
    print(f"⏰ Sleep scheduled for: {sleep_time.strftime('%H:%M:%S')}")
    print(f"\nPress Ctrl+C to cancel the timer\n")
    
    try:
        # Wait for the specified duration
        interval = 60  # Update every minute
        elapsed = 0
        
        while elapsed < sleep_seconds:
            time.sleep(min(interval, sleep_seconds - elapsed))
            elapsed += interval
            
            remaining_minutes = (sleep_seconds - elapsed) // 60
            if elapsed < sleep_seconds:
                print(f"⏳ {remaining_minutes} minutes remaining until sleep...")
        
        print("\n" + "="*50)
        print("⏰ Time's up! Putting computer to sleep...")
        print("="*50 + "\n")
        
        # Put computer to sleep
        put_computer_to_sleep()
        
    except KeyboardInterrupt:
        print("\n\n❌ Sleep timer cancelled by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
