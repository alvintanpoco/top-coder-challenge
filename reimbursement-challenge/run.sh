#!/bin/bash
DAYS=$1
MILES=$2
RECEIPTS=$3

RESULT=$(python3 main.py $DAYS $MILES $RECEIPTS)
echo $RESULT
