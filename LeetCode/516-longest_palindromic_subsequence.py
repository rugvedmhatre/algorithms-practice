"""

https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no 
elements without changing the order of the remaining elements.
 

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.

"""

def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    rev_s = s[::-1]
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            if s[i] == rev_s[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    return dp[n][n]

if __name__ == "__main__":
    # Test Case 1
    s = "bbbab"
    print(longestPalindromeSubseq(s))

    # Test Case 2
    s = "cbbd"
    print(longestPalindromeSubseq(s))