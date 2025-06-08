# Etch GCD-Driven 7-Hour Reverse Engineering Roadmap

## Goal
- Derive `f(inputs…) → output` using layered refinement of logic, regression, and historical rule archaeology.

## Constraint
- Complete in **7 hours**, with targeted analysis per phase.

---


### Hour 1 – Setup, Data Load, Structure & Null Patterning
- [x] **Initial Setup**:
  - Copy `run.sh.template` to `run.sh`
  - Configure `run.sh` to accept exactly 3 parameters: `trip_duration_days`, `miles_traveled`, `total_receipts_amount`
  - Ensure output is a single number (rounded to 2 decimal places)
  - Test script with sample input (e.g., `./run.sh 5 250 150.75`)

  - [x] **Objective**: Ensure reliable ingestion and detect any null logic.
  - Load `public_cases.json` into `df`
  - `.describe()` + null/NaN heatmap
  - Correlation heatmap (Pearson + Spearman)
  - Print distinct values and ranges per input
  - Interaction check: `miles × days`, `receipts ÷ miles`, etc.
  - Legacy null logic check: Any pattern to missing fields?

#### 📌 Output:
- [x] `run.sh` script in place and working with correct input/output format
- [x] Distribution plots per field
- [x] Correlation matrix (including interactions)
- [x] Summary table of field ranges & null logic

---

### Hour 2 – Pattern Recognition & Breakpoint Discovery
- [x] **Objective**: Spot likely thresholds, tiers, and legacy structure.
  - Plot: `output` vs `input` for each dimension (line + scatter)
  - Quantize inputs and analyze `mean(output)` by bin
  - Identify potential thresholds:
    - `miles = 100, 200, 300`
    - `days = 1, 3, 7, 14`
  - Cross-check outputs at edge bins

#### 📌 Output:
- [x] Annotated graph of likely piecewise cutoffs
- [x] Report: Inputs that exhibit nonlinear or discontinuous shifts

---

### Hour 3 – Rule Extraction & Policy Synthesis

#### Objective
Parse written policy documents to extract reimbursement logic as formalized rules. Rank and timestamp each rule. Build a canonical view of reimbursement tiers, caps, and conditions to inform piecewise model design.

---

#### Steps Completed

##### Step 1 – Parse Policy Documents (Full-text Ingest)
- **Input**: `PRD.md`, `INTERVIEWS.md`, any supplemental memos
- **Action**:
  - Read paragraph by paragraph; detect:
    - Explicit rules (e.g., "Trips under 100 miles are reimbursed at a lower rate")
    - Implicit logic (e.g., "multi-day travel requires a bonus approval")
    - Edge cases (e.g., "before 2010, no receipt cap was enforced")
  - Annotate rule candidates with:
    - Source doc + line number (if available)
    - Tone: policy vs anecdote
    - Time scope: current vs legacy

##### Step 2 – Translate to Canonical Mini-DSL
- **Format**:
  ```dsl
  if miles < 100 → rate = reduced_local
  if receipts > 1800 → cap = 1800
  if days >= 7 → tier = weekly_bonus
  if year < 2010 → cap = none
  ```
- **Action**:
  - Ensure each rule is machine-computable (will be passed into later modeling layers)
  - Include conditionals, thresholds, and outcomes

##### Step 3 – Prioritize with Rule Confidence Matrix
- **Matrix**:
  | Rule | Priority | Confidence | Recency | Source |
  |------|----------|------------|---------|--------|
  | if miles < 100 → rate = reduced_local | High | High | Current | PRD.md |
  | if receipts > 1800 → cap = 1800 | High | High | Post-2010 | INTERVIEWS.md |
  | if days > 7 → tier = weekly_bonus | Medium | Medium | 2015 | PRD.md |
  | if year < 2010 → cap = none | Low | Medium | Legacy | INTERVIEWS.md |

- **Legend**:
  - **Priority**: Explanatory power on `expected_output` (from Hour 2)
  - **Confidence**: Clarity and consistency of doc source
  - **Recency**: Approximate time relevance of policy
  - **Source**: Which document and where

##### Step 4 – Build Rule Timeline
- **Summary**:

  **📆 Reimbursement Policy Timeline:**
  - 🕰️ **Pre-2010**:
    - No cap on receipts
    - Flat mileage rate regardless of trip length
  - 📆 **2010–2014**:
    - Receipt cap introduced at $1800
    - Multi-day tiering begins (bonuses after 7 days)
  - ✅ **2015–Present**:
    - Confirmed per-mile and per-diem tier thresholds
    - Strict enforcement of $1800 cap

---

#### Deliverables
- [x] `rules.dsl` — all rules in canonical form
- [x] `priority_matrix.csv` — for model conditioning in Hour 5
- [x] `rule_timeline.md` — policy shifts over time
- [x] `doc_extracts.md` — raw quote references per rule (optional)

---

### Hour 4 – Hypothesis Sprint 1: Linear & Simple Models
- [ ] **Objective**: Create baseline model and surface what’s missing.
  - Implement:
    ```
    y = a*miles + b*days + c*receipts + d
    ```
  - Print: residuals, top 10 worst mismatches
  - Output `abs(pred - actual)` alongside inputs
  - Introduce:
    - Polynomial terms (`miles²`, `days²`, etc.)
    - Log-transform (`log(miles + 1)`, etc.)

#### 📌 Output:
- [X] Initial RMSE, MAE
- [X] Best polynomial/log model summary
- [X] Residual table with flagged anomalies

---

### Hour 5 – Hypothesis Sprint 2: Tiered & Piecewise
- [x] **Objective**: Add business rules + conditional logic.
  - Apply known rules from Hour 3:
    - Per-mile tiers
    - Flat-rate lodging/meals
    - Receipt caps
  - Test multiplicative terms:
    ```
    y = (base_rate × miles) + (allowance × days × meals_multiplier)
    ```

#### 📌 Output:
- [x] Updated model with conditional branches
- [x] Accuracy comparison vs Hour 4
- [x] Annotated formula (both code & human form)

---

### Hour 6 – Precision Bugs & Legacy Quirks
- [x] **Objective**: Handle edge cases, artifacts, and old-system behavior.
  - Review top residuals again:
    - Is it off by 0.01–0.05 → rounding?
    - Is it always $4.31 off → tax logic?
  - Test for:
    - Floating-point precision failures
    - Integer floor/ceil bugs
    - Currency conversion ghosts (e.g., USD↔CAD)
    - Tax rules embedded as constants
    - "Business day" vs "calendar day" logic differences
    - Leap year handling (if dates involved)

#### 📌 Output:
- [x] Patch set of fix functions (e.g., `applyRounding`, `adjustForTax`)
- [x] Cases now explained by patch
- [x] Final model composite: `model + fixSet = final prediction`

---

### Hour 7 – Validation, Eval & Write-up
- [x] **Objective**: Run final test, submit, and document.
  - Run `eval.sh` — confirm high match rate
  - Backtrack remaining mismatches (should be <1%)
  - Write:
    - Canonical formula (`f(inputs…)`)
    - Plain-English explanation for humans
    - List of assumptions, exceptions, unresolved artifacts
    - Generate confidence intervals for remaining errors
    - Document which rules are "certain" vs "inferred"

#### 📌 Output:
- [x] Final implementation file
- [ ] One-pager summary: “How This Model Works”
- [ ] Bonus: Future TODOs (e.g., time-dependent models, rule versioning)

---

### 🔁 Recap GCD Principle
All of this serves one invariant:

`f(inputs) = output`

Every artifact—data, rule, code—is just an input into shaping that function.