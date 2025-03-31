#!/usr/bin/python
import os
import random
import string
import sys
import time
import urllib2

def simulate_users():
    while True:
        try:
            # Simulate a login with sensitive information
            credentials = {
                "username": "admin@example.com",
                "password": "HeartbleedDemo2023!",
                "api_key": "heartbleed_api_key_" + "".join(random.choice(string.hexdigits) for _ in range(16)),
                "session_token": "".join(random.choice(string.ascii_letters + string.digits) for _ in range(64)),
                "credit_card": "4111-1111-1111-1111 CVV:" + "".join(random.choice(string.digits) for _ in range(3)),
                "secret_flag": "FLAG{HEARTBLEED_" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16)) + "}"
            }

            # Make a request to the server
            req = urllib2.Request("https://localhost/")
            req.add_header("Cookie", "session=" + credentials["session_token"])
            req.add_header("Authorization", "Bearer " + credentials["api_key"])
            response = urllib2.urlopen(req, timeout=5)

            # Print a log message
            print("[%s] Simulated user activity with credentials: %s" % (time.ctime(), credentials["username"]))

            # Wait a random amount of time
            time.sleep(random.uniform(0.5, 2.0))
        except Exception as e:
            # Print the error and wait
            print("[%s] Error simulating user: %s" % (time.ctime(), str(e)))
            time.sleep(1)

# Start as daemon
if os.fork() == 0:
    simulate_users()
else:
    sys.exit(0)