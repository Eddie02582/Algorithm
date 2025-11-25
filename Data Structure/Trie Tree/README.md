# 🌳 字典樹 (Trie)

字典樹（Trie）是一種樹型資料結構，用於儲存 **字串集合**，常用於：

- 字典查詢（前綴匹配）
- 自動補全
- 單詞統計
- 字串搜索優化

---

## 📌 Trie 的結構

- 每個節點代表字母或字元
- 路徑從根到節點代表字串前綴
- 可快速查詢某個字串是否存在，或某個前綴是否存在

範例：

假設有字串集合 `["apple","app","bat","ball"]`：

```
        root
       /    \
      a      b
      |      |
      p      a
      |      |
      p      l
      |      |
      l      l
      |      |
      e      (end)
     (end)
```

---

## 📌 Trie 基本操作

- 插入字串（Insert）
- 查詢字串是否存在（Search）
- 查詢是否有特定前綴（StartsWith）
- 可擴展功能：計算出現次數、刪除字串等

---

## Python Trie 範例

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

## 📌 使用範例

```python
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")

print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("ap"))     # False
print(trie.startsWith("ap")) # True
print(trie.startsWith("ba")) # True
print(trie.startsWith("cat"))# False
```

---

## 📌 Trie 的特點

- 適合大量字串查詢
- 插入、查詢時間複雜度與字串長度 L 有關：O(L)
- 空間消耗大於 Hash Map，但支援前綴操作
- 可進一步改良成 **壓縮字典樹（Radix Trie）** 或 **AC自動機**

---

## 📌 LeetCode 常見 Trie 題目

| 題號 | 題名 | 難度 | 說明 |
|------|------|------|------|
| 208 | Implement Trie | Medium | 基本 Trie 操作 |
| 211 | Add and Search Word | Medium | 支援 '.' 通配符 |
| 648 | Replace Words | Medium | Trie + 前綴匹配 |
| 212 | Word Search II | Hard | Trie + DFS |
| 677 | Map Sum Pairs | Medium | Trie + sum 記錄 |

---

## 📌 Trie vs HashMap

| 特性 | Trie | HashMap/Set |
|------|------|-------------|
| 插入 | O(L) | O(L) |
| 查詢 | O(L) | O(L) |
| 前綴查詢 | ✔ | ❌（需額外處理） |
| 空間消耗 | 高 | 中 |
| 適用場景 | 前綴匹配、自動補全、單詞統計 | 簡單字串查找 |

---

## 🎯 Trie 學習建議

1. 實作基本 Trie（Insert/Search/StartsWith）
2. 練習前綴匹配題目（Replace Words, Autocomplete）
3. 擴展進階功能（AC 自動機、壓縮 Trie）
4. 將 Trie 與 DFS/DP 結合解 LeetCode Hard 題目


