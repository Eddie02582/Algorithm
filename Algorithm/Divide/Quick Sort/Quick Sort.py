class Sort:
    def quicksort(self,array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

        
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
quicksort = Sort()
print (unsortedArray)
print(quicksort.quicksort(unsortedArray))