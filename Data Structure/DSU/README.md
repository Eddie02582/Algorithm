# 🔗 Disjoint Set Union (DSU / Union-Find)

DSU（又稱 Union-Find）是一種資料結構，用於管理 **不相交集合**，支持快速：

- 查詢元素所在集合（Find）
- 合併兩個集合（Union）
- 判斷是否在同一集合中

常用於：

- 判斷圖是否有環
- 連通性查詢
- Kruskal 最小生成樹
- 網路/社群合併問題

---

## 📌 基本操作

1. **初始化**

每個節點自成一集合，`parent[i] = i`  

2. **Find（查找代表）**

回傳集合代表（root），可用 **路徑壓縮 Path Compression** 優化  

3. **Union（合併集合）**

將兩個集合合併，可用 **按秩 Union by Rank / Size** 優化

---

## Python 範例 — 基本 DSU

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))  # parent[i] = i
        self.rank = [1] * n           # 可選，用於按秩合併

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路徑壓縮
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # 已在同一集合
        # 按秩合併
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

---

## 使用範例

```python
dsu = DSU(5)
dsu.union(0, 1)
dsu.union(1, 2)
print(dsu.connected(0, 2))  # True
print(dsu.connected(0, 3))  # False
dsu.union(3, 4)
print(dsu.connected(3, 4))  # True
```

---

## DSU 應用場景

1. **判斷圖是否有環**  

```python
edges = [(0,1),(1,2),(2,0)]
dsu = DSU(3)
has_cycle = False
for u,v in edges:
    if not dsu.union(u,v):
        has_cycle = True
        break
print(has_cycle)  # True
```

2. **計算連通分量**  

```python
n = 5
edges = [(0,1),(1,2),(3,4)]
dsu = DSU(n)
for u,v in edges:
    dsu.union(u,v)
components = len(set(dsu.find(i) for i in range(n)))
print(components)  # 2
```

3. **Kruskal 最小生成樹**

```python
edges = [(1,0,1),(2,0,2),(3,1,2)]  # (weight,u,v)
edges.sort()
dsu = DSU(4)
mst_weight = 0
for w,u,v in edges:
    if dsu.union(u,v):
        mst_weight += w
print(mst_weight)
```

---

## LeetCode DSU 常見題目

| 題號 | 題名 | 難度 | 說明 |
|------|------|------|------|
| 547 | Number of Provinces | Medium | 連通分量 |
| 684 | Redundant Connection | Medium | 判斷環 |
| 261 | Graph Valid Tree | Medium | 判斷是否為樹 |
| 990 | Satisfiability of Equality Equations | Medium | 等式/不等式 |
| 924 | Minimize Malware Spread | Hard | DSU + 集合統計 |
| 323 | Number of Connected Components in an Undirected Graph | Medium | 連通分量計數 |

---

## DSU 特性與優化

- Find + Path Compression：幾乎 O(1) 平均
- Union by Rank / Size：保持樹扁平
- 時間複雜度：O(α(n))，α 為反阿克曼函數
- 適合連通性問題、圖判環、最小生成樹

---

## 學習建議

1. 熟練 DSU 基本操作：初始化、Find、Union、Connected
2. 練習圖論題目：Cycle、Connected Components
3. 進階應用：Kruskal MST、集群統計
4. 掌握 Path Compression 與 Union by Rank 優化技巧
5. 解 LeetCode 547, 684, 323, 924 等題目

---

✔ 完整 DSU Markdown 教學（Python + LeetCode 範例）
