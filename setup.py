"""
Setup script for creating a standalone macOS app bundle
Run: python setup.py py2app
"""

from setuptools import setup

APP = ['sleep_timer_menubar.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': None,  # You can add a custom .icns file here
    'plist': {
        'CFBundleName': 'SleepTimer',
        'CFBundleDisplayName': 'Sleep Timer',
        'CFBundleGetInfoString': "Sleep Timer for macOS",
        'CFBundleIdentifier': "com.sleeptimer.app",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'LSUIElement': True,  # This makes it a menu bar only app (no dock icon)
    },
    'packages': ['rumps'],
}

setup(
    name='SleepTimer',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
