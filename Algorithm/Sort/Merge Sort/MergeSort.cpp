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