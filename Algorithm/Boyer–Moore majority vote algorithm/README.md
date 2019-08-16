# Boyer–Moore majority vote algorithm

在給定未排序數組,找出出現最多次的元素




## Algorithm

``` python 

    candidate = None
    count = 0
    
    for value in nums: 
        if count == 0: 
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
             count -= 1
    return candidate
```


## 範例

Majority Element (leetcode 169) </br>
給定陣列siez n 找到元素出現次數大於[ n/2 ],題目說假設必定存在</br>

``` python
    def majorityElement(nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num            
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate        
        
```











