import math

def predict(days: int, miles: float, receipts: float) -> float:
    """
    Enhanced Receipts Component (v2) - Refined for 17321.00 target
    Addresses over-prediction issues while maintaining receipts insight
    """
    
    # BASE PER-DIEM
    base_per_diem = days * 100
    
    # Five-day bonus (5% increase)
    if days == 5:
        base_per_diem = days * 105
    
    # Long trip taper to address over-prediction
    elif days >= 14:
        base_per_diem = days * 85  # Significant reduction for very long trips
    elif days >= 8:
        base_per_diem = days * 95  # Moderate reduction for long trips
    
    # MILEAGE COMPONENT with tiered rates
    if miles <= 100:
        mileage_rate = 0.58
    elif miles <= 600:
        # Logarithmic decay from 0.58 to 0.36
        mileage_rate = 0.58 - 0.12 * math.log10(miles / 100)
    else:  # miles > 600
        mileage_rate = 0.36  # plateau for very long trips
    
    mileage_component = miles * mileage_rate
    
    # RECEIPTS COMPONENT - more conservative to reduce over-prediction
    if receipts <= 600:
        receipt_component = receipts * 0.25  # Reduced from 0.40
    else:
        # Strong diminishing returns for high receipts
        receipt_component = 600 * 0.25 + (receipts - 600) * 0.08
    
    # EFFICIENCY ADJUSTMENTS
    miles_per_day = miles / days if days > 0 else 0
    efficiency_bonus = 0
    
    # Sweet spot efficiency bonus
    if 180 <= miles_per_day <= 220:
        efficiency_bonus = 40  # Reduced from 60
    elif miles_per_day < 80:
        efficiency_bonus = -30  # Low efficiency penalty
    
    # FINAL CALCULATION
    total = base_per_diem + mileage_component + receipt_component + efficiency_bonus
    
    return max(0, round(total, 2))
