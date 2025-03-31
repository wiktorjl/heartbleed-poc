#!/usr/bin/python
import os
import random
import string
import sys
import time

# Create a large memory buffer to store our "leaked" data
MEMORY_SIZE = 1024 * 1024 * 10 # 10 MB
memory_buffer = bytearray(MEMORY_SIZE)

# List of secrets that might be leaked
# SECRETS = [
# "FLAG{HEARTBLEED_MEMORY_EXPOSURE_2023}",
# "API_KEY=4jf8h4f9h24fh9824hf9284fh29",
# "DATABASE_PASSWORD=Sup3rS3cr3tP@ssw0rd!",
# "ADMIN_CREDENTIALS=admin:HeartbleedAdmin2023",
# "SSH_PRIVATE_KEY=-----BEGIN RSA PRIVATE KEY-----\\nMIIEpAIBAAKCAQEAwJ1YX1lyV1WRxrgRNJL...",
# "AWS_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
# "CREDIT_CARD=4111-1111-1111-1111 CVV:123 EXP:12/28",
# "BITCOIN_WALLET_KEY=5Kb8kLf9zgWQnogidDA76MzPL6TsZZY36hWXMssSzNydYXYB9KF",
# "HEARTBLEED_SECRET=If_You_Can_See_This_The_Exploit_Worked!",
# "LOGIN_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkhlYXJ0YmxlZWQgVnVsbmVyYWJsZSBVc2VyIiwiaWF0IjoxNTE2MjM5MDIyfQ",
# "OAUTH_TOKEN=ya29.a0AfH6SMDb1K8VJzXjS_VYaL-xYQ-zlxKsF2JYf5j8",
# "SECURITY_ANSWER=mothers_maiden_name:Smith",
# "SECRET_COOKIE=session=eyJsb2dnZWRpbiI6dHJ1ZSwidXNlcm5hbWUiOiJhZG1pbiJ9",
# "-----MASTER PASSWORD-----\\nThisIsTheHeartbleedMasterPassword!\\n-----END MASTER PASSWORD-----",
# ]

SECRETS = [
"FLAG{HEARTBLEED_MEMORY_EXPOSURE_2023}",
"API_KEY=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
"DATABASE_PASSWORD=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"ADMIN_CREDENTIALS=CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
"SSH_PRIVATE_KEY=-----BEGIN RSA PRIVATE KEY-----\\nDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDd.",
"AWS_SECRET_KEY=EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
"CREDIT_CARD=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf",
"BITCOIN_WALLET_KEY=GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
"HEARTBLEED_SECRET=HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
"LOGIN_TOKEN=IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",
"OAUTH_TOKEN=JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ",
"SECURITY_ANSWER=LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
"SECRET_COOKIE=MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
"-----MASTER PASSWORD-----\\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\\n-----END MASTER PASSWORD-----",
]

# Fill memory with garbage and occasionally insert secrets
def fill_memory():
    global memory_buffer
    # Fill with random data
    for i in range(0, MEMORY_SIZE, 1024):
        chunk = bytearray(random_string(1024))
        memory_buffer[i:i+1024] = chunk

    # Insert secrets at random positions
    for secret in SECRETS:
        pos = random.randint(0, MEMORY_SIZE - len(secret) - 1)
        memory_buffer[pos:pos+len(secret)] = bytearray(secret)

def random_string(length):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Main loop
def main():
    while True:
        # Regenerate memory every few seconds
        fill_memory()

        # Create a heartbeat string that will be visible in memory
        heartbeat = "HEARTBEAT: " + random_string(32) + " TIME: " + str(time.time())
        pos = random.randint(0, MEMORY_SIZE - len(heartbeat) - 1)
        memory_buffer[pos:pos+len(heartbeat)] = bytearray(heartbeat)

        # Sleep for a bit
        time.sleep(1)

# Start as daemon
if os.fork() == 0:
    main()
else:
    sys.exit(0)