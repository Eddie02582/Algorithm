# Merge Sort 

## Algorithm 
將兩個有序對數組合併成一個更大的有序數組


動畫可以參考<a href ="https://visualgo.net/en/sorting">visualgo </a>

步驟
<ul>
    <li>將陣列拆程左邊和右邊</li>
    <li>左邊呼叫mergeSort</li>
    <li>右邊呼叫mergeSort</li>
    <li>合併</li>
</ul>

圖片取自於geeksforgeeks
<img src = "https://www.geeksforgeeks.org/wp-content/uploads/Merge-Sort-Tutorial.png"></img>


## Example 


## Python


``` python
def mergeSort(arr):          
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]   
    mergeSort(left)    
    mergeSort(right)       

    i,j =0,0
    while i <len(left) and j <len(right):
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1
        
    while i < len(left): 
        arr[i + j] = left[i]
        i+= 1      
      
    while j < len(right): 
        arr[i + j] = right[j]
        j+= 1
       
        
    return arr  

```

## C++
```c++
#include <string>
#include <iostream>

using namespace std ; 
void mergeSort (int arr[],int front,int end);
void merge(int arr[], int front, int mid, int end);
void printArray (int arr[],int size);

int main()
{
    int arr[] = {6, 5, 12, 10, 9, 1};
    int size = sizeof(arr) / sizeof(arr[0]); 
    mergeSort (arr,0,size - 1);
    printArray(arr,size);
}

void printArray(int arr[],int size){   
    for (int i = 0;i<size;i++){
        cout << *(arr++) << endl;
    }
}

void mergeSort (int arr[],int front,int end){
    if (front < end)
    {
        int mid = front  + (end  - front)/2;
        mergeSort(arr,front,mid);
        mergeSort(arr,mid + 1,end);
        merge(arr,front,mid,end);
    }
}

void merge(int arr[], int front, int mid, int end) { 
    int n1 = mid - front + 1;
    int n2 = end  - mid;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[front + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid+ 1 + j];

    //merge
    int i, j, k;
    i = 0;
    j = 0;
    k = front;
    while (i < n1 && j < n2){
        if(L[i] < R[j]){
            arr[k++] = L[i++];           
        }
        else{
            arr[k++] = R[j++];      
        }
  
    }
    while (i < n1 ){
        arr[k++] = L[i++];       
    } 
    while (j < n2 ){
        arr[k++] = R[j++];  
    } 
}
```







