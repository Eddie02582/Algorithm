class Sort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        print("left = " + str(left))
        right = self.mergeSort(arr[mid:])
        print("right = " + str(right))
        return self.mergeSortedArray(left, right)

    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        sortedArray = []
        l ,r = 0 , 0 
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        sortedArray += A[l:]
        sortedArray += B[r:]

        return sortedArray


        
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort = Sort()
print (unsortedArray)
print(merge_sort.mergeSort(unsortedArray))