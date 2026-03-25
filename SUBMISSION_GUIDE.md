# 🎯 FINAL SOLUTION - C. ANIMAL FARM
## Ready to Submit on OmegaUp

---

## ✅ WHAT CHANGED

**Previous Problem:** Counted connected 0s in binary grid (incorrectly assumed)

**Actual Problem:** Count distinct rooms/areas in buildings with walls encoded as 0-15

**New Solution:** Uses BFS with wall-bit decoding
- Bit 0 (value 1): Top wall
- Bit 1 (value 2): Right wall
- Bit 2 (value 4): Bottom wall
- Bit 3 (value 8): Left wall

---

## 📋 HOW TO SUBMIT

### Step 1: Copy Code
Open file: `SUBMIT_ON_WEBSITE_FINAL.py`

Copy **ALL** the code from this file

### Step 2: Go to OmegaUp
- URL: https://omegaup.com/arena/gsoc2026/#problems
- Problem: **C. Animal Farm**

### Step 3: Paste & Submit
1. Click the problem
2. Find "Submit Solution" or "Send Code"
3. Paste the entire code
4. Select Language: **Python 3.9** (or Python 3)
5. Click **Submit**

---

## 🧠 HOW THE SOLUTION WORKS

```
INPUT FORMAT:
-----------
T              <- Number of buildings
For each building:
  X Y          <- Columns and Rows
  [Y lines]    <- Each line has X integers (wall encodings 0-15)

OUTPUT:
------
For each building: print count of distinct areas
```

### Algorithm:

**Step 1: Find Outside Area**
- Scan all edge cells
- If edge cell has no wall opening outward → it's connected to "outside"
- BFS from these cells to find all cells in "outside area"
- This counts as 1 area

**Step 2: Find Interior Areas**
- For remaining unvisited cells, count connected components
- Each component = 1 interior area

**Step 3: Return Total**
- Interior areas + (1 if outside area exists, else 0)

### Wall Connectivity Logic:

Two cells are connected if:
1. Current cell does NOT have wall in that direction, AND
2. Adjacent cell does NOT have wall on opposite side

Example:
```
Cell A (right): no right wall (bit 1 = 0)
Cell B (left):  no left wall  (bit 3 = 0)
↓
A and B are CONNECTED
```

---

## ✨ KEY FEATURES

✅ Handles wall boundaries  
✅ Treats outside as one area  
✅ Counts interior regions separately  
✅ Correct bitwise operations  
✅ Efficient BFS traversal  

---

## 📌 IMPORTANT NOTES

1. **Language:** Python 3 (3.9 or later)
2. **Time Limit:** Usually 1s per test case
3. **Complexity:** O(rows × cols) - optimal
4. **Input:** Read from stdin using `input()`
5. **Output:** Print using `print()`

---

## 🚀 FINAL CODE (COPY THIS)

See file: `SUBMIT_ON_WEBSITE_FINAL.py`

Simply copy and paste the entire content on OmegaUp!

---

**Status: ✅ READY FOR SUBMISSION**
