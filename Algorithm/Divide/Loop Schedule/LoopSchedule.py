class Solution():    
    def table(self,k,n):
        res = [[0 for i in range(n)] for i in range(n)]        
        for i in range(n):
            res[0][i] = i + 1      
        m = 1
        
        def copy(to_x,to_y,form_x,from_y,r):
            for i in range(r):
                for j in range(r):
                    res[to_x + i][to_y + j] = res[form_x + i][from_y + j];        
        
        for r in range(0,k):    
            for i in range(0,n,2*m):
                copy(m,m + i ,0,i,m)
                copy(m,i,0,m + i,m)
            m *= 2
        return res    

        
    
    
sol = Solution()   
sol.table(3,8)