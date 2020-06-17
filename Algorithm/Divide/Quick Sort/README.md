# Quick Sort 

## Algorithm 
快速排序使用分治法（Divide and conquer）策略來把一個序列（list）分為較小和較大的2個子序列，然後遞迴地排序兩個子序列。<br>

步驟
<ul>
    <li>挑選基準值：從數列中挑出一個元素，稱為「基準」(pivot)</li>
    <li>分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面(與基準值相等的數可以到任何一邊)。在這個分割結束之後，對基準值的排序就已經完成，</li>
    <li>遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。</li>
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









