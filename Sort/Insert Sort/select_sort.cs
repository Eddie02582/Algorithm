class Sort
{
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
}