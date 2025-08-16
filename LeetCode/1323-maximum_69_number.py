"""

https://leetcode.com/problems/maximum-69-number/

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:
- 1 <= num <= 10^4
- num consists of only 6 and 9 digits.

"""

def maximum69Number (num: int) -> int:
    stringnum = str(num)

    for i in range(len(stringnum)):
        if stringnum[i] == '6':
            return int(stringnum[:i] + '9' + stringnum[i+1:])
    
    return num

if __name__ == "__main__":
    # Test Case 1
    num = 9669
    print(maximum69Number(num))

    # Test Case 2
    num = 9996
    print(maximum69Number(num))

    # Test Case 3
    num = 9999
    print(maximum69Number(num))