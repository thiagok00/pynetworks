#!/usr/local/bin/python3
import os
from subprocess import call

print("CWD: " + os.getcwd())
print(f"UID: {os.getuid()}")
print("$PATH: " + os.getenv("PATH"))

os.system("echo Hello")

call(["echo", "Hi"])
