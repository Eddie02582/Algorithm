public class Sort {
    public static void main(String[] args) {

        Sort sort = new Sort();
        sort.bubble_sort(new int[] { 18, 16, 13, 19, 15, 14, 17 });
    }

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
}