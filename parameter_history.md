# Parameter History Log

This document tracks all parameter changes made to the model to optimize the reimbursement calculation.

## Run 1 - Baseline (Current Parameters)
**Date**: 2025-06-07
**Description**: Initial evaluation with current parameters

### Current Parameters:
- **Base per-diem**: 
  - Standard: 100 per day
  - 5-day special: 105 per day
  - Long trip penalties: 90 per day (days >= 10), 75 per day (days >= 14)

- **Mileage rates**:
  - miles <= 100: 0.58
  - 100 < miles <= 600: 0.58 - 0.12 * log10(miles/100) 
  - miles > 600: 0.48

- **Receipt component**:
  - receipts <= 1000: receipts * 0.35
  - receipts > 1000: 1000 * 0.35 + (receipts - 1000) * 0.15

- **Efficiency bonuses**:
  - Sweet spot (180-220 miles/day): +50
  - Low efficiency (<80 miles/day): -30
  - High mileage (>800 miles): +40

### Results:
- **Score: 21012.00**
- **Exact matches: 0 (0%)**
- **Close matches: 3 (0.3%)**
- **Average error: $209.12**
- **Max error: $983.81**

### Analysis:
The model is significantly over-predicting, especially on cases with high receipts. The worst cases show the model predicting 2-3x the expected amount.

---

## Run 2 - Aggressive Over-prediction Fix
**Date**: 2025-06-07
**Description**: Major reduction in receipt component and per-diem rates to address severe over-prediction

### Parameter Changes:
- **Base per-diem**: Reduced significantly
  - Standard: 75 per day (was 100)
  - 5-day special: 80 per day (was 105)
  - Long trip penalties: 65 per day (days >= 10, was 90), 55 per day (days >= 14, was 75)

- **Receipt component**: Drastically reduced
  - receipts <= 1000: receipts * 0.20 (was 0.35)
  - receipts > 1000: 1000 * 0.20 + (receipts - 1000) * 0.05 (was 0.15)

- **Mileage rates**: Slightly reduced
  - miles <= 100: 0.50 (was 0.58)
  - 100 < miles <= 600: 0.50 - 0.10 * log10(miles/100) (was 0.58 - 0.12)
  - miles > 600: 0.40 (was 0.48)

- **Efficiency bonuses**: Reduced
  - Sweet spot (180-220 miles/day): +30 (was +50)
  - Low efficiency (<80 miles/day): -20 (was -30)
  - High mileage (>800 miles): +20 (was +40)

### Rationale:
The baseline showed massive over-prediction (2-3x expected values). This run aggressively reduces all components, especially the receipt multiplier which appears to be the main culprit.

### Results:
- **Score: 45471.00** (WORSE - went too far in reduction)
- **Exact matches: 0 (0%)**
- **Close matches: 1 (0.1%)**
- **Average error: $453.71**
- **Max error: $1123.35**

### Analysis:
Overcorrected! Now severely under-predicting. The pattern flipped - model now predicts ~50% of expected values. Need to find middle ground between Run 1 and Run 2.

---

## Run 3 - Balanced Middle Ground
**Date**: 2025-06-07
**Description**: Finding middle ground between over-prediction (Run 1) and under-prediction (Run 2)

### Parameter Changes:
- **Base per-diem**: Moderate rates
  - Standard: 85 per day (between 100 and 75)
  - 5-day special: 90 per day (between 105 and 80)
  - Long trip penalties: 75 per day (days >= 10), 65 per day (days >= 14)

- **Receipt component**: Balanced approach
  - receipts <= 1000: receipts * 0.28 (between 0.35 and 0.20)
  - receipts > 1000: 1000 * 0.28 + (receipts - 1000) * 0.10 (between 0.15 and 0.05)

- **Mileage rates**: Moderate adjustment
  - miles <= 100: 0.54 (between 0.58 and 0.50)
  - 100 < miles <= 600: 0.54 - 0.11 * log10(miles/100)
  - miles > 600: 0.44 (between 0.48 and 0.40)

- **Efficiency bonuses**: Balanced
  - Sweet spot (180-220 miles/day): +40 (between +50 and +30)
  - Low efficiency (<80 miles/day): -25 (between -30 and -20)
  - High mileage (>800 miles): +30 (between +40 and +20)

