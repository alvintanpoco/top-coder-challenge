────────────────────────────────────────────────────────────────
1) CORE PIECEWISE POLICY  (High Confidence: Lisa / Jennifer)
────────────────────────────────────────────────────────────────

# ─── BASE PER-DIEM ─────────────────────────────────────────────
if days ≤ 4          → per_diem = 100  
if days == 5         → per_diem = 100 × 1.05   # five-day bonus  
if 6 ≤ days ≤ 13     → per_diem = 100  
if days ≥ 14         → per_diem = 85          # long-trip taper  

# ─── MILEAGE TIERS ─────────────────────────────────────────────
if miles ≤ 100         → rate = 0.58  
if 100 < miles ≤ 600   → rate = 0.58 − 0.12·log₁₀(miles/100)  
if miles > 600         → rate = 0.36        # plateau  

────────────────────────────────────────────────────────────────
2) EFFICIENCY & SPEND ADJUSTMENTS  (Medium Confidence: Kevin)
────────────────────────────────────────────────────────────────

# ─── EFFICIENCY BONUS ─────────────────────────────────────────
let r = miles / days  
if 180 ≤ r ≤ 220       → adjust += 0.07·base_reimb  
if r < 80              → adjust  = −0.05·base_reimb  
if r > 300             → adjust  = −0.04·base_reimb  

# ─── RECEIPT-SPEND CURVE ──────────────────────────────────────
if receipts < 200         → adjust += −0.05·base_reimb  
if 200 ≤ receipts ≤ 1800  → adjust += +0.06·base_reimb  
if receipts > 1800        → receipts = 1800           # hard cap  

────────────────────────────────────────────────────────────────
3) INTERACTION COMBOS & QUIRKS  (Investigative / Flag Only)
────────────────────────────────────────────────────────────────

# ─── JACKPOT & PENALTY ───────────────────────────────────────
if days==5 and 180≤r≤220 and receipts/days≤100  
                         → adjust += 0.12·base_reimb   # Kevin jackpot  
if days≥8 and receipts/days≥120  
                         → adjust += −0.15·base_reimb  # Kevin vacation penalty  

# ─── ROUNDING BUG ────────────────────────────────────────────
if receipts % 1 ∈ {0.49,0.99}  
                         → flag double-round-quirk    # Lisa  

