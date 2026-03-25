# HOW TO SUBMIT CODE ON OMEGAUP (WEBSITE)

## 📋 STEP-BY-STEP GUIDE

### Step 1: Copy the Code
Use the code from `SUBMIT_TO_WEBSITE.py` - it's ready to paste!

### Step 2: Go to OmegaUp
- Open: https://omegaup.com/ (or your online judge website)
- Login to your account
- Find the problem: "C. Animal Farm"

### Step 3: Paste Code
1. Click on the problem
2. Click "Submit Answer" or "Send Solution"
3. Paste the entire code from `SUBMIT_TO_WEBSITE.py`
4. Select language: **Python 3**

### Step 4: Click Submit/Send
- Click the Submit button
- Wait for results

---

## ✅ WHAT THE CODE DOES

**Input Format:**
```
3
0 0 1
0 1 0
1 0 0
```

**Output:**
```
2
```

---

## 📝 HOW THE INPUT/OUTPUT WORKS

### Reading Input:
```python
n = int(input())          # Read number of rows (3)
grid = []

for i in range(n):
    row = list(map(int, input().split()))  # Read each row
    grid.append(row)
```

### Output Result:
```python
print(room_count)         # Print the answer
```

---

## 🎯 TESTING BEFORE SUBMITTING

Before you submit to website, test locally:

```bash
# Create test input file
cat > input.txt << EOF
3
0 0 1
0 1 0
1 0 0
EOF

# Run the code
python SUBMIT_TO_WEBSITE.py < input.txt
```

Expected output: `2`

---

## 📌 COMMON MISTAKES TO AVOID

❌ **Don't do this:**
```python
# DON'T add comments or extra prints
print("The answer is:")    # ❌ WRONG!
print(room_count)          # ❌ WRONG!
```

✅ **Do this:**
```python
# DO only output the answer
print(room_count)          # ✅ CORRECT!
```

---

## 💡 IF IT DOESN'T WORK

### Problem 1: "Wrong Answer" (WA)
- Check if grid format is correct
- Verify input parsing
- Test with the example cases

### Problem 2: "Time Limit Exceeded" (TLE)
- Our algorithm is O(n×m) which is optimal
- Should work fine for large inputs

### Problem 3: "Runtime Error" (RE)
- Check for invalid array access
- Ensure grid dimensions are correct
- Verify input parsing

---

## 🚀 QUICK REFERENCE

| Aspect | Details |
|--------|---------|
| **Language** | Python 3 |
| **Time Limit** | Usually 1-2 seconds |
| **Memory Limit** | Usually 256 MB |
| **Input** | Read from stdin using `input()` |
| **Output** | Print result using `print()` |
| **Complexity** | O(rows × cols) - Optimal |

---

## 📄 FINAL CODE (COPY THIS EXACTLY)

```python
from collections import deque

def solve():
    n = int(input())
    grid = []
    
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False] * cols for _ in range(rows)]
    room_count = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_valid(r, c):
        return (0 <= r < rows and 
                0 <= c < cols and 
                not visited[r][c] and 
                grid[r][c] == 0)
    
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            for dr, dc in directions:
                next_r = curr_r + dr
                next_c = curr_c + dc
                
                if is_valid(next_r, next_c):
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                bfs(r, c)
                room_count += 1
    
    print(room_count)

if __name__ == "__main__":
    solve()
```

---

## ✨ YOU'RE READY!

Just:
1. ✅ Copy the code
2. ✅ Paste on website
3. ✅ Select Python 3
4. ✅ Click Submit
5. ✅ Get AC (Accepted) ✓

Good luck! 🎉
