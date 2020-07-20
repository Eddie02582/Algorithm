class Sort(object):
    def sift_down(self,array,parentIndex,length):
        childIndex = 2 * parentIndex + 1
        temp = array[parentIndex]
        while childIndex < length:
            if childIndex + 1 < length and array[childIndex] < array[childIndex + 1]:
                childIndex += 1
            if temp >= array[childIndex]:
                break
            
            array[parentIndex] = array[childIndex]
            parentIndex = childIndex
            childIndex = 2 * parentIndex + 1
        array[parentIndex] = temp    



    def heapSort(self,array):
        start = (len(array) - 2 ) //2 
        for i in range(start,-1,-1):
            self.sift_down(array,i,len(array))
        
        for end in range(len(array) - 1, 0, -1):
            array[0], array[end] = array[end], array[0]
            self.sift_down(array,0, end)
        

       
            

        
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
sort = Sort()
sort.heapSort(unsortedArray)
print (unsortedArray)
