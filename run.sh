#!/bin/bash
# Etch DSL-Based Reimbursement Engine
# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>

python3 -c "from model import predict; print(predict($1, $2, $3))"
