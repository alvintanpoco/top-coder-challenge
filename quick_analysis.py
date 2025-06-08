#!/usr/bin/env python3
import json

# Load public cases
with open('public_cases.json', 'r') as f:
    cases = json.load(f)

# Quick stats analysis
total_cases = len(cases)
print(f"Total cases: {total_cases}")

# Look at some high-error cases from your analysis
high_error_indices = [683, 995, 151, 547, 710]

print("\nHigh error cases analysis:")
for i in high_error_indices:
    if i < len(cases):
        case = cases[i]
        days = case['input']['trip_duration_days']
        miles = case['input']['miles_traveled']
        receipts = case['input']['total_receipts_amount']
        expected = case['expected_output']
        
        print(f"Case {i}: {days} days, {miles} miles, ${receipts:.2f} receipts -> Expected: ${expected:.2f}")

# Check receipt ranges
high_receipts = 0
for case in cases:
    if case['input']['total_receipts_amount'] > 1800:
        high_receipts += 1

print(f"\nCases with receipts > $1800: {high_receipts}")

# Calculate simple linear relationship
total_receipts = sum(case['input']['total_receipts_amount'] for case in cases)
total_expected = sum(case['expected_output'] for case in cases)
print(f"Avg receipts: ${total_receipts/total_cases:.2f}")
print(f"Avg expected: ${total_expected/total_cases:.2f}")
print(f"Rough receipt multiplier: {total_expected/total_receipts:.3f}")
