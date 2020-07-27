# 如何求GCD和LCD




## GCD 最大公因數

### 暴力法
``` python
# m > n 
def gcd(m, n):
    if m % n == 0:
        return n
    
    for i in range(n//2 ,1, - 1):
        if n % i == 0 and m % i == 0:
            return i


```

### 輾轉相除法
``` python
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)
```

### 更相減損術
``` python
def gcd(m, n):
    return m if n == 0 else gcd(n, m － n)
```

### 進階更相減損術
