def gnome_sort(array):
    index = 0 
    
    while index < len(array):
        if index == 0:
            index += 1
        if array[index] < array[index -1]:
            array [index],array[index -1] = array [index - 1],array[index]
            index -= 1
        else:
            index += 1   
    return array   



assert gnome_sort( [18, 16, 13, 19, 15, 14, 17] ) ==  [13, 14, 15, 16, 17, 18, 19] 
    


