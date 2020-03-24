'''
    x1   x  x2
    y1   y  y2
    
    x = x1 + ((x2 - x1)/(y2 - y1)) * (y - y1)

'''

def interpolationSearch(arr, n, x): 
    l , h = 0 , n - 1
    while l <= h and x >= arr[l] and x <= arr[h]:
        if l == h:
            if arr[l] == x:
                return x
            return - 1
        
        pos = l + ( (x - arr[l]) * (h - l))//(arr[h] - arr[l])
        
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            l = pos + 1
        else:
            h = pos - 1
            
    return -1
    
arr = [10, 12, 13, 16, 18, 19, 20, 21, 
                22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 
  
x = 18 # Element to be searched 
print (interpolationSearch(arr, n, x))