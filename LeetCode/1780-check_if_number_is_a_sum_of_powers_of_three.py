"""

https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of 
three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3^x.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false
 

Constraints:
- 1 <= n <= 10^7

"""

def checkPowersOfThree(n: int) -> bool:
    powersOfThree = [1]
    val = 3
    while val <= n:
        powersOfThree.append(val)
        val = val * 3

    curr_sum = 0

    for i in range(len(powersOfThree) - 1, -1, -1):
        if curr_sum + powersOfThree[i] <= n:
            curr_sum += powersOfThree[i]
            if curr_sum == n:
                return True
    
    return False


if __name__ == "__main__":
    # Test Case 1
    print(checkPowersOfThree(12))
    
    # Test Case 2
    print(checkPowersOfThree(91))
    
    # Test Case 3
    print(checkPowersOfThree(21))