
     
def bubble_sort(array):
    
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1],array[j]           
   
    return array
    
def bubble_sort_flag(array):
    
    for i in range(0,len(array)):
        flag = False 
        for j in range(0,len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1],array[j]
                flag = True
            
        if not flag :          
            break

    return array    
    

    
    
    
assert bubble_sort( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 

assert bubble_sort_flag( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 