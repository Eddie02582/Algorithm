class Sort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])  
        return self.mergeSortedArray(left, right)

    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, left, right):
        sortedArray = []
        l ,r = 0 , 0 
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                sortedArray.append(left[l])
                l += 1
            else:
                sortedArray.append(right[r])
                r += 1
        sortedArray += left[l:]
        sortedArray += right[r:]

        return sortedArray

def mergeSort(arr):          
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]   
    mergeSort(left)    
    mergeSort(right)       

    i,j =0,0
    while i <len(left) and j <len(right):
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1
        
    while i < len(left): 
        arr[i + j] = left[i]
        i+= 1      
      
    while j < len(right): 
        arr[i + j] = right[j]
        j+= 1
       
        
    return arr  


        
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort = Sort()
print (unsortedArray)
print(merge_sort.mergeSort(unsortedArray))