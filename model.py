import numpy as np
import pandas as pd

def predict(days: int, miles: float, receipts: float) -> float:
    # Model coefficients from your trained linear regression
    # TODO: Replace these with actual coefficients from your model
    # Run the coefficient extraction code to get these values
    coefficients = {
        'miles_traveled': 0.5,  # Replace with actual
        'trip_duration_days': 85.0,  # Replace with actual
        'total_receipts_amount': 0.3,  # Replace with actual
        'miles_per_day': -0.2,  # Replace with actual
        'log_miles': 50.0,  # Replace with actual
        'log_receipts': 100.0,  # Replace with actual
        'is_long_trip': -200.0,  # Replace with actual
        'is_five_day': 50.0,  # Replace with actual
        'receipt_bin': 25.0,  # Replace with actual
        'receipts_x_days': 0.01,  # Replace with actual
        'efficiency_bonus_zone': 75.0,  # Replace with actual
        'receipts_squared': 0.0001,  # Replace with actual
        'five_day_bonus': 1.0,  # Replace with actual
        'low_receipt_penalty': 1.0,  # Replace with actual
        'mileage_adjusted': 0.8,  # Replace with actual
        'mileage_longtrip_penalty': 1.0,  # Replace with actual
    }
    
    intercept = 0.0  # Replace with model.intercept_
    
    # Feature Engineering (matching your training code exactly)
    miles_per_day = miles / days
    log_miles = np.log1p(miles)
    log_receipts = np.log1p(receipts)
    is_long_trip = int(days >= 14)
    is_five_day = int(days == 5)
    
    # Receipt binning
    if receipts <= 600:
        receipt_bin = 0
    elif receipts <= 800:
        receipt_bin = 1
    elif receipts <= 1200:
        receipt_bin = 2
    elif receipts <= 1800:
        receipt_bin = 3
    else:
        receipt_bin = 4
    
    receipts_x_days = receipts * days
    efficiency_bonus_zone = int(180 <= miles_per_day <= 220)
    receipts_squared = receipts ** 2
    five_day_bonus = is_five_day * days * 100 * 0.05
    low_receipt_penalty = int(receipts < 200) * -25
    
    # Mileage component (matching your training function)
    if miles <= 100:
        mileage_adjusted = miles * 0.58
    elif miles <= 600:
        mileage_adjusted = miles * (0.58 - 0.12 * np.log10(miles / 100))
    else:
        mileage_adjusted = miles * 0.36
    
    mileage_longtrip_penalty = mileage_adjusted * is_long_trip * -0.15
    
    # Linear regression prediction
    total = intercept
    total += coefficients['miles_traveled'] * miles
    total += coefficients['trip_duration_days'] * days
    total += coefficients['total_receipts_amount'] * receipts
    total += coefficients['miles_per_day'] * miles_per_day
    total += coefficients['log_miles'] * log_miles
    total += coefficients['log_receipts'] * log_receipts
    total += coefficients['is_long_trip'] * is_long_trip
    total += coefficients['is_five_day'] * is_five_day
    total += coefficients['receipt_bin'] * receipt_bin
    total += coefficients['receipts_x_days'] * receipts_x_days
    total += coefficients['efficiency_bonus_zone'] * efficiency_bonus_zone
    total += coefficients['receipts_squared'] * receipts_squared
    total += coefficients['five_day_bonus'] * five_day_bonus
    total += coefficients['low_receipt_penalty'] * low_receipt_penalty
    total += coefficients['mileage_adjusted'] * mileage_adjusted
    total += coefficients['mileage_longtrip_penalty'] * mileage_longtrip_penalty
    
    return round(total, 2)