## 🌳 Segment Tree (線段樹) 筆記與實現

Segment Tree 是一種高效的**區間查詢與更新**的二元樹資料結構。它允許我們在 $O(\log n)$ 的時間複雜度內完成對陣列區間的聚合查詢（如求和、最大值、最小值）和單點/區間更新。

### 📌 核心概念 (Core Concepts)

| 節點類型 | 區間表示 | 資訊儲存 |
| :--- | :--- | :--- |
| **根節點 (Root)** | 代表整個原始陣列 $[0, n-1]$。 | 整個區間的聚合值。 |
| **內部節點 (Internal)** | 代表一個子區間 $[L, R]$。 | 其左右子節點聚合值的組合。 |
| **葉節點 (Leaf)** | 代表原始陣列中的單個元素 $[i, i]$。 | 原始陣列 $A[i]$ 的值。 |

每個內部節點 $[L, R]$ 的子節點劃分如下：
* **左子節點 (Left Child):** 代表區間 $[L, M]$。
* **右子節點 (Right Child):** 代表區間 $[M+1, R]$。
* 其中 $M = \lfloor (L+R)/2 \rfloor$。

### 💻 程式碼實現：區間和 (Python Implementation: Range Sum)

以下是一個 Python 類別實現，用於解決 **單點更新 (Point Update)** 和 **區間求和 (Range Sum Query)** 問題。

```python
class SegmentTree:
    """
    Segment Tree implementation for Range Sum Query and Point Update.
    Time Complexity:
    - Build: O(n)
    - Update: O(log n)
    - Query: O(log n)
    """
    def __init__(self, nums: list[int]):
        """
        Initializes the Segment Tree.
        :param nums: The original array.
        """
        self.n = len(nums)
        # Tree array size is typically 4 * n for safety.
        self.tree = [0] * (4 * self.n) 
        self._nums = nums
        if self.n > 0:
            self._build(0, 0, self.n - 1)

    # --- 1. Build Operation ---

    def _build(self, tree_index, start, end):
        """
        Recursively builds the segment tree.
        :param tree_index: Current node index in self.tree.
        :param start: Start index of the current node's range.
        :param end: End index of the current node's range.
        """
        if start == end:
            # Leaf node: Store the value from the original array.
            self.tree[tree_index] = self._nums[start]
            return

        mid = start + (end - start) // 2
        left_child = 2 * tree_index + 1
        right_child = 2 * tree_index + 2

        # Recursively build children
        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)

        # Internal node: Aggregate (Sum) the children's results.
        self.tree[tree_index] = self.tree[left_child] + self.tree[right_child]

    # --- 2. Update Operation (Point Update) ---

    def update(self, index: int, val: int):
        """
        Updates the element at the given index and updates the tree.
        :param index: Index of the element to update.
        :param val: The new value.
        """
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, tree_index, start, end, index, val):
        if start == end:
            # Found the leaf node, update the value.
            self.tree[tree_index] = val
            return

        mid = start + (end - start) // 2
        left_child = 2 * tree_index + 1
        right_child = 2 * tree_index + 2

        if index <= mid:
            # The target index is in the left child's range.
            self._update(left_child, start, mid, index, val)
        else:
            # The target index is in the right child's range.
            self._update(right_child, mid + 1, end, index, val)

        # Backtrack: Update the current node's value based on children.
        self.tree[tree_index] = self.tree[left_child] + self.tree[right_child]

    # --- 3. Query Operation (Range Sum) ---

    def query(self, L: int, R: int) -> int:
        """
        Queries the sum of the range [L, R].
        :param L: Query range left boundary.
        :param R: Query range right boundary.
        :return: The sum of elements in the range [L, R].
        """
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, tree_index, start, end, L, R):
        # Case 1: Current node range [start, end] is COMPLETELY INSIDE target range [L, R]
        if L <= start and end <= R:
            return self.tree[tree_index]

        # Case 2: Current node range [start, end] has NO OVERLAP with target range [L, R]
        if start > R or end < L:
            return 0 # Return identity element for sum (0)

        # Case 3: PARTIAL OVERLAP, recursively query children
        mid = start + (end - start) // 2
        left_child = 2 * tree_index + 1
        right_child = 2 * tree_index + 2

        # Sum the results from the children
        sum_left = self._query(left_child, start, mid, L, R)
        sum_right = self._query(right_child, mid + 1, end, L, R)

        return sum_left + sum_right


# --- Example Usage ---
# nums = [1, 3, 5, 7, 9]
# st = SegmentTree(nums)

# # Initial Query: sumRange(1, 4) -> 3 + 5 + 7 + 9 = 24
# print(f"Query [1, 4] initial sum: {st.query(1, 4)}") 

# # Update: update(2, 6) -> nums becomes [1, 3, 6, 7, 9]
# st.update(2, 6) 

# # Updated Query: sumRange(1, 4) -> 3 + 6 + 7 + 9 = 25
# print(f"Query [1, 4] updated sum: {st.query(1, 4)}")


### 🧠 LeetCode 範例：307. Range Sum Query - Mutable

#### 題目連結 (Link)
[LeetCode 307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

#### 題目要求 (Problem Statement)
實現一個 `NumArray` 類別，支援以下操作：
1.  `NumArray(int[] nums)`: 初始化物件。
2.  `void update(int index, int val)`: 將 `nums[index]` 更新為 `val`。
3.  `int sumRange(int left, int right)`: 返回 `nums` 區間 `[left, right]` 的總和。

#### 解決方案 (Solution)

```python
class NumArray:
    """
    LeetCode 307 Solution using Segment Tree.
    """
    def __init__(self, nums: list[int]):
        # The SegmentTree class (defined above) must be accessible or defined within this scope 
        # for this LeetCode solution to work.
        self.seg_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        # Delegate the update operation to the Segment Tree.
        self.seg_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        # Delegate the query operation to the Segment Tree.
        return self.seg_tree.query(left, right)




