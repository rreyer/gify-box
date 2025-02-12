#!/bin/sh 
cd src/client

# Disable screen saver and screen blanking
xset s off
xset -dpms

# Activate virtual environment
source "./venv/bin/activate"

# Start the program
sudo DISPLAY=:0 python single_instance.py
cd ../.. 

