# 迴圈賽程

          
## 題目

<ul>
    <li>設有n=2^k個運動員，要進行網球迴圈賽</li>
    <li>每個選手必須與其他n-1個選手各賽一次</li>
    <li>每個選手一天只能賽一次</li>
    <li>循環賽一共進行n-1天</li>
</ul>




## 分析
1.將所有的選手分為兩半，n個選手的比賽日程表可以通過為n/2個選手設計的比賽日程表來決定<br>
2.遞歸地用對選手進行分割，直到只剩下2個選手時，只要讓這2個選手進行比賽就可<br>


<img src = "https://github.com/Eddie02582/Algorithm/blob/master/Algorithm/Divide/Loop%20Schedule/1.png">

<img src = "https://github.com/Eddie02582/Algorithm/blob/master/Algorithm/Divide/Loop%20Schedule/2.png">

<img src = "https://github.com/Eddie02582/Algorithm/blob/master/Algorithm/Divide/Loop%20Schedule/3.png">

## Code

```python
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
```