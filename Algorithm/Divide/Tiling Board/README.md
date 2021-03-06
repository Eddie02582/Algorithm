# 棋牌覆蓋

          
## 題目


影片參考<a href = "https://www.youtube.com/watch?v=ss7eQtz-KHU">Maximum Subarray</a><br>
GeeksforGeeks<a href = "https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/">Tiling Problem using Divide and Conquer algorithm</a><
以下圖片取自GeeksforGeeks

棋盤覆蓋問題要求在2^k * 2^k 個方格組成的棋盤中，你給定任意一個特殊點，用一種方案實現對除該特殊點的棋盤實現全覆蓋。

## 分析

以8*8為例<br>
<img src="https://www.geeksforgeeks.org/wp-content/uploads/tiles2-1024x539.png" alt="tiles3" width="400" height="315">

我們把化簡4*4並在補上特殊點

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/tiles3.png" alt="tiles3" width="400" height="315">

我們把化簡2*2並在補上特殊點

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/tiles4.png" alt="tiles3" width="400" height="315">

所有都補上特殊點

<img src="https://www.geeksforgeeks.org/wp-content/uploads/tiles5-1024x793.png" alt="tiles3" width="400" height="315">


實現

解決方案就是利用分治法，將方形棋盤分成4部分，如果該特殊點在某一部分，我們就去遞歸他，如果不在某一部分，我們假設一個點為特殊點，同樣遞歸下去<br>

    左上角的子棋盤（若不存在特殊方格）：則將該子棋盤右下角的那個方格假設為特殊方格；<br>
    右上角的子棋盤（若不存在特殊方格）：則將該子棋盤左下角的那個方格假設為特殊方格；<br>
    左下角的子棋盤（若不存在特殊方格）：則將該子棋盤右上角的那個方格假設為特殊方格；<br>
    右下角的子棋盤（若不存在特殊方格）：則將該子棋盤左上角的那個方格假設為特殊方格；<br>




## Code

```python
class Solution():
    def __init__(self,specialRow,specialCol,size):
        self.number = 0
        self.specialRow = specialRow
        self.specialCol = specialCol
        self.board =[ ['00']*size  for i in range(size)]
        self.size = size

      
    def setBoard(self,specialROW,specialCOL,leftROW,leftCOL,size):
        if size == 1:
            return
        subSize = size //2
        self.number += 1
        n = self.number
        n = str(self.number).zfill(2)
        #假設特殊點在左上角區域
        if specialROW < (leftROW + subSize) and specialCOL < (leftCOL + subSize):
            self.setBoard(specialROW, specialCOL, leftROW, leftCOL, subSize)                
        else:
            #不在左上角，設左上角矩陣的右下角就是特殊點（和別的一起放置L形）              
            self.board[leftROW + subSize - 1][leftCOL + subSize - 1] = n
            self.setBoard(leftROW + subSize - 1, leftCOL + subSize - 1, leftROW, leftCOL, subSize)
        
        if specialROW < (leftROW + subSize) and specialCOL >= (leftCOL + subSize) :
            self.setBoard(specialROW, specialCOL, leftROW, leftCOL + subSize, subSize)               
        else: 
            #不在右上方，設右上方矩陣的左下角就是特殊點（和別的一起放置L形）
            self.board[leftROW + subSize -1][leftCOL + subSize] = n
            self.setBoard(leftROW + subSize -1, leftCOL + subSize, leftROW, leftCOL + subSize, subSize)
        
      
        #//特殊點在左下方
        if specialROW >= (leftROW + subSize) and specialCOL < (leftCOL + subSize): 
            self.setBoard(specialROW, specialCOL, leftROW + subSize, leftCOL, subSize)		
        else: 
            #不在左下方，設左下方矩陣的右上角就是特殊點（和別的一起放置L形）
            self.board[leftROW + subSize][leftCOL + subSize - 1] = n
            self.setBoard(leftROW + subSize, leftCOL + subSize - 1, leftROW + subSize, leftCOL, subSize)
        	
    
        #特殊點在右下角
        if specialROW >= (leftROW + subSize) and specialCOL >= (leftCOL + subSize):
            self.setBoard(specialROW, specialCOL, leftROW + subSize, leftCOL + subSize, subSize)
        		
        else:
            #不在右下角，設右下角矩陣的左上就是特殊點（和別的一起放置L形）
            self.board[leftROW + subSize][leftCOL + subSize] = n
            self.setBoard(leftROW + subSize, leftCOL + subSize, leftROW + subSize, leftCOL + subSize, subSize)       			

        
    def get_board(self):
        self.setBoard(self.specialRow,self.specialCol,0,0,self.size)   
        for row in self.board:
            print (row)
        return self.board
  
```