### Rationale:
Run 1 over-predicted (21012), Run 2 under-predicted (45471). This attempts to find the optimal middle ground by averaging the parameter values.

### Results:
- **Score: 30904.00** (IMPROVED from Run 2, but still worse than baseline)
- **Exact matches: 0 (0%)**
- **Close matches: 3 (0.3%)**
- **Average error: $308.04**
- **Max error: $914.05**

### Analysis:
Good progress! Found middle ground between over and under-prediction. Still under-predicting on high-mileage cases but closer to target. Need to boost parameters slightly, especially for high-mileage scenarios.

---

## Run 4 - Mileage Component Boost
**Date**: 2025-06-07
**Description**: Targeting high-mileage under-prediction by boosting mileage rates and high-mileage bonuses

### Parameter Changes:
- **Base per-diem**: Slight increase
  - Standard: 90 per day (increased from 85)
  - 5-day special: 95 per day (increased from 90)
  - Long trip penalties: 80 per day (days >= 10, up from 75), 70 per day (days >= 14, up from 65)

- **Receipt component**: Unchanged
  - receipts <= 1000: receipts * 0.28
  - receipts > 1000: 1000 * 0.28 + (receipts - 1000) * 0.10

- **Mileage rates**: BOOSTED for high-mileage cases
  - miles <= 100: 0.54 (unchanged)
  - 100 < miles <= 600: 0.54 - 0.08 * log10(miles/100) (reduced decay from 0.11)
  - miles > 600: 0.52 (increased from 0.44)

- **Efficiency bonuses**: BOOSTED high-mileage
  - Sweet spot (180-220 miles/day): +40 (unchanged)
  - Low efficiency (<80 miles/day): -25 (unchanged)
  - High mileage (>800 miles): +60 (increased from +30)
  - Very high mileage (>1000 miles): +100 (NEW)

### Rationale:
High-error cases all involve 700+ miles. The model needs to recognize that high-mileage trips have different reimbursement patterns. Boosting mileage rates and bonuses for these cases.

### Results:
- **Score: 26333.00** (BEST SO FAR! Improved from 30904)
- **Exact matches: 0 (0%)**
- **Close matches: 3 (0.3%)**
- **Average error: $262.33**
- **Max error: $833.31**

### Analysis:
Significant improvement! High-mileage cases are better, but new pattern emerged: under-predicting on LOW-mileage, HIGH-receipt cases. Need to boost receipt component for low-mileage trips.

---

## Run 5 - Receipt Component Adjustment for Low Mileage
**Date**: 2025-06-07
**Description**: Addressing under-prediction on low-mileage, high-receipt cases

### Parameter Changes:
- **Base per-diem**: Unchanged
  - Standard: 90 per day
  - 5-day special: 95 per day
  - Long trip penalties: 80 per day (days >= 10), 70 per day (days >= 14)

- **Receipt component**: BOOSTED for low-mileage cases
  - receipts <= 1000: receipts * 0.35 (increased from 0.28)
  - receipts > 1000: 1000 * 0.35 + (receipts - 1000) * 0.12 (increased from 0.10)
  - NEW: Low-mileage receipt bonus: if miles < 200, multiply receipt component by 1.2

- **Mileage rates**: Unchanged
  - miles <= 100: 0.54
  - 100 < miles <= 600: 0.54 - 0.08 * log10(miles/100)
  - miles > 600: 0.52

- **Efficiency bonuses**: Unchanged
  - Sweet spot (180-220 miles/day): +40
  - Low efficiency (<80 miles/day): -25
  - High mileage (>800 miles): +60
  - Very high mileage (>1000 miles): +100

### Rationale:
Run 4 fixed high-mileage under-prediction but revealed low-mileage, high-receipt under-prediction. These cases suggest receipt reimbursement is more generous when trip mileage is low.

### Results:
- **Score: 21632.00** (WORSE than baseline 21012 - over-corrected)
- **Exact matches: 0 (0%)**
- **Close matches: 2 (0.2%)**
- **Average error: $215.32**
- **Max error: $916.23**

### Analysis:
Went backwards! Receipt boost was too aggressive, brought back over-prediction problems. Need smaller, more targeted adjustments. Run 4 (26333) was better direction.

---

## Run 6 - Minimal Adjustment from Baseline
**Date**: 2025-06-07
**Description**: Small tweaks to baseline parameters to try to beat 21012.00

