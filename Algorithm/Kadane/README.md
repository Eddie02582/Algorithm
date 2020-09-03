# Kadane's Algorithm

Kadane算法掃描一次整個數列的所有數值，在每一個掃描點計算以該點數值為結束點的子數列的最大和（正數和）。
該子數列由兩部分組成：以前一個位置為結束點的最大子數列、該位置的數值。






## Algorithm
已知A[:i]的max sum，那麼A[:i+1]的max sum必定包含或不包含A[:i]的prefix。<br>
對每個A內的元素，求那個位置所能達到的sum最大值，令其為max_ending_here。<br
包含prefix的情況下，max_ending_here為prefix加上當前元素a；不包含prefix的情況下，max_ending_here為0。<br
（不包含的情況，表示max_ending_here + a小於0，就直接捨棄掉prefix和當前元素a，令max_ending_here歸零，從下一個元素開始計算）<br



## 程式代碼

``` python
def max_slice(A):
    max_ending_here = max_so_far = 0
    for a in A:
        max_ending_here = max(0, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```











