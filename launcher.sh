#!/bin/sh 
cd ~/gify-box/src/client

# Disable screen saver and screen blanking
xset s off
xset -dpms


# Start the program
sudo ../../venv/bin/python single_instance.py
cd ../.. 

