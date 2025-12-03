#!/usr/bin/env python3
"""
Sleep Timer Menu Bar App for macOS
A simple menu bar application to schedule macOS sleep/shutdown
"""

import rumps
import subprocess
import threading
from datetime import datetime, timedelta


class SleepTimerApp(rumps.App):
    def __init__(self):
        super(SleepTimerApp, self).__init__("💤", quit_button=None)
        self.timer_active = False
        self.remaining_seconds = 0
        self.action_type = "sleep"  # 'sleep' or 'shutdown'
        
        # Build the menu
        self.menu = [
            rumps.MenuItem("Sleep Timer", callback=None),
            rumps.separator,
            rumps.MenuItem("10 minutes", callback=self.start_timer_10),
            rumps.MenuItem("30 minutes", callback=self.start_timer_30),
            rumps.MenuItem("60 minutes", callback=self.start_timer_60),
            rumps.MenuItem("120 minutes", callback=self.start_timer_120),
            rumps.MenuItem("180 minutes", callback=self.start_timer_180),
            rumps.MenuItem("Custom...", callback=self.start_timer_custom),
            rumps.separator,
            rumps.MenuItem("Action: Sleep Mac", callback=self.toggle_action),
            rumps.separator,
            rumps.MenuItem("Cancel Timer", callback=self.cancel_timer),
            rumps.separator,
            rumps.MenuItem("Quit", callback=self.quit_app),
        ]
        
        self.update_menu_state()
    
    @rumps.timer(1)
    def update_display(self, _):
        """Update the menu bar title with remaining time every second"""
        if self.timer_active and self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            
            hours = self.remaining_seconds // 3600
            minutes = (self.remaining_seconds % 3600) // 60
            seconds = self.remaining_seconds % 60
            
            if hours > 0:
                self.title = f"💤 {hours}:{minutes:02d}:{seconds:02d}"
            else:
                self.title = f"💤 {minutes}:{seconds:02d}"
            
            # Check if timer has finished
            if self.remaining_seconds == 0:
                self.execute_action()
        elif not self.timer_active:
            self.title = "💤"
    
    def update_menu_state(self):
        """Update menu items based on timer state"""
        if self.timer_active:
            self.menu["Cancel Timer"].set_callback(self.cancel_timer)
            # Disable time selection when timer is active
            for item in ["10 minutes", "30 minutes", "60 minutes", "120 minutes", "180 minutes", "Custom..."]:
                self.menu[item].set_callback(None)
        else:
            self.menu["Cancel Timer"].set_callback(None)
            # Enable time selection when timer is inactive
            self.menu["10 minutes"].set_callback(self.start_timer_10)
            self.menu["30 minutes"].set_callback(self.start_timer_30)
            self.menu["60 minutes"].set_callback(self.start_timer_60)
            self.menu["120 minutes"].set_callback(self.start_timer_120)
            self.menu["180 minutes"].set_callback(self.start_timer_180)
            self.menu["Custom..."].set_callback(self.start_timer_custom)
    
    def toggle_action(self, sender):
        """Toggle between sleep and shutdown actions"""
        if self.action_type == "sleep":
            self.action_type = "shutdown"
            sender.title = "Action: Shutdown Mac"
        else:
            self.action_type = "sleep"
            sender.title = "Action: Sleep Mac"
    
    def start_timer_10(self, _):
        self.start_timer(10)
    
    def start_timer_30(self, _):
        self.start_timer(30)
    
    def start_timer_60(self, _):
        self.start_timer(60)
    
    def start_timer_120(self, _):
        self.start_timer(120)
    
    def start_timer_180(self, _):
        self.start_timer(180)
    
    def start_timer_custom(self, _):
        """Prompt user for custom time in minutes"""
        response = rumps.Window(
            title="Custom Timer",
            message="Enter time in minutes:",
            default_text="90",
            ok="Start Timer",
            cancel="Cancel"
        ).run()
        
        if response.clicked:
            try:
                minutes = int(response.text)
                if minutes > 0:
                    self.start_timer(minutes)
                else:
                    rumps.alert("Invalid Input", "Please enter a positive number.")
            except ValueError:
                rumps.alert("Invalid Input", "Please enter a valid number.")
    
    def start_timer(self, minutes):
        """Start the countdown timer"""
        if self.timer_active:
            self.cancel_timer(None)
        
        self.remaining_seconds = minutes * 60
        self.timer_active = True
        self.update_menu_state()
        
        # Calculate end time
        end_time = datetime.now() + timedelta(minutes=minutes)
        
        # Show notification
        action_text = "sleep" if self.action_type == "sleep" else "shutdown"
        rumps.notification(
            title="Sleep Timer Started",
            subtitle=f"Mac will {action_text} in {minutes} minutes",
            message=f"Scheduled for {end_time.strftime('%H:%M:%S')}"
        )
    
    def cancel_timer(self, _):
        """Cancel the active timer"""
        if self.timer_active:
            self.timer_active = False
            self.remaining_seconds = 0
            self.title = "💤"
            
            self.update_menu_state()
            
            rumps.notification(
                title="Timer Cancelled",
                subtitle="Sleep timer has been cancelled",
                message=""
            )
    
    def execute_action(self):
        """Execute the sleep or shutdown action"""
        self.timer_active = False
        self.title = "💤"
        self.update_menu_state()
        
        try:
            if self.action_type == "sleep":
                # Show final notification
                rumps.notification(
                    title="Putting Mac to Sleep",
                    subtitle="Sleep timer completed",
                    message="Your Mac will sleep now"
                )
                # Execute sleep command
                subprocess.run(["pmset", "sleepnow"], check=True)
            else:
                # Show final notification
                rumps.notification(
                    title="Shutting Down Mac",
                    subtitle="Sleep timer completed",
                    message="Your Mac will shutdown now"
                )
                # Execute shutdown command
                subprocess.run(["osascript", "-e", 'tell app "System Events" to shut down'], check=True)
        except Exception as e:
            rumps.alert("Error", f"Failed to {self.action_type} Mac: {str(e)}")
    
    def quit_app(self, _):
        """Quit the application"""
        if self.timer_active:
            response = rumps.alert(
                title="Timer Active",
                message="A timer is currently active. Are you sure you want to quit?",
                ok="Quit",
                cancel="Cancel"
            )
            if response == 0:  # Cancel
                return
        
        rumps.quit_application()


if __name__ == "__main__":
    SleepTimerApp().run()