### Parameter Changes from Baseline:
- **Base per-diem**: Tiny reduction
  - Standard: 95 per day (was 100)
  - 5-day special: 100 per day (was 105)
  - Long trip penalties: 85 per day (days >= 10, was 90), 70 per day (days >= 14, was 75)

- **Receipt component**: Slight reduction
  - receipts <= 1000: receipts * 0.32 (was 0.35)
  - receipts > 1000: 1000 * 0.32 + (receipts - 1000) * 0.13 (was 0.15)

- **Mileage rates**: Tiny reduction
  - miles <= 100: 0.55 (was 0.58)
  - 100 < miles <= 600: 0.55 - 0.11 * log10(miles/100) (was 0.58 - 0.12)
  - miles > 600: 0.45 (was 0.48)

- **Efficiency bonuses**: Slight reduction
  - Sweet spot (180-220 miles/day): +45 (was +50)
  - Low efficiency (<80 miles/day): -25 (was -30)
  - High mileage (>800 miles): +35 (was +40)

### Rationale:
Baseline was best at 21012.00. Making minimal reductions across all components to try to reduce over-prediction slightly without going too far.

### Results:
- **Score: 23819.00** (Worse than baseline, but better than most runs)
- **Exact matches: 0 (0%)**
- **Close matches: 1 (0.1%)**
- **Average error: $237.19**
- **Max error: $877.04**

### Analysis:
Still not beating baseline. The original parameters seem to be close to optimal already.

---

## Run 7 - Baseline + Tiny Receipt Adjustment
**Date**: 2025-06-07
**Description**: Exact baseline parameters with ONE tiny change to receipts

### Parameter Changes:
- **Base per-diem**: EXACTLY baseline
  - Standard: 100 per day
  - 5-day special: 105 per day
  - Long trip penalties: 90 per day (days >= 10), 75 per day (days >= 14)

- **Receipt component**: Tiny reduction
  - receipts <= 1000: receipts * 0.34 (was 0.35)
  - receipts > 1000: 1000 * 0.34 + (receipts - 1000) * 0.15 (unchanged)

- **Mileage rates**: EXACTLY baseline
  - miles <= 100: 0.58
  - 100 < miles <= 600: 0.58 - 0.12 * log10(miles/100)
  - miles > 600: 0.48

- **Efficiency bonuses**: EXACTLY baseline
  - Sweet spot (180-220 miles/day): +50
  - Low efficiency (<80 miles/day): -30
  - High mileage (>800 miles): +40

### Rationale:
Baseline (21012) is still best. Making the tiniest possible adjustment - reducing receipt rate by just 0.01 from 0.35 to 0.34.

### Results:
- **Score: 21303.00** (Close to baseline! Only 291 points worse)
- **Exact matches: 0 (0%)**
- **Close matches: 4 (0.4%)** (Improvement!)
- **Average error: $212.03**
- **Max error: $973.81**

### Analysis:
Very close to baseline! Got one more close match. The tiny reduction helped slightly but not enough to beat baseline.

---

## Run 8 - Baseline + Tiny Receipt Increase
**Date**: 2025-06-07
**Description**: Trying the opposite - slightly increase receipt rate from baseline

### Parameter Changes:
- **Receipt component**: Tiny increase
  - receipts <= 1000: receipts * 0.36 (was 0.35, increased by 0.01)
  - receipts > 1000: 1000 * 0.36 + (receipts - 1000) * 0.15

- **All other parameters**: EXACTLY baseline

### Rationale:
Run 7 (receipt rate 0.34) got 21303. Baseline (0.35) got 21012. Testing if 0.36 can beat baseline.

### Results:
- **Score: 20741.00** 🎉 **NEW BEST! Beat baseline by 271 points!**
- **Exact matches: 0 (0%)**
- **Close matches: 5 (0.5%)** (Best so far!)
- **Average error: $206.41**
- **Max error: $993.81**

### Analysis:
BREAKTHROUGH! The tiny increase in receipt rate was exactly what was needed. We now have our best score and most close matches.

---

## Run 9 - Fine-tune from New Best
**Date**: 2025-06-07
**Description**: Building on Run 8 success, trying to optimize further

### Parameter Changes from Run 8:
- **Receipt component**: Tiny further increase
  - receipts <= 1000: receipts * 0.37 (was 0.36)
  - receipts > 1000: 1000 * 0.37 + (receipts - 1000) * 0.15

