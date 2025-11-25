def insert_sort(array):
    for i,n in enumerate(array):
        index = i 
        while index > 0 and n < array[index - 1]
            array [index] = array [index - 1]
            index -= 1
        array[index]  = n       
    return array  

assert insert_sort( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 
    


