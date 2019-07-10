# Bubble Sort

<ul>
    <li>比較相鄰的兩個元素，若前面的元素較大就進行交換。</li>
    <li>重複進行1的動作直到最後面，最後一個元素將會是最大值。</li>
    <li>重複進行1,2的動作，每次比較到上一輪的最後一個元素。</li>
    <li>重複進行以上動作直到沒有元素需要比較</li>
</ul>

動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>


## Python




``` python

def bubble_sort(arr):
    for i in range (len(arr)):
        for j in range (len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
    return arr
```

新增一個flag

``` python
def bubble_sort_flag(arr):
    for i in range (len(arr)):
        flag = False
        for j in range (len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
                flag = True
        if not flag:
            return array
    return arr
```

## C sharp

``` csharp
public int[] bubble_sort(int[] arr)
{
    int temp = 0;
    bool bSwap = false;
    for (int i = 0; i < arr.Length; i++)
    {
        bSwap = false;
        for (int j = 0; j < arr.Length - i - 1 ; j++)
        {                    
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                bSwap = true;
            }
        }
        if (!bSwap)
            return arr;

    }
    return arr;
 }
```

## Java

``` java
public int[] bubble_sort(int[] arr)
{
    Integer temp = 0;
    Boolean bSwap = false ;
    for (int i = 0; i < arr.length; i++)
    {
        bSwap = false;
        for (int j = 0; j < arr.length - i - 1 ; j++)
        {                    
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                bSwap = true;
            }
        }
        if (!bSwap)
            return arr;

    }
    return arr;
}

```









