# 🌳 二元樹 (Binary Tree)

二元樹是一種每個節點最多有兩個子節點的樹型資料結構，常用於：

- 二元搜索樹 (BST)
- 樹遍歷
- 堆 (Heap)
- 表達式樹 / 遞迴問題

---

## 二元樹結構

- 每個節點最多兩個子節點：左子節點 (left)、右子節點 (right)
- 節點通常包含值 (val)
- 樹的根 (root) 是進入樹的唯一入口

範例：

```
       1
      / \
     2   3
    / \   \
   4   5   6
```

---

## Python 節點與樹定義

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## 常用操作

### 1. 遍歷 (Traversal)

- 前序 Preorder: root → left → right
- 中序 Inorder: left → root → right
- 後序 Postorder: left → right → root
- 層序 Level-order: BFS

```python
# Preorder
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# Inorder
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Postorder
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

# Level-order (BFS)
from collections import deque
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

---

## 建立範例樹

```python
# 範例樹：
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))
```

---

## 樹的基本操作

### 計算節點總數

```python
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### 計算樹高度

```python
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
```

### 搜尋節點值

```python
def search(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    return search(root.left, val) or search(root.right, val)
```

---

## 二元搜索樹 (BST) 特點

- 左子樹所有節點 < 根節點
- 右子樹所有節點 > 根節點
- 每棵子樹也符合 BST

BST 插入範例：

```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root
```

---

## LeetCode 常見二元樹題目

| 題號 | 題名 | 難度 | 說明 |
|------|------|------|------|
| 94 | Binary Tree Inorder Traversal | Easy | 中序遍歷 |
| 144 | Binary Tree Preorder Traversal | Easy | 前序遍歷 |
| 145 | Binary Tree Postorder Traversal | Medium | 後序遍歷 |
| 102 | Binary Tree Level Order Traversal | Medium | BFS 層序 |
| 104 | Maximum Depth of Binary Tree | Easy | 計算樹高度 |
| 110 | Balanced Binary Tree | Easy | 判斷平衡樹 |
| 222 | Count Complete Tree Nodes | Medium | 節點計數 |
| 106 | Construct Binary Tree from Inorder and Postorder | Medium | 樹重建 |

---

## 二元樹 vs 字典樹 vs 線段樹

| 資料結構 | 用途 | 插入/查詢複雜度 | 特點 |
|-----------|------|----------------|------|
| Binary Tree | 任意樹型資料 | O(log n) 平均 | 左右子節點，支援排序（BST） |
| Trie | 字串集合 / 前綴查詢 | O(L) | 前綴匹配，自動補全 |
| Segment Tree | 區間查詢/更新 | O(log n) | 區間操作，支援 sum/min/max |

---

## 學習建議

1. 熟練樹遍歷：Preorder, Inorder, Postorder, BFS
2. 實作 BST 插入、搜尋、刪除
3. 練習 LeetCode Easy/Medium 題目
4. 進階：平衡樹（AVL, Red-Black）、樹重建、DFS + DP 題目


