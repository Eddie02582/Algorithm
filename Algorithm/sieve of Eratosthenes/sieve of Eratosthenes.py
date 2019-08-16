def Primes(n) :
    IsPrime = 0, [True] * n
    for i in range(2, n):
        if IsPrime[i]:            
            for j in range(i*i, n, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]

    
