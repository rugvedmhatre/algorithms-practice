"""

https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

"""

def countSubstrings(s: str) -> int:
    result = 0
    for i in range(len(s)):
        result += countPalindromes(s, i, i)
        result += countPalindromes(s, i, i+1)
    return result
        
def countPalindromes(s: str, l: int, r: int) -> int:
    result = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        result += 1
        l -= 1
        r += 1
    return result

if __name__ == '__main__':
    s = "abc"
    print(countSubstrings(s))