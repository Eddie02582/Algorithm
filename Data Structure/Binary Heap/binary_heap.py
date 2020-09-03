class Solution(object):
    def upAdjust(self, array):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        childIndex = len(array) - 1
        parentIndex = (childIndex - 1)//2
        temp = array[childIndex]
        while childIndex > 0 and temp < array[parentIndex]:
            array[childIndex] = array[parentIndex]
            #update child
            childIndex = parentIndex
            #update parent
            parentIndex = (childIndex - 1)// 2
        
        array[childIndex] = temp
        
        #return array
            
    def downAdjust(self, arry,parentIndex,length):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = arry[parentIndex]
        childIndex = 2 * parentIndex + 1      
        
        while childIndex < length:
            if childIndex + 1 < length and array[childIndex + 1] < array[childIndex]:
                childIndex += 1
            if temp <= array[childIndex]:
                break
            array[parentIndex] = array[childIndex]
            parentIndex = childIndex
            childIndex = 2 * parentIndex + 1
            #childIndex = 2 * childIndex + 1
        
        array[parentIndex] = temp
    
    def buildHeap(self,array):
        start = (len(array) - 2)//2
        for i in range(start, -1 , -1):
            self.downAdjust(array,i,len(array))
        
'''
        1
       / \
      3    2
     / \  / \
    6  5 7  8
   / \
  9  10
'''



array = [1,3,2,6,5,7,8,9,10,0]
sol = Solution()
sol.upAdjust(array)
print (array)

array = [7,1,3,10,5,2,8,9,6]
sol.buildHeap(array)
print (array)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        