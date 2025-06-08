import math

def predict(days: int, miles: float, receipts: float) -> float:
    
    # BASE PER-DIEM - Run 19: Adding 6-day bonus to complete sweet spot
    base_per_diem = days * 101  # Tiny increase from baseline 100
    
    # Trip length sweet spot bonuses (4-6 day range)
    if days == 4:
        base_per_diem = days * 104  # 4-day bonus (4% increase)
    elif days == 5:
        base_per_diem = days * 106  # 5-day bonus (6% increase) 
    elif days == 6:
        base_per_diem = days * 103  # NEW: 6-day bonus (3% increase)
    # Long trip penalties
    elif days >= 14:
        base_per_diem = days * 75  # Same as baseline
    elif days >= 10:
        base_per_diem = days * 90  # Same as baseline
    
    # MILEAGE COMPONENT - Run 13 parameters
    if miles <= 100:
        mileage_rate = 0.59  # From baseline 0.58
    elif miles <= 600:
        mileage_rate = 0.59 - 0.12 * math.log10(miles / 100)  # Baseline formula with 0.59 base
    else:  # miles > 600
        mileage_rate = 0.49  # Small increase from baseline 0.48
    
    mileage_component = miles * mileage_rate
    
    # RECEIPTS COMPONENT - Run 17: Big jump to 0.48
    if receipts <= 1000:
        receipt_component = receipts * 0.48  # Big jump from 0.43 to 0.48
    else:
        # Excess rate unchanged from Run 13
        receipt_component = 1000 * 0.48 + (receipts - 1000) * 0.17
    
    # EFFICIENCY ADJUSTMENTS - Run 13 parameters
    miles_per_day = miles / days if days > 0 else 0
    efficiency_bonus = 0
    
    # Sweet spot efficiency bonus
    if 180 <= miles_per_day <= 220:
        efficiency_bonus = 52  # Tiny increase from baseline 50
    elif miles_per_day < 80:
        efficiency_bonus = -30  # Same as baseline
    
    # High-mileage bonus
    if miles > 800:
        efficiency_bonus += 42  # Small increase from baseline 40
    
    # FINAL CALCULATION
    total = base_per_diem + mileage_component + receipt_component + efficiency_bonus
    
    return max(0, round(total, 2))
