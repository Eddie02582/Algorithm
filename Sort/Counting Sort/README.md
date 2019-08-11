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










