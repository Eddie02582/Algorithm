public class Sort {
    public static void main(String[] args) {

        Sort sort = new Sort();
        sort.select_sort(new int[] { 18, 16, 13, 19, 15, 14, 17 });
    }

    public int[] select_sort(int[] arr)
    {       
        int index = 0 ;
        int temp = 0 ;   
        for (int i = 0; i < arr.length - 1; i++)
        {
            index = i ;
            for (int j = i + 1; j < arr.length  ; j++)
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
}