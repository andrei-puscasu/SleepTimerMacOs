# Sleep Timer - macOS Menu Bar App

A simple and elegant menu bar application for macOS that allows you to schedule your Mac to sleep or shutdown after a specified time.

## Features

- 💤 **Menu Bar Integration** - Lives in your menu bar for easy access
- ⏱️ **Preset Timers** - Quick access to 10, 30, 60, 120, and 180-minute timers
- ✏️ **Custom Time** - Set your own custom timer duration
- 🔔 **Notifications** - Get notified when timer starts and completes
- ⏳ **Live Countdown** - See remaining time directly in the menu bar
- 🛑 **Cancel Anytime** - Cancel active timer with one click
- 🔀 **Sleep or Shutdown** - Choose between putting Mac to sleep or shutting down
- 🎯 **Lightweight** - Minimal resource usage

## Installation

### Option 1: Run with Python (Requires Python 3)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   python sleep_timer_menubar.py
   ```

### Option 2: Build Standalone App (Recommended)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build the app:**
   ```bash
   python setup.py py2app
   ```

3. **The app will be created in the `dist/` folder**
   - Find `SleepTimer.app` in the `dist` folder
   - Drag it to your Applications folder
   - Double-click to run!

## Usage

1. **Launch the app** - You'll see a 💤 icon in your menu bar
2. **Click the icon** to see timer options
3. **Select a time preset** (10, 30, 60, 120, or 180 minutes) or choose "Custom..."
4. **Watch the countdown** in the menu bar showing remaining time
5. **Cancel anytime** by clicking "Cancel Timer"
6. **Toggle action** between "Sleep Mac" and "Shutdown Mac"

### Menu Options

- **Time Presets**: 10, 30, 60, 120, 180 minutes
- **Custom...**: Enter any custom duration in minutes
- **Action**: Toggle between Sleep and Shutdown
- **Cancel Timer**: Stop the active countdown
- **Quit**: Close the application

## Permissions

The app requires permission to:
- Display notifications (for timer alerts)
- Control system sleep/shutdown

macOS may prompt you to grant these permissions on first use.

## Compatibility

- Compatible with macOS 10.10 (Yosemite) and later
- Tested on macOS Monterey, Ventura, and Sonoma
- Works on both Intel and Apple Silicon Macs

## Troubleshooting

**App won't sleep/shutdown the Mac:**
- You may need to grant the app accessibility permissions
- Go to System Settings → Privacy & Security → Accessibility
- Add the app to the allowed list

**Notifications not showing:**
- Go to System Settings → Notifications
- Find SleepTimer and enable notifications

## Development

The original command-line version is available in `sleep_timer.py`.

## License

Free to use and modify as needed.

## Credits

Built with [rumps](https://github.com/jaredks/rumps) - Ridiculously Uncomplicated macOS Python Statusbar apps
