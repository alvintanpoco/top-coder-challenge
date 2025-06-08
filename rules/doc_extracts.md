# Employee Discovery Interviews Extracts

This document captures key insights and theories from employee interviews conducted in March–April 2025 regarding the company's expense reimbursement system.

---

## Marcus (Regional Sales Director)

**Date:** March 15, 2025 | **Duration:** 32 minutes

* **Unpredictability:** Identical trips yield different reimbursements; variability by calendar date suggests monthly quotas or unexplained timing effects.
* **Trip Length Effects:** Believes 5–6 day trips have a sweet spot, but 8-day trips with high hustle yield disproportionately high reimbursements; longer trips may face tapering inconsistencies.
* **Effort/Hustle Factor:** Suspects system rewards "effort" (e.g., high mileage + full-day meetings).
* **Mileage Variance:** Short drives follow standard rates; longer drives see nonlinear drop-offs (600 miles yielded less than linear, while others claim higher rates at 800 miles).
* **Receipt Caps & Penalties:** High weekly receipts sometimes lead to lower reimbursements, implying diminishing returns or hidden caps.
* **Historical Bias & Adaptation:** Perceives system "remembers" user history—big expense patterns trigger stinginess, modest patterns restore generosity.
* **Department & Timing Theories:** Anecdotes about department-specific rules and day-of-week submission effects (e.g., Tuesdays favored by some).
* **Miscellaneous Theories:** "Magic number" amounts, rounding quirks, and randomization theories abound but lack systematic validation.

---

## Lisa (Senior Staff Accountant)

**Date:** March 22, 2025 | **Duration:** 41 minutes

* **Base Per Diem:** \$100/day for trips ≤4 days; +5% bonus on exactly 5-day trips; \$100/day for 6–13 days; \$85/day for ≥14 days.
* **Mileage Tiers:**

  * ≤100 miles → \$0.58/mi
  * 100–600 miles → \$0.58 − 0.12·log₁₀(miles/100)
  * > 600 miles → \$0.36/mi
* **Receipt Spend Curve:**

  * <\$50 → −10% penalty on base reimbursement
  * \$50–\$600 → +8% bonus
  * \$600–\$1800 → +3% bonus
  * > \$1800 → cap at \$1800
* **Temporal & Random Layers:** Weekday bonuses/penalties, moon-phase bonus (+1% on new moon), historical grandfather rules (pre-2010 no cap), new-hire penalty.
* **Rounding Quirk:** Receipts ending in .49 or .99 trigger double-round-up, boosting reimbursements.
* **System Evolution:** Complexity from layered rules and ad hoc patches; patterns exist but are inconsistent over time.

---

## Dave (Regional Marketing Manager)

**Date:** March 29, 2025 | **Duration:** 28 minutes

* **City & Timing Variance:** Similar trips in different cities or months yield different outcomes; no clear seasonal or location-based logic.
* **Mileage & Receipts Advice:** Small receipts can reduce total reimbursement; sometimes better to omit minor expenses.
* **"Magic" Combos:** Anecdotal jackpot combinations (day count, miles, spend) with no reproducible pattern.
* **User Experience:** System feels arbitrary; recommends keeping expectations low and submitting promptly.

---

## Jennifer (HR Business Partner)

**Date:** April 8, 2025 | **Duration:** 35 minutes

* **Fairness & Perception:** Inconsistent reimbursements fuel complaints and distrust, even when underlying factors differ subtly.
* **New vs. Veteran Employees:** New hires see lower reimbursements early; experienced travelers leverage strategies to optimize claims.
* **Optimal Trip Length:** Perceived sweet spot at 4–6 days; longer or shorter trips often disappoint.
* **Departmental Differences:** Sales travels outperform other departments, possibly due to higher volume and strategic submissions.
* **HR Priorities:** Desires transparency and consistency; current opacity creates communication challenges.

---

## Kevin (Senior Procurement Analyst)

**Date:** April 12, 2025 | **Duration:** 48 minutes

* **Data-Driven Patterns:** Efficiency (miles/day) and spend/day thresholds are key predictors; interactive effects dominate.
* **Efficiency Bonus:** 180–220 mi/day → +7% bonus; <80 mi/day → −5% penalty; >300 mi/day → −4% penalty.
* **Spend Ranges:** <\$75/day (short trips), ≤\$120/day (4–6 days), <\$90/day (long trips) for optimal treatment.
* **Timing Effects:** Tuesday/Thursday submissions → +2% bonus; Friday → −3% penalty; end-of-quarter and lunar-cycle correlations (\~4% new moon bonus).
* **Calculation Paths:** At least six distinct rule sets based on trip/mileage/spend clustering (identified via k-means).
* **Interaction Combos:**

  * 5-day trips + 180–220 mi/day + ≤\$100/day spend → +12% jackpot bonus
  * ≥8-day trips + ≥\$120/day spend → −15% vacation penalty
* **Adaptive & Randomized Logic:** System may profile users over time; includes noise to deter gaming, but controllable factors still yield a \~30% reimbursement improvement if optimized.

---

*End of Extracts*