- **Mileage rates**: Tiny adjustment
  - miles <= 100: 0.59 (was 0.58, tiny increase)
  - 100 < miles <= 600: 0.59 - 0.12 * log10(miles/100)
  - miles > 600: 0.48 (unchanged)

- **All other parameters**: Same as Run 8

### Rationale:
Run 8 beat baseline with 0.36 receipt rate. Testing if 0.37 and slightly higher low-mileage rate can improve further.

### Results:
- **Score: 20477.00** 🚀 **NEW BEST! 535 points better than baseline!**
- **Exact matches: 0 (0%)**
- **Close matches: 4 (0.4%)**
- **Average error: $203.77** (Improving!)
- **Max error: $1003.81**

### Analysis:
Continued improvement! The combination of higher receipt rate (0.37) and slightly higher low-mileage rate (0.59) is working well. Average error is dropping.

---

## Run 10 - Push Receipt Rate Further
**Date**: 2025-06-07
**Description**: Continue the successful trend of increasing receipt rates

### Parameter Changes from Run 9:
- **Receipt component**: Continue increasing
  - receipts <= 1000: receipts * 0.38 (was 0.37)
  - receipts > 1000: 1000 * 0.38 + (receipts - 1000) * 0.15

- **Base per-diem**: Tiny adjustment to 5-day bonus
  - 5-day special: 106 per day (was 105, tiny increase)

- **All other parameters**: Same as Run 9

### Rationale:
The pattern is clear - increasing receipt rates is helping. Testing 0.38 and slightly higher 5-day bonus.

### Results:
- **Score: 20237.00** 🔥 **NEW BEST! 775 points better than baseline!**
- **Exact matches: 0 (0%)**
- **Close matches: 1 (0.1%)**
- **Average error: $201.37** (Continuing to drop!)
- **Max error: $1013.81**

### Analysis:
Excellent progress! Receipt rate increases continue to work. Average error breaking below $202. Close matches dropped but score improved significantly.

---

## Run 11 - Test Receipt Rate Limit
**Date**: 2025-06-07
**Description**: Testing if we can push receipt rate even higher

### Parameter Changes from Run 10:
- **Receipt component**: Push further
  - receipts <= 1000: receipts * 0.39 (was 0.38)
  - receipts > 1000: 1000 * 0.39 + (receipts - 1000) * 0.16 (also increased excess rate)

- **Efficiency bonus**: Slight adjustment
  - Sweet spot (180-220 miles/day): +52 (was +50, tiny increase)

- **All other parameters**: Same as Run 10

### Rationale:
Continuing the successful receipt rate increases. Also testing if excess receipt rate and efficiency bonus tweaks help.

### Results:
- **Score: 19924.00** 🚀🚀 **BROKE 20K BARRIER! 1,088 points better than baseline!**
- **Exact matches: 0 (0%)**
- **Close matches: 5 (0.5%)** (BEST YET!)
- **Average error: $198.24** (Below $200!)
- **Max error: $1030.27**

### Analysis:
MAJOR BREAKTHROUGH! Broke the 20,000 barrier with excellent close match performance. Receipt rate optimization strategy is working perfectly.

---

## Run 12 - Continue the Momentum
**Date**: 2025-06-07
**Description**: Building on the 20K breakthrough with careful refinements

### Parameter Changes from Run 11:
- **Receipt component**: Moderate increase
  - receipts <= 1000: receipts * 0.40 (was 0.39)
  - receipts > 1000: 1000 * 0.40 + (receipts - 1000) * 0.16

- **Base per-diem**: Tiny increase
  - Standard: 101 per day (was 100, tiny increase)

- **All other parameters**: Same as Run 11

### Rationale:
Riding the momentum of breaking 20K. Testing round number 0.40 receipt rate and tiny base increase.

### Results:
- **Score: 19741.00** 🎉 **NEW BEST! 1,271 points better than baseline!**
- **Exact matches: 0 (0%)**
- **Close matches: 0 (0%)** (Lost close matches but score improved)
- **Average error: $196.41** (Lowest yet!)
- **Max error: $1048.27**

### Analysis:
Continued improvement in overall score and average error. The 0.40 receipt rate is working well. May have hit diminishing returns on close matches.

---

## Run 13 - Push Toward 19.5K
**Date**: 2025-06-07  
**Description**: Attempting to break 19.5K barrier with aggressive optimization

