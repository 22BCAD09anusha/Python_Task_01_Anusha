import os
import platform
import sys

print("Operating System Name:", platform.system())
print("Current Username:", os.getlogin())
print("Current Working Directory:", os.getcwd())
print("Python Version:", sys.version)