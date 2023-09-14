#!/usr/bin/python

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# accumulate sums of primes
sum = 0
primeCount = 0
for i in range (2,1000000):
    if isPrime(i):
        primeCount += 1
        if primeCount > 1000: # stop at 1000
            break
        sum += i

# print sum
print sum
