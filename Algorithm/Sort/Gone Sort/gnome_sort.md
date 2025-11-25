# Insert Sort


## Algorithm 
<ul>
    <li>從未排序數列取出一元素</li>
    <li>由後往前和已排序數列元素比較，直到遇到不大於自己的元素並插入此元素之後；若都沒有則插入在最前面</li>
    <li>重複進行1,2的動作，直到未排序數列全部處理完成。</li>
</ul>

動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>


## Python




``` python

def insert_sort(array):
    count = 0 
    for i in range(1,len(array)): 
        n = array[i]
        j = i - 1

        while j >= 0 and n < array[j]:            
            array [j + 1] = array[j]
            j = j -1        
        array [j + 1] = n         
    return array   
```


## C sharp

``` csharp
class Sort
{
    public int[] select_sort(int[] arr)
    {
        int index = 0 ;
        int temp = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            j = i -1 ;
            int n = array[i]
            while j >= 0 and array[j] > n:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = n
        }
        return arr;
    }       
}
```










