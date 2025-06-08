# Complete Rules Analysis for Model Optimization

## Summary of Rules Folder Analysis

### High-Priority Rules (Tier 1) - Already Implemented or Optimized:
1. **Base per-diem ($100)** - ✅ Core foundation
2. **Mileage tiered system** - ✅ Implemented with log decay after 100 miles
3. **Efficiency sweet spot (180-220)** - ✅ Well-optimized
4. **Small receipt penalty** - ✅ Penalty for receipts < 200
5. **Five-day bonus** - ✅ Implemented (5% bonus)
6. **Receipt sweet spot (600-800)** - ✅ Recently optimized to 0.48 rate

### Next Major Optimization Targets (Tier 2):

#### 1. **Trip Length Sweet Spot (4-6 days)** - HIGH PRIORITY
- **Evidence**: Multiple sources confirm 4-6 day trips have optimal treatment
- **Current Implementation**: Only 5-day bonus exists, no 4-day or 6-day optimization
- **Opportunity**: Add specific bonuses for 4-day and 6-day trips
- **Impact Score**: 70 (Tier 2)

#### 2. **Long Trip Penalty (≥8 days)** - HIGH PRIORITY
- **Evidence**: "Vacation penalty" for trips ≥8 days with high daily spend
- **Current Implementation**: Only basic per-diem taper at 14+ days
- **Opportunity**: Implement penalty for 8+ day trips with receipts/day ≥ 120
- **Impact Score**: 72 (Tier 2)

#### 3. **Spending Per Day Thresholds** - MEDIUM PRIORITY
- **Evidence**: Detailed spend-per-day analysis shows thresholds matter
- **Current Implementation**: Basic receipt amount bonus/penalty
- **Opportunity**: Implement daily spending rate optimizations
- **Impact Score**: 78 (Tier 2)

#### 4. **Inverse Efficiency Penalties** - MEDIUM PRIORITY
- **Evidence**: Low mileage + high spend penalty, High mileage + low spend bonus
- **Current Implementation**: Basic efficiency ratios only
- **Opportunity**: Add specific penalties/bonuses for inverse efficiency patterns
- **Impact Score**: 68-70 (Tier 2)

### Structural Insights from DSL:

#### Core Piecewise Policy (rules.dsl):
```
Per-diem: 100 (≤4 days), 105 (5 days), 100 (6-13 days), 85 (≥14 days)
Mileage: 0.58 (≤100), logarithmic decay (100-600), 0.36 plateau (>600)
```

#### Efficiency & Spend Adjustments:
```
Efficiency bonus: +7% for 180-220 miles/day ratio
Low efficiency penalty: -5% for <80 miles/day
High efficiency penalty: -4% for >300 miles/day
Receipt bonus: +6% for 200-1800 receipts, -5% for <200
```

#### Interaction Combos:
```
Jackpot combo: 5 days + 180-220 efficiency + low daily spend → +12%
Vacation penalty: ≥8 days + ≥120 daily spend → -15%
```

### Timeline Evolution:
- **Pre-2010**: Simple flat rates
- **2010-2014**: Receipt caps and mileage curves introduced
- **2015-2018**: 5-day bonus formalized, long-trip taper
- **2019-Present**: Complex combos, timing multipliers, penalties

## Recommended Next Optimization Target:

### **Trip Length Sweet Spot Enhancement**

**Rationale:**
1. **High Impact**: Score 70 in priority matrix
2. **Clear Evidence**: Multiple sources confirm 4-6 day optimization
3. **Current Gap**: Only 5-day bonus exists, missing 4-day and 6-day bonuses
4. **Low Risk**: Well-documented pattern, unlikely to cause negative effects

**Proposed Changes:**
1. Add 4-day trip bonus (similar to 5-day)
2. Add 6-day trip bonus (slightly smaller than 5-day)
3. Implement vacation penalty for 8+ day trips with high daily spending

**Implementation Strategy:**
- Modify per-diem calculation to include 4-day and 6-day bonuses
- Add vacation penalty logic for long trips with high daily spend
- Test incrementally with 1-2 parameter changes per run

This represents the next logical optimization step based on the comprehensive rules analysis.
