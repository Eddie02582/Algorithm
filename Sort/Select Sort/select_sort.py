def select_sort(array):    
    for i in range(0,len(array)):        
        index = i
        for j in range(i,len(array)):
            if array[j] < array[index]:
                index = j                
        array[i],array[index] = array[index],array[i]   
    return array
    


    
    
    
assert select_sort( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 

