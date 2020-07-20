# Quick Sort 

快速排序使用分治法(Divide and conquer)策略來把一個序列（list）分為較小和較大的2個子序列，然後遞迴地排序兩個子序列。<br>

## Algorithm 

步驟
<ul>
    <li>挑選基準值：從數列中挑出一個元素，稱為「基準」(pivot)</li>
    <li>分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面(與基準值相等的數可以到任何一邊)。在這個分割結束之後，對基準值的排序就已經完成，</li>
    <li>遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。</li>
</ul>

這邊取pivot 有幾種取法
<ul>
    <li>始終選擇第一個元素</li>
    <li>始終選擇最後一個元素</li>
    <li>隨機選擇一個</li>
    <li>選擇中間的元素</li>
</ul>

## Example 

## Python

``` python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
```

## Example  (Inplace)

雙邊循環法
``` python
def quickSort_twoPointer(arr,startIndex,endIndex):            
    def partition(arr, startIndex,endIndex):  
        pivot,left,right = arr[startIndex],startIndex,endIndex
        while left != right:
            while left < right and arr[right] > pivot:
                right -= 1
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                arr[left],arr[right] = arr[right],arr[left]
        
        arr[startIndex] = arr[left]
        arr[left] = pivot
        return left
        
    if startIndex >= endIndex:
        return 
    pivotIndex = partition(arr, startIndex, endIndex)
    quickSort_twoPoint(arr, startIndex, pivotIndex - 1)
    quickSort_twoPoint(arr, pivotIndex + 1, endIndex)   

``` 
單邊循環法


``` python
def quickSort_Pointer(arr,startIndex,endIndex):            
    def partition(arr, startIndex,endIndex):  
        pivot,mark = arr[startIndex],startIndex
        for i in range(startIndex + 1,endIndex + 1):            
            if arr[i] < pivot:
                mark += 1
                arr[mark],arr[i] = arr[i],arr[mark]
        
        arr[startIndex] = arr[mark]
        arr[mark] = pivot
        return mark
        
    if startIndex >= endIndex:
        return 
    pivotIndex = partition(arr, startIndex, endIndex)
    quickSort_Pointer(arr, startIndex, pivotIndex - 1)
    quickSort_Pointer(arr, pivotIndex + 1, endIndex)   
``` 



























