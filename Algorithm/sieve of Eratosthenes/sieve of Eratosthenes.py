def Primes(n) :
    IsPrime = [True] * (n + 1)
    IsPrime[0] = False
    IsPrime[1] = False
    primes = []
    for i in range(2, n + 1):
        if IsPrime[i]:            
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
            primes.append(i)
    return primes

