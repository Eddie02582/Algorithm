class Sort
{
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

       
}