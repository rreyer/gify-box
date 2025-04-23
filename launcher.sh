#!/bin/sh 
cd /home/innospace/gify-box/src/client

#export DISPLAY=:0

# Disable screen saver and screen blanking
xset s off
xset -dpms


# Start the program
sudo ../../venv/bin/python single_instance.py
cd ../.. 

