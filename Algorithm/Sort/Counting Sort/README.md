# Counting Sort

## 特點
<ul>
    <li>非in place </li>
    <li>須知道值範圍</li>    
</ul>

## Algorithm 

<ul>
    <li>建立一個陣列計數</li>
    <li>迴圈建立新陣列</li>    
</ul>



動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>


## Python




``` python
def counting(array,max_value):
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
```

自己找範圍

``` python
def counting(array):
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
```

在同値的情況下,想按照原本順序排

``` python
def counting(array):
    # find Max and Min
    maxValue ,minValue= array[0],array[0]    
    for n in array:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    
    d = maxValue - min_value
    
    countArray = [0] * (d + 1)
    
    #count element numbers
    
    for n in array:
       countArray[n - min_value] += 1  
       
    for i in range(1,len(counts)):
       countArray[i] += countArray[i - 1]          
       
    sortedArray = []     
    
    for i in range(len(array) - 1, - 1,-1): 
        sortedArray[countArray[array[i]- min] - 1] = array[i]
        countArray[array[i]-min] -= 1
    return sortedArray
```






























