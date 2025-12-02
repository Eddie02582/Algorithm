# 📌 Sliding Window（滑動視窗）

---

## 1️⃣ 定義

Sliding Window 是一種在 **線性資料結構（陣列 / 字串）** 上進行 **連續區間分析的技巧**：

- 維護一個固定長度或變長的窗口
- 對窗口內元素做統計、求和、最大最小、條件判斷等
- 隨著迭代將窗口往右移動

核心思想：

- **固定窗口大小** → 窗口內元素統計
- **可變窗口大小** → 窗口滿足條件就收縮或擴張

---

## 2️⃣ 適用場景

| 類型 | 說明 |
|------|------|
| 固定長度區間統計 | 最大值、最小值、總和、平均值 |
| 可變長度區間 | 滿足條件的最短子串 / 子陣列 |
| 單調隊列結合 Sliding Window | 找最大值/最小值、K 大數、最小子陣列 |
| 字串 / 陣列處理 | 包含 / 不包含條件、字符計數 |

---

## 3️⃣ 常見操作模式

1. **固定長度窗口**

```python
# 固定窗口長度 k 的滑動和範例
nums = [1,3,-1,-3,5,3,6,7]
k = 3
window_sum = sum(nums[:k])
res = [window_sum]

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i-k]
    res.append(window_sum)
```

---

2. **可變長度窗口（條件收縮 / 擴張）**

```python
# 找最短子串或子陣列，使 sum >= target
def minSubArrayLen(target, nums):
    left = 0
    sum_window = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        sum_window += nums[right]
        while sum_window >= target:
            min_len = min(min_len, right - left + 1)
            sum_window -= nums[left]
            left += 1
    
    return 0 if min_len == float('inf') else min_len
```

---

3. **單調隊列 + Sliding Window（找區間最大值）**

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    res = []

    for i, num in enumerate(nums):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

---

## 4️⃣ 時間複雜度分析

| 類型 | 複雜度 |
|------|--------|
| 固定窗口累加 / 統計 | O(n) |
| 可變窗口（條件收縮） | O(n) |
| 單調隊列維護 | O(n)（每個元素進出隊列至多一次） |

---

## 5️⃣ Python LeetCode 題型模板

### 5.1 固定長度窗口

```python
def fixed_window(nums, k):
    # 初始化窗口統計
    window = sum(nums[:k])
    res = [window]
    
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        res.append(window)
    return res
```

### 5.2 可變長度窗口

```python
def variable_window(nums, target):
    left = 0
    sum_window = 0
    min_len = float('inf')

    for right, val in enumerate(nums):
        sum_window += val
        while sum_window >= target:
            min_len = min(min_len, right - left + 1)
            sum_window -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
```

### 5.3 單調隊列模板（滑動最大 / 最小）

```python
from collections import deque

def monotonic_window(nums, k, mode="max"):
    dq = deque()
    res = []

    for i, val in enumerate(nums):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and ((mode=="max" and nums[dq[-1]] < val) or
                      (mode=="min" and nums[dq[-1]] > val)):
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

---

## 6️⃣ 常見 LeetCode 題目

| 題號 | 題名 | 類型 |
|------|------|------|
| 209 | Minimum Size Subarray Sum | 可變長度窗口 |
| 76  | Minimum Window Substring | 可變長度窗口 |
| 3   | Longest Substring Without Repeating Characters | 可變長度窗口 + 字典 |
| 239 | Sliding Window Maximum | 單調隊列 |
| 862 | Shortest Subarray with Sum ≥ K | 單調隊列 |
| 904 | Fruit Into Baskets | 固定/可變長度窗口 |
| 1004| Max Consecutive Ones III | 可變長度窗口 |

---

## 7️⃣ 小結

- 固定長度窗口 → 滑動累加 / 統計 → O(n)
- 可變長度窗口 → 條件收縮/擴張 → O(n)
- 單調隊列 → 求窗口最大值/最小值 → O(n)
- Sliding Window + Dictionary → 最長無重複子串 / 條件限制
- 幾乎所有線性陣列、字串子區間問題都可以思考此技巧

---