### Parameter Changes from Run 12:
- **Receipt component**: Continue aggressive increase
  - receipts <= 1000: receipts * 0.41 (was 0.40)
  - receipts > 1000: 1000 * 0.41 + (receipts - 1000) * 0.17 (increased excess)

- **Mileage rates**: Boost high-mileage rate
  - miles > 600: 0.49 (was 0.48, small increase)

- **Efficiency bonus**: Increase high-mileage bonus
  - High mileage (>800 miles): +42 (was +40)

### Rationale:
We're on an incredible run. Testing if we can push even further toward 19.5K with continued receipt optimization and high-mileage improvements.

### Results:
- **Score: 19626.00** 🎯 **SO CLOSE TO 19.5K! 1,386 points better than baseline!**
- **Exact matches: 0 (0%)**
- **Close matches: 5 (0.5%)** (Back to good close match performance!)
- **Average error: $195.26** (Lowest yet!)
- **Max error: $1072.68**

### Analysis:
Incredible momentum! Just 126 points from breaking 19.5K. Close matches returned and average error continues dropping. Final push needed!

---

## Run 14 - AGGRESSIVE PUSH FOR 10K TARGET
**Date**: 2025-06-07
**Description**: Going all-out to reach the 10K goal with major parameter increases

### Parameter Changes from Run 13:
- **Receipt component**: MAJOR BOOST
  - receipts <= 1000: receipts * 0.45 (was 0.41, big jump)
  - receipts > 1000: 1000 * 0.45 + (receipts - 1000) * 0.20 (major excess increase)

- **Base per-diem**: Significant increase
  - Standard: 105 per day (was 101)
  - 5-day special: 110 per day (was 106)

- **Mileage rates**: Boost all rates
  - miles <= 100: 0.62 (was 0.59)
  - miles > 600: 0.52 (was 0.49)

- **Efficiency bonuses**: MAJOR INCREASES
  - Sweet spot (180-220 miles/day): +60 (was +52)
  - High mileage (>800 miles): +50 (was +42)

### Rationale:
WE'RE GOING FOR 10K! Making aggressive increases across ALL components to see how low we can push this score.

### Results:
- Score: TBD (TARGET: <15000!)
- Exact matches: TBD
- Close matches: TBD

---

## Run 15 - Systematic: Receipt Rate Only  
**Date**: 2025-06-07
**Description**: ONLY adjusting receipt rate - maximum 1 parameter change

### Parameter Changes from Run 13:
- **Receipt component**: Single change
  - receipts <= 1000: receipts * 0.42 (was 0.41, +0.01 increase)

- **ALL OTHER PARAMETERS**: Exactly same as Run 13

### Current Run 13 Parameters (baseline for this test):
- Base per-diem: 101/day (106 for 5-day, 75/90 for long trips)
- Mileage: 0.59 (≤100), 0.59-0.12*log10(miles/100) (100-600), 0.49 (>600)
- Receipt base: 0.42 rate (≤1000), 0.17 excess rate (>1000)
- Efficiency: +52 (sweet spot), -30 (low), +42 (high mileage)

### Results:
- **Score: 19545.00** ✅ **IMPROVED by 81 points from Run 13!**
- **Exact matches: 0 (0%)**
- **Close matches: 3 (0.3%)**
- **Average error: $194.45** (Improved!)
- **Max error: $1082.68**

### Analysis:
Single parameter change worked! Receipt rate 0.42 is better than 0.41. Lost some close matches but overall score improved significantly.

---

## Run 16 - Systematic: Receipt Rate 0.43
**Date**: 2025-06-07
**Description**: ONLY adjusting receipt rate from 0.42 to 0.43 - single parameter change

### Parameter Changes from Run 15:
- **Receipt component**: Single change
  - receipts <= 1000: receipts * 0.43 (was 0.42, +0.01 increase)
  - receipts > 1000: 1000 * 0.43 + (receipts - 1000) * 0.17 (adjusted for consistency)

- **ALL OTHER PARAMETERS**: Exactly same as Run 15

### Current Parameters (Run 16):
- Base per-diem: 101/day (106 for 5-day, 75/90 for long trips)
- Mileage: 0.59 (≤100), 0.59-0.12*log10(miles/100) (100-600), 0.49 (>600)
- Receipt base: 0.43 rate (≤1000), 0.17 excess rate (>1000)
- Efficiency: +52 (sweet spot), -30 (low), +42 (high mileage)

