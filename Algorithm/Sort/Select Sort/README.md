# Select Sort

## Algorithm 
<ul>
    <li>從未排序的數列中找到最小的元素。</li>
    <li>將此元素與已排序部分的尾端元素進行交換</li>
    <li>重複進行1,2的動作，直到未排序數列全部處理完成。</li>
</ul>

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







