# Merge Sort 

## Algorithm 
將兩個有序對數組合併成一個更大的有序數組


動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>

步驟
<ul>
    <li>將陣列拆程左邊和右邊</li>
    <li>左邊呼叫mergeSort</li>
    <li>右邊呼叫mergeSort</li>
    <li>合併</li>
</ul>

<img src = ""></img>
## Example 


## Python


``` python
def mergeSort(arr):          
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]   
    mergeSort(left)    
    mergeSort(right)       

    i,j =0,0
    while i <len(left) and j <len(right):
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1
        
    while i < len(left): 
        arr[i + j] = left[i]
        i+= 1      
      
    while j < len(right): 
        arr[i + j] = right[j]
        j+= 1
       
        
    return arr  

```








