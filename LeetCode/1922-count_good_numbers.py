"""

https://leetcode.com/problems/count-good-numbers/

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd 
indices are prime (2, 3, 5, or 7).
- For example, "2582" is good because the digits (2 and 8) at even positions are even and the 
  digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even
  index but is not even.

Given an integer n, return the total number of good digit strings of length n. Since the answer 
may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros. 


Example 1:
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Example 2:
Input: n = 4
Output: 400

Example 3:
Input: n = 50
Output: 564908303
 

Constraints:
- 1 <= n <= 10^15

"""

def countGoodNumbers(n: int) -> int:
    MOD = 10**9 + 7

    even_pos = (n + 1) // 2
    odd_pos = n // 2

    def binary_exp(base, power):
        result = 1
        base %= MOD

        while power > 0:
            if power % 2 == 1:
                result = (result * base) % MOD
            base = (base * base) % MOD
            power = power // 2
        
        return result

    even_ways = binary_exp(5, even_pos)
    odd_ways = binary_exp(4, odd_pos)

    return (even_ways * odd_ways) % MOD

if __name__ == "__main__":
    # Test Case 1
    n = 1
    print(countGoodNumbers(n))

    # Test Case 2
    n = 4
    print(countGoodNumbers(n))
    
    # Test Case 3
    n = 50
    print(countGoodNumbers(n))