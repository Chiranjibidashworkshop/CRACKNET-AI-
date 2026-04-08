import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.crack_simulator import time_to_crack, format_time

pwd = "Password@123"

brute, ai = time_to_crack(pwd)

print("Password:", pwd)
print("Brute-force time:", format_time(brute))
print("AI attack time:", format_time(ai))