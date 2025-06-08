import sys

days = float(sys.argv[1])
miles = float(sys.argv[2])
receipts = float(sys.argv[3])

# Dummy placeholder formula
result = round(days * 50 + miles * 0.57 + min(receipts, 100), 2)
print(result)
