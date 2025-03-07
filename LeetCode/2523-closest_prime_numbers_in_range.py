"""

https://leetcode.com/problems/closest-prime-numbers-in-range/

Given two positive integers left and right, find the two integers num1 and num2 such that:
- left <= num1 < num2 <= right
- Both num1 and num2 are prime numbers.
- num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these 
conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].


Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:
Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be
satisfied.


Constraints:
- 1 <= left <= right <= 10^6

"""

def sieveOfEratosthenes(left, n):
    primes = []
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    
    p = 2
    
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(left, n+1):
        if prime[p]:
            primes.append(p)
    
    return primes

def closestPrimes(left: int, right: int) -> list[int]:
    primes = sieveOfEratosthenes(left, right)
    
    if len(primes) < 2:
        return [-1, -1]
    
    result = [-1, -1]
    minDistance = right - left + 1

    for i in range(len(primes) - 1, 0, -1):
        currentDist = primes[i] - primes[i-1]
        if currentDist <= minDistance:
            minDistance = currentDist
            result[0] = primes[i-1]
            result[1] = primes[i]
    
    return result

if __name__ == '__main__':
    # Test case 1
    left = 10
    right = 19
    print(closestPrimes(left, right)) # Output: [11,13]

    # Test case 2
    left = 4
    right = 6
    print(closestPrimes(left, right)) # Output: [-1,-1]

    # Test case 3
    left = 1
    right = 100000
    print(closestPrimes(left, right)) # Output: [2, 3]