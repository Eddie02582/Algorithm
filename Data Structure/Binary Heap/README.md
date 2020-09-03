# Binary Heap

二叉堆本質上是一種完全二叉樹，它分為兩個類型。
1. 最大堆: 最大堆的任何一個父節點的值，都大於或等於它左、右孩子節點的值。
2. 最小堆: 最小堆的任何一個父節點的值，都小於或等於它左、右孩子節點的值。



# 操作

## 插入節點
以最小堆為例,新增0點
          1
        /   \
       3      2
      / \    / \
     6   5  7   8
    / \  /
   9  10 0*
   

新節點的父節點5比0大，顯然不符合最小堆的性質。於是讓新節點“上浮”，和父節點交換位置。
          1
        /   \
       3      2
      / \    / \
     6   0*  7   8
    / \  /
   9  10 5


新節點的父節點3比0大，顯然不符合最小堆的性質。於是讓新節點“上浮”，和父節點交換位置。

          1
        /   \
       3      2
      / \    / \
     6    0* 7  8
    / \  /
   9  10 5

   
新節點的父節點1比0大，顯然不符合最小堆的性質。於是讓新節點“”，和父節點交換位置。

          0
        /    \
       1      2
      /  \   /  \
     6    3 7    8
    / \  /
   9  10 5
   
 ## 刪除節點  
 是刪除最小値1
          1
        /   \
       3      2
      / \    / \
     6   5  7   8
    / \  
   9  10  
為了維持Binary Heap 將最後的節點移上去
          10
        /    \
       3      2
      / \    / \
     6   5  7   8
    /   
   9    
將10跟左右子節點最小的交換,這邊為2   
          2
        /    \
       3      10
      / \    / \
     6   5  7   8
    /   
   9      
   
將10跟左右子節點最小的交換,這邊為7   
          2
        /    \
       3      7
      / \    / \
     6   5  10  8
    /   
   9      
      
 ## 建構Binary Heap 
 構建二叉堆，也就是把一個無序的完全二叉樹調整為二叉堆<br>
          7
        /    \
       1      3
      / \    / \
     10  5  2   8
    /  \ 
   9    6   
   
首先，從最後一個非葉子節點開始，也就是從節點10開始。<br>
如果節點10大於它左、右孩子節點中最小的一個，則節點10"下沉"<br>   
          7
        /    \
       1      3
      / \    / \
     6  5   2   8
    / \ 
   9  10      




接下來輪到節點3，如果節點3大於它左、右孩子節點中最小的一個，則節點3“下沉”。<br>

          7
        /    \
       1      2
      / \    / \
     6  5   3   8
    / \ 
   9  10      
  
然後輪到節點1，如果節點1大於它左、右孩子節點中最小的一個，則節點1“下沉”。事實上節點1小於它的左、右孩子，所以不用改變。<br>
接下來輪到節點7，如果節點7大於它左、右孩子節點中最小的一個，則節點7“下沉”。 <br>  
   
          1
        /    \
       7      2
      / \    / \
     6  5   3   8
    / \ 
   9  10      
  
節點7繼續比較，繼續“下沉”。 <br>  
   
          1
        /    \
       5      2
      / \    / \
     6   7  3   8
    /  \ 
   9    10      
  
# 代碼實現  

          1
        /   \
       3      2
      / \    / \
     6   5  7   8
    / \  
   9  10 

二叉堆的存儲方式是順序存儲在陣列
=> [1,3,2,6,5,7,8,9,10]
 
從父節點找到子節點,假設父節點的下標是parent,那麼左子節點 2×parent+1；右子節點下標就是2×parent+2。

```
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
```

















   
   
   