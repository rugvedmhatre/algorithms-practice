"""

https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from 
it. 


Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
 

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

"""

def validPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            subStrL, subStrR = s[l+1:r+1], s[l:r]
            return subStrL == subStrL[::-1] or subStrR == subStrR[::-1]
        l += 1
        r -= 1

    return True

if __name__ == "__main__":
    # Test Case 1
    s = "aba"
    print(validPalindrome(s)) # True

    # Test Case 2
    s = "abca"
    print(validPalindrome(s)) # True

    # Test Case 3
    s = "abc"
    print(validPalindrome(s)) # False