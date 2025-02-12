#!/bin/sh 
cd src/client

# Disable screen saver and screen blanking
xset s off
xset -dpms


# Start the program
sudo DISPLAY=:0 ../../venv/bin/python single_instance.py
cd ../.. 

