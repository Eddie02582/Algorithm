class Graph: 
    def __init__(self,graph):
        self.graph = graph
        self.row = len(graph)
        self.col = len(graph[0])
        
    
    def isSafe(self, i, j, visited): 
        # row number is in range, column number 
        # is in range and value is 1  
        # and not yet visited 
        return (i >= 0 and i < self.row and 
                j >= 0 and j < self.col and 
                not visited[i][j] and self.graph[i][j])
    
    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 
        visited[i][j] = True
        for k in range(8): 
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
                self.DFS(i + rowNbr[k], j + colNbr[k], visited) 

        
    def countIslands(self): 
        # Make a bool array to mark visited cells. 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self.col)]for i in range(self.row)] 
      
        # Initialize count as 0 and travese  
        # through the all cells of 
        # given matrix 
        count = 0
        for i in range(self.row): 
            for j in range(self.col): 
                # If a cell with value 1 is not visited yet,  
                # then new island found 
                if visited[i][j] == False and self.graph[i][j] == 1: 
                    # Visit all cells in this island  
                    # and increment island count 
                    self.DFS(i, j, visited) 
                    count += 1
        return count 
        
class Graph2: 
    def __init__(self,graph):
        self.graph = graph
        self.row = len(graph)
        self.col = len(graph[0])
        
    
    def isSafe(self, i, j, visited): 
        # row number is in range, column number 
        # is in range and value is 1  
        # and not yet visited 
        return (i >= 0 and i < self.row and 
                j >= 0 and j < self.col and 
                not visited[i][j] and self.graph[i][j])
        
    def countIslands(self): 
        # Make a bool array to mark visited cells. 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self.col)]for i in range(self.row)] 
      
        # Initialize count as 0 and travese  
        # through the all cells of 
        # given matrix 
        count = 0
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 
        for i in range(self.row): 
            for j in range(self.col):                 
                if visited[i][j] == False and self.graph[i][j] == 1: 
                    visited[i][j] == True
                    queue = []
                    queue.append([i,j])
                    while queue:
                        v = queue.pop(0)
                        ci,cj = v
                        for k in range(8):
                            ni,nj = ci + rowNbr[k] ,cj + colNbr[k]
                            if self.isSafe(ni , nj, visited):                                 
                                queue.append([ni,nj])
                                visited[ni][nj] = True                  
                   
                    count += 1
        return count 
                  
        
        
        
        
        
        
          
graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
  
  

g = Graph(graph) 
  
print ("Number of islands is:")
print (g.countIslands()) 

g = Graph2(graph) 
print (g.countIslands()) 













  