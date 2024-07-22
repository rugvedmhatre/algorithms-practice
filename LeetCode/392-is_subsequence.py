"""

https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the 
remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.

"""

def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print("Result :", isSubsequence(s, t))