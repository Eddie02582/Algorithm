# 📊 Topological Sort — 拓撲排序

拓撲排序（Topological Sort）是對 **有向無環圖 DAG (Directed Acyclic Graph)** 的節點進行排序，使得：

```
若有邊 u -> v，則 u 在排序中出現於 v 之前
```

常用於：

- 任務調度（Task Scheduling）
- 編譯順序
- 依賴關係解析（Dependency Resolution）

---

## 📌 拓撲排序方法

### 1️⃣ Kahn 演算法 (BFS)

步驟：

1. 計算每個節點的入度 `in_degree`
2. 將入度為 0 的節點加入隊列
3. 依序彈出節點，將其鄰居的入度減 1
4. 若鄰居入度變為 0，加入隊列
5. 直到隊列空，得到拓撲排序

時間複雜度：O(V + E)

---

### 2️⃣ DFS 方法

1. 對每個未訪問節點執行 DFS
2. 對節點的每個鄰居遞迴 DFS
3. 遞歸結束後將節點加入結果堆疊
4. 最後將堆疊反轉得到拓撲排序

時間複雜度：O(V + E)

---

## Python 範例 — Kahn 演算法

```python
from collections import deque, defaultdict

def topological_sort_kahn(n, edges):
    """
    n: 節點數量 (0 ~ n-1)
    edges: 邊列表 [(u, v), ...]
    """
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(topo_order) != n:
        return []  # 有環，不存在拓撲排序
    return topo_order
```

---

## Python 範例 — DFS 方法

```python
from collections import defaultdict

def topological_sort_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = [0] * n  # 0=未訪問,1=訪問中,2=已完成
    topo_order = []
    cycle = [False]
    
    def dfs(u):
        if visited[u] == 1:
            cycle[0] = True
            return
        if visited[u] == 2:
            return
        visited[u] = 1
        for v in graph[u]:
            dfs(v)
        visited[u] = 2
        topo_order.append(u)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
    
    if cycle[0]:
        return []  # 有環
    return topo_order[::-1]
```

---

## 使用範例

```python
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
n = 6

print(topological_sort_kahn(n, edges))  # 可能輸出: [4,5,0,2,3,1]
print(topological_sort_dfs(n, edges))   # 可能輸出: [5,4,2,3,1,0]
```

---

## 特性與注意事項

- 適用於 **有向無環圖 (DAG)**  
- 若圖有環，拓撲排序不存在
- 常用於：
  - 編譯依賴
  - 任務排程
  - 項目依賴管理
- 時間複雜度：O(V + E)  
- 空間複雜度：O(V + E)

---

## LeetCode 拓撲排序常見題目

| 題號 | 題名 | 難度 | 說明 |
|------|------|------|------|
| 207 | Course Schedule | Medium | 是否存在拓撲排序（檢查環） |
| 210 | Course Schedule II | Medium | 返回拓撲排序（課程順序） |
| 269 | Alien Dictionary | Hard | 拓撲排序 + 字母依賴 |
| 310 | Minimum Height Trees | Medium | 拓撲排序 + 刪葉 BFS |
| 366 | Find Leaves of Binary Tree | Medium | 模擬拓撲排序刪葉節點 |

---

## 拓撲排序 vs Dijkstra vs BFS

| 特性 | Topological Sort | Dijkstra | BFS |
|------|-----------------|---------|-----|
| 適用圖 | DAG | 帶權圖（非負） | 無權圖/層序 |
| 結果 | 節點線性順序 | 最短距離 | 層次順序 |
| 有環檢查 | 可檢查 | ❌ | ❌ |
| 時間複雜度 | O(V+E) | O((V+E) log V) | O(V+E) |

---

## 學習建議

1. 熟練 Kahn + DFS 兩種方法
2. 練習課程排程與依賴解析
3. 結合 BFS/DFS 解 LeetCode Hard 題目
4. 理解 DAG 與有向圖有環的差別
5. 可擴展到 Minimum Height Tree、Alien Dictionary 題目


