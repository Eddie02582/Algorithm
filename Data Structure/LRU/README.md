# LRU




 
 
# 代碼實現I
這邊的作法利用sentinel,tail坐定位,這邊是將越常使用的放置頭<br>
有幾個操作
<ul>
    <li>put:如果該節點key以存在緩存,需要刪掉節點,把新的節點放置頭部,判斷是否超過緩存容量,如果超過緩存刪掉最後節點</li>
    <li>get:需要刪掉該key節點,並把新的節點放置頭部</li>
</ul>
 
sentinel -> data1 ->data2 -> tail
 
```
class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # 最大容量
        self.cap = capacity
        self.cache = {}
        # 哨兵节点
        self.sentinel = ListNode(None, None)
        # 尾节点： 用于链表容量超过最大容量是快速定位、删除尾节点
        self.tail = ListNode(None, None)
        # 初始化双向链表
        self.sentinel.next = self.tail
        self.tail.prev = self.sentinel

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 从链表中删除该节点
            self.remove_node_from_list(node)
            # 把该节点添加到链表头部
            self.push_node_to_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 如果该节点已经存在那么删除该节点
        if key in self.cache:
            self.remove_node_from_list(self.cache[key])

        # 把该节点添加到链表头部
        node = ListNode(key, value)
        self.cache[key] = node
        self.push_node_to_front(node)

        # 如果链表超过最大容量，删除链表尾部节点
        if len(self.cache) > self.cap:
            last_node = self.tail.prev
            self.remove_node_from_list(last_node)
            self.cache.pop(last_node.key)

    # 从链表中删除节点
    def remove_node_from_list(self, node: "ListNode") -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # 添加节点到链表头部
    def push_node_to_front(self, node: "ListNode") -> None:
        nxt = self.sentinel.next
        self.sentinel.next = node
        node.next = nxt
        node.prev = self.sentinel
        nxt.prev = node
        
        
        
cache = LRUCache(2);        
        
cache.put(1, 1);
#cache = [(1, 1)]
cache.put(2, 2);
#cache = [(2, 2), (1, 1)]
cache.get(1);       #返回 1
#cache = [(1, 1), (2, 2)]
#解释：因为最近访问了键 1，所以提前至队头
#返回键 1 对应的值 1
cache.put(3, 3);
#cache = [(3, 3), (1, 1)]
#解释：缓存容量已满，需要删除内容空出位置
#优先删除久未使用的数据，也就是队尾的数据
#然后把新的数据插入队头
cache.get(2);       #返回 -1 (未找到)
#cache = [(3, 3), (1, 1)]
#解释：cache 中不存在键为 2 的数据
cache.put(1, 4);    
#cache = [(1, 4), (3, 3)]
#解释：键 1 已存在，把原始值 1 覆盖为 4
```
        
        
        
# 代碼實現 II   

這邊是將越常使用的放置後面,利用head,end記錄節點是否在頭尾<br>
有幾個操作
<ul>
    <li>put:如果該節點key以存在緩存,需要刪掉節點,把新的節點放置頭部,判斷是否超過緩存容量,如果超過緩存刪掉最後節點</li>
    <li>get:需要刪掉該key節點,並把新的節點放置頭部</li>
</ul>

head -> data1 ->data2 ->end 
 
```        
class ListNode: 

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
     

class LRUCache:
    def __init__(self, capacity: int):       
        self.cap = capacity
        self.cache = {}
        self.end = None
        self.head = None        
       

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.refreshNode(node)          
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            #update node
            node.val = value
            self.refreshNode(node)        
        else:            
            if len(self.cache) >= self.cap:
                oldKey = self.removeNode(self.head)                
                self.cache.pop(oldKey)
                
            node = ListNode(key, value)
            self.addNode(node)
            self.cache[key] = node
                
    def remove(self,key:int) -> None:
        node = self.cache[key]
        self.removeNode(node)
        self.cache.pop(key)

    def refreshNode(self,node):
        if node == self.end:
            return
        self.removeNode(node)
        self.addNode(node)

    def removeNode(self,node):
        if node == self.head and node == self.end:
            self.head = None
            self.end = None
        elif node == self.end:
            self.end = self.end.prev
            self.end.next = None
        elif node == self.head:
            self.head = self.head.next
        else:
            node.pre.next = node.next
            node.next.pre = node.pre      
        
        return node.key
    
    
    def addNode(self,node):
        if self.end:
            self.end.next = node
            node.pre = self.end
            node.next = None
        
        self.end = node
        if not self.head:
            self.head = node        
        
```        







   
   
   