# 🌳 字典樹 Trie

字典樹 Trie 是樹型結構，支援：

- 字串集合管理
- 前綴匹配
- 自動補全
- 多種字串查詢優化
- 支援通配符、加權計算

---

## Trie 範例結構

給定字串集合：

```
["apple","app","bat","ball","batter"]
```

Trie 結構：

```
         root
       /      \
      a        b
      |        |
      p        a
      |        |
      p        l
      | \       \
      l  e       t
      |           \
      e            t
(end)           (end)
```

- 每條路徑代表字串前綴
- is_end 標記字串結尾

---

## 基本操作

- **Insert(word)**：插入字串
- **Search(word)**：查詢完整字串
- **StartsWith(prefix)**：查詢前綴
- **Delete(word)**（進階）：刪除字串
- **CountWords(prefix)**（進階）：計算前綴出現次數
- **Wildcard Search**（進階）：支援 '.' 或 '?' 通配符

---

## Python Trie 基礎版本

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

---

## 進階功能：計算前綴出現次數

```python
class TrieNodeCount:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # 記錄前綴次數

class TrieCount:
    def __init__(self):
        self.root = TrieNodeCount()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNodeCount()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def countPrefix(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count
```

---

## 進階功能：支援通配符搜尋

```python
class TrieWildcard:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            return False
        return dfs(self.root, 0)
```

---

## 使用範例

```python
trie = TrieWildcard()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")

print(trie.search("apple"))  # True
print(trie.search("a..le"))  # True
print(trie.search("b.t"))    # True
print(trie.search("b..l"))   # True
print(trie.search("cat"))    # False

trie_count = TrieCount()
trie_count.insert("apple")
trie_count.insert("app")
trie_count.insert("apex")
print(trie_count.countPrefix("ap"))  # 3
```

---

## Trie 常用 LeetCode 題目

| 題號 | 題名 | 難度 | 功能 |
|------|------|------|------|
| 208 | Implement Trie | Medium | 基本 Trie |
| 211 | Add and Search Word | Medium | 支援 '.' 通配符 |
| 648 | Replace Words | Medium | 前綴匹配 |
| 212 | Word Search II | Hard | Trie + DFS |
| 677 | Map Sum Pairs | Medium | Trie + sum 記錄 |
| 745 | Prefix and Suffix Search | Hard | 雙向 Trie |
| 500 | Keyboard Row | Easy | Trie 應用 |
| 1804 | Implement Trie II | Medium | 計數 + 前綴搜尋 |

---

## Trie vs HashMap

| 特性 | Trie | HashMap/Set |
|------|------|-------------|
| 插入 | O(L) | O(L) |
| 查詢 | O(L) | O(L) |
| 前綴查詢 | ✔ | ❌ 需遍歷 |
| 通配符搜尋 | ✔ | ❌ |
| 空間消耗 | 高 | 中 |
| 適用場景 | 前綴匹配、自動補全、單詞統計 | 單詞查找 |

---

## 學習建議

1. 基礎 Trie（Insert/Search/StartsWith）
2. 前綴計數/自動補全
3. 通配符搜尋
4. LeetCode Hard 題目：Trie + DFS / Trie + DP
5. 進一步：壓縮 Trie / AC 自動機

---
