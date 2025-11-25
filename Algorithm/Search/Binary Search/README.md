# Binary Search


  
## 一般的版本


```python
def binarySearch(arr,target):
    l ,r = 0 ,len(arr) - 1
    
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1    
    return -1
```

## 分治法


```python
def binarySearch_res(arr,l,r,target):
    if l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1  
        return binarySearch_res(arr,l,r,target)
    return -1
```

或是
```python
def binarySearch_res(arr,l,r,target):
    if l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:           
            return binarySearch_res(arr,mid + 1,r,target)
        else:           
            return binarySearch_res(arr,l,mid - 1,target)      
    return -1
```