# An Iterative Python program to do DFS traversal from  
# a given source vertex. DFS(int s) traverses vertices  
# reachable from s.  
  
# This class represents a directed graph using adjacency  
# list representation 

from collections import defaultdict  
class Graph:  
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
    
    # to add an edge to graph 
    def addEdge(self,u, v):     # to add an edge to graph 
        self.graph[u].append(v)    
  
  
   
    def DFS(self,v):       
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
        
        # Create a stack for DFS  
        stack = [] 
  
        # Push the current source node.  
        stack.append(v)  
  
        while (len(stack)):  
            # Pop a vertex from stack and print it  
            v = stack[-1]  
            stack.pop() 
            
            # Stack may contain same vertex twice. So  
            # we need to print the popped item only  
            # if it is not visited.  
            if not visited[v]:  
                print(v,end=' ') 
                visited[v] = True 
  
            # Get all adjacent vertices of the popped vertex s  
            # If a adjacent has not been visited, then push it  
            # to the stack.  
            for node in self.graph[v]:  
                if not visited[node]:  
                    stack.append(node)
  
  
  
# Driver program to test methods of graph class  
  
g = Graph(); # Total 5 vertices in graph  
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(1, 0) 
g.addEdge(2, 1) 
g.addEdge(3, 4) 
g.addEdge(4, 0)   
print("Following is Depth First Traversal")  
g.DFS(0) 
  

