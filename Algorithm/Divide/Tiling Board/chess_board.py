

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
    
#sol = Solution(3,1,8)
sol = Solution(0,1,4)

sol.get_board()
