import sys
import random
import string
import time
sys.path.insert(0, "/var/www/flask")
from flask import Flask

app = Flask(__name__)

# Function to generate random memory activity
def memory_activity():
    # Create a 100KB array of random data just to use memory
    data = []
    for i in range(100):
        data.append("".join(random.choice(string.ascii_letters) for _ in range(1024)))
    return data

@app.route("/")
def hello():
    # Generate some memory activity on each request
    data = memory_activity()
    # Add a timestamp so the memory is different each time
    timestamp = str(time.time())
    return "<h1>Welcome to the Heartbleed Vulnerable Server</h1>" + \
           "<p>This server runs OpenSSL 1.0.1f which is vulnerable to the Heartbleed bug (CVE-2014-0160).</p>" + \
           "<p>Try using the Heartbleed exploit to retrieve data from memory!</p>" + \
           "<p>Current time: " + timestamp + "</p>"