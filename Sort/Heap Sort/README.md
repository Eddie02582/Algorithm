# Heap Sort 


## Algorithm 

步驟
<ul>
    <li>將陣列變成最大堆Binary Heap</li>
    <li>將最大値移到最後(相當於執行Binary Heap刪除動作)</li>
    <li>重新調整陣列成Binary Heap</li>
    <li>尾巴網前一個,回到步驟2</li>
</ul>


## Example 

## Python

``` python
class Sort(object):
    def sift_down(self,array,parentIndex,length):
        childIndex = 2 * parentIndex + 1
        temp = array[parentIndex]
        while childIndex < length:
            if childIndex + 1 < length and array[childIndex] < array[childIndex + 1]:
                childIndex += 1
            if temp >= array[childIndex]:
                break
            
            array[parentIndex] = array[childIndex]
            parentIndex = childIndex
            childIndex = 2 * parentIndex + 1
        array[parentIndex] = temp    



    def heapSort(self,array):
        start = (len(array) - 2 ) //2 
        for i in range(start,-1,-1):
            self.sift_down(array,i,len(array))
        
        for end in range(len(array) - 1, 0, -1):
            array[0], array[end] = array[end], array[0]
            self.sift_down(array,0, end)
        
    quickSort_Pointer(arr, pivotIndex + 1, endIndex)   
``` 



























