#!/bin/bash
# Start the memory leaker in the background
/usr/local/bin/memory_leaker.py

# Wait for Apache to start
sleep 5

# Start the user simulator in the background
/usr/local/bin/user_simulator.py &

# Start Apache in the foreground
/usr/sbin/apache2ctl -D FOREGROUND