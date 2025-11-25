class Sort(object):
    def quicksort(self,array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
        return self.quicksort(less) + [pivot] + self.quicksort(greater)
        
        

    def quickSort_twoPointer(self,arr,startIndex,endIndex):            
        def partition(arr, startIndex,endIndex):  
            pivot,left,right = arr[startIndex],startIndex,endIndex
            while left != right:
                while left < right and arr[right] > pivot:
                    right -= 1
                while left < right and arr[left] <= pivot:
                    left += 1
                if left < right:
                    arr[left],arr[right] = arr[right],arr[left]
            
            arr[startIndex] = arr[left]
            arr[left] = pivot
            return left
            
        if startIndex >= endIndex:
            return 
        pivotIndex = partition(arr, startIndex, endIndex)
        self.quickSort_twoPointer(arr, startIndex, pivotIndex - 1)
        self.quickSort_twoPointer(arr, pivotIndex + 1, endIndex)           
            

        
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
quicksort = Sort()
print (unsortedArray)
print(quicksort.quicksort(unsortedArray))
quicksort.quickSort_twoPointer(unsortedArray,0,len(unsortedArray) - 1)
print (unsortedArray)
