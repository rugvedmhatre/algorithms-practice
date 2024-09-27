"""

https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

"""

def longestPalindrome(s: str) -> str:
    result = ""
    result_len = 0

    for i in range(len(s)):
        # checking odd length palindromes
        l, r = i, i
        while l >= 0 and r<len(s) and s[l] == s[r]:
            if (r - l + 1) > result_len:
                result = s[l:r+1]
                result_len = r-l+1
            l -= 1
            r += 1

        # checking even length palindromes
        l, r = i, i+1
        while l >= 0 and r<len(s) and s[l] == s[r]:
            if (r - l + 1) > result_len:
                result = s[l:r+1]
                result_len = r-l+1
            l -= 1
            r += 1
    
    return result

if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))