# 🌲 線段樹 (Segment Tree) — 完整學習指南（Python + LeetCode）

線段樹是一種支援 **動態更新 + 區間查詢** 並保持 **O(log n)** 時間複雜度的資料結構，常用於：

- 區間總和 (Range Sum)
- 區間最小值/最大值
- 區間更新（Lazy Propagation）

---

## 📌 為什麼需要線段樹？

給定陣列：

```
[2, 4, 5, 7, 8, 9, 12]
```

你要執行：

| 操作 | 範例 |
|------|------|
| 查詢區間和 | sum(1..5) |
| 更新 | arr[3] = 20 |

效率比較：

| 方法 | 區間查詢 | 更新 |
|------|----------|------|
| 暴力 | O(n) | O(1) |
| 前綴和 Prefix Sum | O(1) | ❌ 不支援 |
| Fenwick Tree (BIT) | O(log n) | O(log n) |
| **Segment Tree** | **O(log n)** | **O(log n)** |

---

## 📌 線段樹結構示意

陣列 `[2,4,5,7,8,9,12]` → 區間總和：

```
                [0,6]=47
              /              \
        [0,3]=18            [4,6]=29
        /      \            /       \
  [0,1]=6   [2,3]=12   [4,5]=17   [6,6]=12
  /    \
[0]=2 [1]=4
```

---

## 📌 Segment Tree Python 版本（支援查詢 + 更新）

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, l, r):
        if l == r:
            self.tree[index] = nums[l]
            return nums[l]
        mid = (l + r) // 2
        left_sum = self.build(nums, index*2+1, l, mid)
        right_sum = self.build(nums, index*2+2, mid+1, r)
        self.tree[index] = left_sum + right_sum
        return self.tree[index]

    def update(self, pos, value):
        self._update(0, 0, self.n-1, pos, value)

    def _update(self, index, l, r, pos, value):
        if l == r:
            self.tree[index] = value
            return
        mid = (l + r) // 2
        if pos <= mid:
            self._update(index*2+1, l, mid, pos, value)
        else:
            self._update(index*2+2, mid+1, r, pos, value)
        self.tree[index] = self.tree[index*2+1] + self.tree[index*2+2]

    def query(self, ql, qr):
        return self._query(0, 0, self.n-1, ql, qr)

    def _query(self, index, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[index]
        if r < ql or qr < l:
            return 0
        mid = (l + r) // 2
        return self._query(index*2+1, l, mid, ql, qr) + \
               self._query(index*2+2, mid+1, r, ql, qr)
```

---

## 📌 使用範例

```python
arr = [2,4,5,7,8,9,12]
seg = SegmentTree(arr)

print(seg.query(1, 5))  # 33
seg.update(2, 10)
print(seg.query(1, 5))  # 38
```

---

## 📌 Lazy Propagation — 區間修改優化

Lazy Propagation 用於解決：

❌ 每次對範圍更新（ex: +5）就必須推到底 → O(n)

✔ Lazy 樹允許「先記帳，之後需要時再更新」。

---

### Lazy Segment Tree Python 程式

```python
class LazySegmentTree:
    def __init__(self, nums):
        n = len(nums)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(nums, 0, 0, n - 1)

    def build(self, nums, idx, l, r):
        if l == r:
            self.tree[idx] = nums[l]
            return
        mid = (l+r)//2
        self.build(nums, idx*2+1, l, mid)
        self.build(nums, idx*2+2, mid+1, r)
        self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]

    def push(self, idx, l, r):
        if self.lazy[idx] != 0:
            mid = (l+r)//2
            self.tree[idx*2+1] += (mid-l+1) * self.lazy[idx]
            self.tree[idx*2+2] += (r-mid) * self.lazy[idx]
            self.lazy[idx*2+1] += self.lazy[idx]
            self.lazy[idx*2+2] += self.lazy[idx]
            self.lazy[idx] = 0

    def update_range(self, idx, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self.tree[idx] += (r-l+1) * val
            self.lazy[idx] += val
            return
        if r < ql or qr < l:
            return
        self.push(idx, l, r)
        mid = (l+r)//2
        self.update_range(idx*2+1, l, mid, ql, qr, val)
        self.update_range(idx*2+2, mid+1, r, ql, qr, val)
        self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]

    def query(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[idx]
        if r < ql or qr < l:
            return 0
        self.push(idx, l, r)
        mid = (l+r)//2
        return self.query(idx*2+1, l, mid, ql, qr) + \
               self.query(idx*2+2, mid+1, r, ql, qr)
```

---

## 📌 LeetCode 相關題目

| 題號 | 題名 | 難度 | 是否推薦用線段樹 |
|------|------|--------|----------------|
| 307 | Range Sum Query - Mutable | Medium | ⭐ 必學 |
| 308 | Range Sum Query 2D - Mutable | Hard | ✔ 2D Segment Tree |
| 715 | Range Module | Hard | ✔ Lazy Propagation |
| 1094 | Car Pooling | Medium | ✔ 可選 |
| 732 | My Calendar III | Hard | ⭐ Segment Tree / Map Sweep |

---

## 📌 Segment Tree vs Fenwick Tree

| 特性 | Segment Tree | Fenwick Tree (BIT) |
|------|--------------|------------------|
| 區間查詢 | ✔ | ✔ |
| 單點更新 | ✔ | ✔ |
| 區間更新 | ✔（Lazy Propagation） | ⚠ 有難度 |
| 支援 min/max 等自定義功能 | ✔ | ❌ 不適合 |
| 記憶體需求 | 高 | 低 |

---