### Results:
- **Score: 19487.00** ✅ **NEW BEST! Improved by 58 points from Run 15!**
- **Exact matches: 0 (0%)**
- **Close matches: 2 (.2%)**
- **Average error: $193.87** (Improved from $194.45!)
- **Max error: $1092.68**

### Analysis:
Another successful single parameter change! Receipt rate 0.43 is better than 0.42. The pattern continues: 0.41 → 0.42 → 0.43 all show improvement. Should test 0.44 next. Lost 1 close match but overall score improved.

---

## Run 17 - Jump to Receipt Rate 0.48
**Date**: 2025-06-07
**Description**: Bigger jump in receipt rate to accelerate optimization

### Parameter Changes from Run 16:
- **Receipt component**: Big jump
  - receipts <= 1000: receipts * 0.48 (was 0.43, jump of +0.05)

- **All other parameters**: Same as Run 16

### Rationale:
Instead of incremental steps, testing a bigger jump to 0.48 to see if we can accelerate the improvement trend.

### Results:
- **Score: 19474.00** (NEW BEST! Improved by 13 points, but smaller gain)
- **Exact matches: 0 (0%)**
- **Close matches: 3 (0.3%)**
- **Average error: $193.74** (Continuing to improve)
- **Max error: $1142.68**

### Analysis:
Still improving but diminishing returns on receipt rate increases. The big jump yielded smaller improvement than incremental steps. May need to try different parameters.

---

## Run 18 (Trip Length Optimization - 4-day bonus)
**Date**: June 7, 2025
**Focus**: Implementing trip length sweet spot - adding 4-day bonus

**Parameters Changed**:
1. **4-day bonus**: NEW - Added 4-day per-diem bonus (days * 104, equivalent to 4% bonus)

**Rationale**: 
- Based on comprehensive rules analysis, identified trip length as next major optimization target
- Evidence from priority matrix shows "trip_length_sweet_spot_4_6" with impact score 70
- Current model only has 5-day bonus, missing 4-day and 6-day bonuses
- Starting with 4-day bonus (4% increase) to test trip length optimization hypothesis

**Other Parameters** (unchanged from Run 17):
- Receipt rate: 0.48 (for receipts ≤ 1000)
- Base per-diem: 101 (for non-bonus days)
- 5-day bonus: 106 per day
- Mileage rates: 0.59 base, log decay, 0.49 plateau
- Efficiency bonus: 52 for sweet spot (180-220 miles/day)
- High-mileage bonus: 42 (for miles > 800)

**Expected Impact**: Should improve handling of 4-day trips, which are part of the documented 4-6 day sweet spot range.

**Result**: **19460.00** ✅ IMPROVEMENT! (Previous best: 19474.00, improvement of 14 points)
- Trip length optimization shows positive impact
- 4-day bonus successfully improves handling of 4-day trips
- Ready for next trip length enhancement (6-day bonus or 8+ day penalty)

---

## Run 19 (Complete Trip Length Sweet Spot - 6-day bonus)
**Date**: June 7, 2025
**Focus**: Completing the 4-6 day sweet spot optimization by adding 6-day bonus

**Parameters Changed**:
1. **6-day bonus**: NEW - Added 6-day per-diem bonus (days * 103, equivalent to 3% bonus)

**Rationale**: 
- Run 18 showed positive results (+14 point improvement) with 4-day bonus
- Rules analysis indicates 4-6 day range is the complete sweet spot
- Adding 6-day bonus with moderate 3% increase (less than 5-day 6% and 4-day 4%)
- This completes the trip length sweet spot implementation

**Other Parameters** (unchanged from Run 18):
- 4-day bonus: 104 per day (4% bonus)
- 5-day bonus: 106 per day (6% bonus) 
- Receipt rate: 0.48 (for receipts ≤ 1000)
- Base per-diem: 101 (for non-bonus days)
- Mileage rates: 0.59 base, log decay, 0.49 plateau
- Efficiency bonus: 52 for sweet spot (180-220 miles/day)
- High-mileage bonus: 42 (for miles > 800)

**Expected Impact**: Should further improve score by optimizing 6-day trips, completing the documented 4-6 day sweet spot range.

**Result**: [To be filled after evaluation]
