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

    
    
    
cache = LRUCache(2);        
        
cache.put(1, 1);

cache.put(2, 2);

cache.get(1);    
cache.put(3, 3);
cache.get(2);      
cache.put(1, 4);    

           
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        