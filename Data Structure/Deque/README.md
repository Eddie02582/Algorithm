# 🚦 Deque（Double-Ended Queue / 雙端佇列）

`deque` 是 Python `collections` 模組提供的一種 **雙端資料結構**，支援：

- 頭部插入 (`appendleft`)
- 尾部插入 (`append`)
- 頭部彈出 (`popleft`)
- 尾部彈出 (`pop`)

並且 **所有操作平均時間複雜度為 O(1)**，比 `list.insert(0, x)` 或 `pop(0)` 更高效。

---

## 1️⃣ 為什麼需要 Deque？

普通 Python List：

| 操作 | Big-O | 說明 |
|------|-------|------|
| `append()` | O(1) | 尾端添加快 |
| `pop()` | O(1) | 尾端移除快 |
| `insert(0, x)` | ❌ O(n) | 頭部插入需要搬移所有元素 |
| `pop(0)` | ❌ O(n) | 頭部移除需要搬移所有元素 |

Deque 改善了這個問題：

👉 **首尾增刪均為 O(1)**。

---

## 2️⃣ Python Deque 基本語法

```python
from collections import deque

dq = deque()

dq.append(1)       # [1]
dq.appendleft(0)   # [0,1]
dq.append(2)       # [0,1,2]

dq.pop()           # -> 2, remaining [0,1]
dq.popleft()       # -> 0, remaining [1]
```

### 其他常用操作：

```python
dq.extend([3,4])         # [1,3,4]
dq.extendleft([-1,-2])   # [-2,-1,1,3,4]

dq.rotate(1)  # 向右旋轉 → [4,-2,-1,1,3]
dq.rotate(-1) # 向左旋轉 → [-2,-1,1,3,4]
```

---

## 3️⃣ Deque 底層結構

Deque 底層是 **雙向鏈結區塊緩衝（Linked Block Memory）**，不是 array，也不是單純 linked list。

```
 <--block--> <--block--> <--block-->
[ 0 | 1 | 2 ]-[ 3 | 4 ]-[ 5 | 6 | 7 ]
 ^head                               ^tail
```

✨ 好處：

- 支援 **O(1) 首尾插入**（不像 list 需要搬移大量元素）
- 記憶體連續性比 linked list 好 → cache-friendly

⚠️ 注意：

- **不支援 O(1) 隨機存取**（不像 list 用 index）

---

## 4️⃣ 使用場景與思考模式

Deque 適合：

| 場景 | 例子 |
|------|------|
| Queue（佇列） | BFS |
| Sliding Window（滑動視窗） | 最大/最小視窗問題 |
| Palindrome 檢查 | 前後比較 |
| Rate Limit / Task Scheduling | 模擬先進先出事件 |
| Circular buffer（循環緩衝區） | rotate |

---

## 5️⃣ LeetCode 常見題目

| 題號 | 題名 | 難度 | 為什麼用 deque |
|------|------|------|----------------|
| 239 | Sliding Window Maximum | 🔥 Hard | 維持單調隊列 |
| 862 | Shortest Subarray With Sum >= K | Hard | 用 monotonic deque |
| 649 | Dota2 Senate | Medium | 模擬 queue |
| 933 | Number of Recent Calls | Easy | 滑動時間窗口 |
| 207 | Course Schedule (BFS 版本) | Medium | BFS queue |
| 752 | Open the Lock | Medium | BFS |
| 994 | Rotting Oranges | Medium | BFS |

---

## 6️⃣ 經典範例：Sliding Window Maximum（LC 239）

利用 **單調遞減 Deque** 儲存滑動窗口最大值。

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    res = []

    for i, num in enumerate(nums):
        
        # 移除左邊界已滑出的值
        if dq and dq[0] == i - k:
            dq.popleft()

        # 維持單調遞減（移除小於目前元素的）
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # 當形成第 k 個元素後開始加入答案
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# Output: [3,3,5,5,6,7]
```

---

## 7️⃣ BFS Queue（典型 Deque 用法）

```python
from collections import deque

def bfs(tree, start):
    dq = deque([start])
    visited = set([start])
    
    while dq:
        node = dq.popleft()
        print(node)
        
        for nxt in tree[node]:
            if nxt not in visited:
                visited.add(nxt)
                dq.append(nxt)
```

---

## 8️⃣ 使用建議與最佳實踐

✔ 使用 deque 而不是 list 當作 queue  
✔ 遇到滑動視窗最大/最小 → 思考「單調 deque」  
✔ BFS → 必備 deque  
✔ 不需要 index 隨機存取時，deque 效率最佳  

---

## 📌 總結

| 結構 | O(1) 頭部插入 | O(1) 頭部刪除 | O(1) 尾部插入 | O(1) 尾部刪除 |
|------|---------------|---------------|---------------|---------------|
| List | ❌ | ❌ | ✅ | ✅ |
| Deque | ✅ | ✅ | ✅ | ✅ |
| Linked List | ❌ Python 無內建 | ❌ Python 無內建 | ❌ Python 無內建 | ❌ Python 無內建 |

👉 **想用 queue / sliding window / BFS → 首選 deque**

---


