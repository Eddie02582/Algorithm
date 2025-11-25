# 🔗 Linked List (鏈結串列)

Linked List 是一種線性資料結構，由 **節點 Node** 連結而成，每個節點包含：

- 值 (val)
- 指向下一個節點的指標 (next)

用途：

- 插入/刪除效率高（O(1) 在節點已知時）
- 線性遍歷
- 支援單向、雙向、循環鏈結串列
- 常用於面試經典題型

---

## Linked List 節點結構

### 單向鏈結串列 Node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## 基本操作

### 1. 遍歷 Linked List

```python
def traverse(head):
    node = head
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
```

### 2. 插入節點

```python
# 在頭部插入
def insert_head(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# 在尾部插入
def insert_tail(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    node = head
    while node.next:
        node = node.next
    node.next = new_node
    return head
```

### 3. 刪除節點

```python
def delete_node(head, val):
    dummy = ListNode(0)
    dummy.next = head
    prev, node = dummy, head
    while node:
        if node.val == val:
            prev.next = node.next
            break
        prev, node = node, node.next
    return dummy.next
```

---

## 進階操作

### 反轉 Linked List

```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

### 找中間節點

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### 檢查是否有環

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### 合併兩個排序鏈表

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next
```

---

## 使用範例

```python
# 建立 Linked List: 1 -> 2 -> 3 -> None
head = ListNode(1)
head = insert_tail(head, 2)
head = insert_tail(head, 3)

traverse(head)  # 1 -> 2 -> 3 -> None

# 刪除節點 2
head = delete_node(head, 2)
traverse(head)  # 1 -> 3 -> None

# 反轉鏈表
head = reverse_list(head)
traverse(head)  # 3 -> 1 -> None
```

---

## LeetCode Linked List 常見題目

| 題號 | 題名 | 難度 | 說明 |
|------|------|------|------|
| 206 | Reverse Linked List | Easy | 反轉鏈表 |
| 21 | Merge Two Sorted Lists | Easy | 合併兩個排序鏈表 |
| 141 | Linked List Cycle | Easy | 判斷鏈表是否有環 |
| 142 | Linked List Cycle II | Medium | 找入環起點 |
| 876 | Middle of the Linked List | Easy | 找中間節點 |
| 19 | Remove Nth Node From End | Medium | 刪除倒數第 n 個節點 |
| 234 | Palindrome Linked List | Easy | 判斷回文鏈表 |
| 23 | Merge k Sorted Lists | Hard | 合併 K 個排序鏈表 |

---

## Linked List vs Array

| 特性 | Linked List | Array |
|------|------------|-------|
| 插入/刪除 | O(1) (已知節點) | O(n) |
| 查詢 | O(n) | O(1) |
| 空間 | 高（指標額外空間） | 低 |
| 靈活性 | 高 | 固定長度 |

---

## 學習建議

1. 熟練單向 Linked List 基本操作：遍歷、插入、刪除
2. 練習反轉、找中間節點、檢查環
3. 熟練合併兩個排序鏈表
4. 進階題目：Remove Nth, Palindrome, Merge k Lists
5. 掌握快慢指針技巧

---

