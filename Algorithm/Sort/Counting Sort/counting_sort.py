
def counting_sort_range(array,max_value):
    counts = [0] * max_value
    
    for n in array:
       counts[n] += 1 
    result = []
    for i,count in enumerate(counts):
        j = 0 
        while j < count:
            result.append(i)
            j += 1   
    return result

def counting_sort_(array):
    max_value ,min_value= array[0],array[0]
    
    for n in array:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
            
    k = max_value - min_value + 1
    counts = [0] * k
    
    for n in array:
       counts[n - min_value] += 1 
    result = []
  
    for i in range(len(counts)): 
        while counts[i] > 0:
            result.append(i + min_value)
            counts[i] -= 1   
    return result
    

assert counting_sort_range( [1, 4, 1, 2, 7, 5, 2],10 ) ==  [1, 1, 2, 2, 4, 5, 7] 

assert counting_sort_range( [18, 16, 13, 19, 15, 14, 17],20 ) ==  [13, 14, 15, 16, 17, 18, 19] 
    
assert counting_sort_( [100, 93, 97, 92, 96, 99, 92, 89, 93, 97, 90, 94, 92, 95] ) ==  [89, 90, 92, 92, 92, 93, 93, 94, 95, 96, 97, 97, 99, 100]

