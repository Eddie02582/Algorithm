
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
    
    
assert binarySearch([ 2, 5, 8, 12, 16,23,38,56,72,91 ],23) == 5

assert binarySearch([ 2, 5, 8, 12, 16,23,38,56,72,91 ],17) == -1

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

assert binarySearch_res([ 2, 5, 8, 12, 16,23,38,56,72,91 ],0,9,23) == 5
