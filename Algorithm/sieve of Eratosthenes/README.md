# sieve of Eratosthenes

這是一種簡單且歷史悠久的篩法，用來找出一定範圍內所有的質數。</br>

所使用的原理是從2開始，將每個質數的各個倍數，標記成合數。一個質數的各個倍數，是一個差為此質數本身的等差數列。此為這個篩法和試除法不同的關鍵之處，後者是以質數來測試每個待測數能否被整除。






## Algorithm

虛擬碼來表示
``` 
Input: an integer n > 1
 
Let A be an array of Boolean values, indexed by integers 2 to n,
initially all set to true.
 
 for i = 2, 3, 4, ..., not exceeding 
  
    
    {\displaystyle {\sqrt {n}}}
  
{\displaystyle {\sqrt {n}}}:
  if A[i] is true:
    for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n :
      A[j] := false
 
Output: all i such that A[i] is true.
```


## 程式代碼

``` python
def Primes(n) :
    IsPrime = 0, [True] * n
    for i in range(2, n):
        if IsPrime[i]:            
            for j in range(i*i, n, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]
```











