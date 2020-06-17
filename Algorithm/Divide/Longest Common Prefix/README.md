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

這題為Leetcode 14.<a href = "https://leetcode.com/problems/longest-common-prefix/">Longest Common Prefix</a><br>
解法可以<a href = "https://github.com/Eddie02582/Leetcode/blob/master/014_Longest%20Common%20Prefix.md">參考</a><br>使用排序比較陣列頭尾字串即可<br>
這邊主要使用分治法解


## 分析

類似合併排序法,一次比較太多的話,有點難比較所以縮小問題,每次只比較2個

圖片取自於geeksforgeeks
<img src = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/longest_common_prefix6.jpg"></img>



## Code

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]          
        
        def helper(str1,str2):
            p = 0
            s = ""
            while p < len(str1) and  p <len(str2):
                if str1[p] != str2[p]:
                    break              
                s += str1[p]
                p += 1            
            return s
                
        
        mid = len(strs)//2
        left = strs[:mid]
        right = strs[mid:]
        left = self.longestCommonPrefix(left)
        right = self.longestCommonPrefix(right)
        s = helper(left,right)
        return s
        

sol = Solution()
input = ["geeksforgeeks", "geeks", "geek", "geezer"]
sol.longestCommonPrefix(input)

```