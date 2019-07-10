# Select Sort

<ul>
    <li>從未排序的數列中找到最小的元素。</li>
    <li>將此元素與已排序部分的尾端元素進行交換</li>
    <li>重複進行1,2的動作，直到未排序數列全部處理完成。</li>
</ul>

動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>


## Python




``` python

def select_sort(array):    
    for i in range(0,len(array)):        
        index = i
        for j in range(i,len(array)):
            if array[j] < array[index]:
                index = j                
        array[i],array[index] = array[index],array[i]   
    return array
```


## C sharp

``` csharp
public int[] select_sort(int[] arr)
{
    int index = 0 ;
    int temp = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        index = i;
        for (int j = i; j < arr.Length ; j++)
        {
            if (arr[j] < arr[index])
            {
                index = j;                   
            }
        }
        if (index != i)
        {
            temp = arr[index];
            arr[index] = arr[i];
            arr[i] = temp;
        }
        
    }
    return arr;
}
```

## Java

``` Java
public int[] select_sort(int[] arr)
{       
    int index = 0 ;
    int temp = 0 ;   
    for (int i = 0; i < arr.length; i++)
    {
        index = i ;
        for (int j = i; j < arr.length  ; j++)
        {                    
            if (arr[j] < arr[index])
            {
                index = j ;                  
            }
        }
        if (index != i)
        {   
            temp = arr[i] ;
            arr[i] = arr[index];
            arr[index]= temp;  
        }  

    }
    return arr;
}

```









