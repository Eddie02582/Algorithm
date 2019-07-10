
     
def bubble_sort(array):
    count = 0
    for i in range(0,len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j + 1] = array[j + 1],array[j]
            count += 1
    print (count)
    return array
    
def bubble_sort_flag(array):
    count = 0
    for i in range(0,len(array)):
        flag = False 
        for j in range(0,len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1],array[j]
                flag = True
            count += 1
        if not flag :
            print (count)
            return array
    print (count)
    return array    
    

    
    
    
assert bubble_sort( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 

assert bubble_sort_flag( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 