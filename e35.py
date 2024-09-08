import math

# Sieve of erastothenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n : int):
    if n < 1:
        return
    primes = [True for c in range(n + 1)] 
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            j = i**2
            while j <= n:
                primes[j] = False
                j += i
    
    return [k for k in range(2, n) if primes[k]]

primes = set(sieve(1000000))

def isCircular(n : int):
    strint = str(n)
    for i in range(len(strint)):
        if int(strint[i:] + strint[0:i]) not in primes:
            return False
    
    return True
numCirc = 0
for i in list(primes):
    if isCircular(i):
        numCirc += 1
print(numCirc)

