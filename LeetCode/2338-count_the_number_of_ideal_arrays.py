"""

https://leetcode.com/problems/count-the-number-of-ideal-arrays/

You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
- Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
- Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return 
it modulo 109 + 7.


Example 1:
Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.

Example 2:
Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

Constraints:
- 2 <= n <= 10^4
- 1 <= maxValue <= 10^4

"""

from collections import Counter
from math import comb

def idealArrays(n: int, maxValue: int) -> int:
    MOD = 1_000_000_007
    total_ways = maxValue
    frequency_map = {num: 1 for num in range(1, maxValue + 1)}
    
    for array_size in range(1, n): 
        new_frequency = Counter()
        for base_value in frequency_map: 
            for multiplier in range(2, maxValue // base_value + 1): 
                combinations = comb(n - 1, array_size)
                total_ways += combinations * frequency_map[base_value]
                new_frequency[multiplier * base_value] += frequency_map[base_value]
        frequency_map = new_frequency
        total_ways %= MOD
    
    return total_ways

if __name__ == "__main__":
    # Test Case 1
    n = 2
    maxValue = 5
    print(idealArrays(n, maxValue))

    # Test Case 2
    n = 5
    maxValue = 3
    print(idealArrays(n, maxValue))