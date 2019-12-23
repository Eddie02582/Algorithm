# Merge Sort 

## Algorithm 
將兩個有序對數組合併成一個更大的有序數組


動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>


## Example 
假設陣列範圍0-9，陣列為 [1, 4, 1, 2, 7, 5, 2]

## Python


``` python
def counting_sort(array,max_value):
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



## Example 
陣列為 [100, 93, 97, 92, 96, 99, 92, 89, 93, 97, 90, 94, 92, 95] </br>
此時不知道範圍須先找出最大最小值</br>







