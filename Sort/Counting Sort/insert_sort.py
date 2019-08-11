def insert_sort(array):
    count = 0 
    for i in range(1,len(array)): 
        n = array[i]
        j = i - 1

        while j >= 0 and n < array[j]:            
            array [j + 1] = array[j]
            j -= 1         
        array [j + 1] = n         
    return array   



assert insert_sort( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 
    


