# 📦 Heap (堆)

Heap 是一種特殊的二元樹結構，滿足：

- **最大堆 Max-Heap**：父節點 ≥ 子節點  
- **最小堆 Min-Heap**：父節點 ≤ 子節點  

用途：

- 優先隊列
- 動態取得最大/最小值
- 排序（Heap Sort）
- Top-K 問題
- 合併排序

---

## Heap 特點

- 完全二元樹：除了最後一層，其它層都是滿的，最後一層靠左填充
- 插入/刪除最大值（或最小值）時間複雜度 O(log n)
- Python 提供 `heapq` 模組，只支援最小堆

---

## Python heapq 範例

```python
import heapq

# 建立最小堆
nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)  # O(n)
print(nums)  # [1,2,8,5,3] (內部結構保持最小堆)

# 插入元素
heapq.heappush(nums, 0)
print(nums)  # [0,...]

# 取出最小元素
min_val = heapq.heappop(nums)
print(min_val)  # 0

# 取最小前 k 個元素
top3 = heapq.nsmallest(3, nums)
print(top3)

# 取最大前 k 個元素
top3_max = heapq.nlargest(3, nums)
print(top3_max)
```

---

## Max-Heap 實現

Python heapq 只支援最小堆，可透過 **取負數** 或自訂類別：

```python
import heapq

nums = [5, 3, 8, 1, 2]
max_heap = [-num for num in nums]
heapq.heapify(max_heap)

# 取最大值
max_val = -heapq.heappop(max_heap)
print(max_val)  # 8

# 插入最大值
heapq.heappush(max_heap, -10)
```

---

## Heap 應用範例

### 1. Top K 最大元素

```python
def topK(nums, k):
    return heapq.nlargest(k, nums)

print(topK([3,2,1,5,6,4], 2))  # [6,5]
```

### 2. 合併 K 個排序列表

```python
import heapq
def mergeKLists(lists):
    heap = []
    for l in lists:
        for val in l:
            heapq.heappush(heap, val)
    res = []
    while heap:
        res.append(heapq.heappop(heap))
    return res

lists = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(lists))  # [1,1,2,3,4,4,5,6]
```

---

## LeetCode Heap 常見題目

| 題號 | 題名 | 難度 | 說明 |
|------|------|------|------|
| 703 | Kth Largest Element in a Stream | Easy | Min-Heap 維護 Top-K |
| 215 | Kth Largest Element in an Array | Medium | Heap / Quickselect |
| 23 | Merge k Sorted Lists | Hard | Min-Heap 合併多個排序列表 |
| 703 | Find Kth Largest Element in a Stream | Easy | 優先隊列動態更新 |
| 347 | Top K Frequent Elements | Medium | Counter + Heap |
| 1046 | Last Stone Weight | Easy | Max-Heap |
| 295 | Find Median from Data Stream | Hard | Min-Heap + Max-Heap |

---

## Heap vs BST vs Segment Tree

| 特性 | Heap | BST | Segment Tree |
|------|------|-----|--------------|
| 插入 | O(log n) | O(log n) | O(log n) |
| 查詢最大/最小 | O(1) | O(log n) | O(log n) |
| 區間查詢 | ❌ | ❌ | ✔ |
| 前綴查詢 | ❌ | ❌ | ❌ |
| 空間 | O(n) | O(n) | O(4n) |

---

## 學習建議

1. 熟悉 heapq 模組
2. 練習 Min-Heap / Max-Heap 操作
3. 解 Top-K / 優先隊列題目
4. 練習合併 K 個排序列表
5. 結合 Heap + DFS/DP 題目（LeetCode Hard）

---
