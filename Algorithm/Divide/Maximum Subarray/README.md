# Longest Common Prefix

          
## 題目
```
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"
    
 Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
Explanation: There is no common prefix among the input strings.
```

這題為Leetcode 14.<a href = "https://leetcode.com/problems/maximum-subarray//">Maximum Subarray</a><br>
解法可以<a href = "https://github.com/Eddie02582/Leetcode/blob/master/053_Maximum%20Subarray.md">參考</a><br>使用動態規劃<br>
這邊主要使用分治法解


## 分析
<ol>
    <li>Divide the given array in two halves</li>
    <li>Return the maximum of following three
        <ol type="a">
            <li>Maximum subarray sum in left half (Make a recursive call)</li>
            <li>Maximum subarray sum in right half (Make a recursive call)</li>
            <li>Maximum subarray sum such that the subarray</li>
        </ol>    
    </li>
</ol>

圖片取自於geeksforgeeks
<img src = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/longest_common_prefix6.jpg"></img>



## Code

```python
# A Divide and Conquer based program 
# for maximum subarray sum problem 
  
# Find the maximum possible sum in 
# arr[] auch that arr[m] is part of it 
def maxCrossingSum(arr, l, m, h) : 
      
    # Include elements on left of mid. 
    sm = 0; left_sum = -10000
      
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
      
      
    # Include elements on right of mid 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 
          
        if (sm > right_sum) : 
            right_sum = sm 
      
  
    # Return sum of elements on left and right of mid 
    # returning only left_sum + right_sum will fail for [-2, 1] 
    return max(left_sum + right_sum, left_sum, right_sum) 
  
  
# Returns sum of maxium sum subarray in aa[l..h] 
def maxSubArraySum(arr, l, h) : 
      
    # Base Case: Only one element 
    if (l == h) : 
        return arr[l] 
  
    # Find middle point 
    m = (l + h) // 2
  
    # Return maximum of following three possible cases 
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the  
    #     subarray crosses the midpoint  
    return max(maxSubArraySum(arr, l, m), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h)) 
              
  
# Driver Code 
arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr) 
  
max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 
  
```