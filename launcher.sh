#!/bin/bash 

echo "$(date) - Startversuch" >> /home/innospace/gify-box/log.log
sleep 5

export DISPLAY=:0
export XAUTHORITY=/home/innospace/.Xauthority

# Disable screen saver and screen blanking
xset s off
xset -dpms


# Start the program
sudo /home/innospace/gify-box/venv/bin/python /home/innospace/gify-box/src/client/single_instance.py >> /home/innospace/gify-box/log.log 2>&1

