#!/usr/bin/env python3
"""
Simple run.sh replacement that calls the model.py predict function
"""
import sys
from model import predict

# Read input from command line args or stdin
if len(sys.argv) == 4:
    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])
else:
    # Read from stdin
    line = sys.stdin.readline().strip()
    if line:
        parts = line.split()
        days = int(parts[0])
        miles = float(parts[1])
        receipts = float(parts[2])
    else:
        exit(1)

# Call the model and output the result
result = predict(days, miles, receipts)
print(result)
