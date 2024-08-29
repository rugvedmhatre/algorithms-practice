"""

https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the 
partition is a palindrome. Return all possible palindrome 
partitioning of s.
 

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.

"""

def partition(s: str) -> list[list[str]]:
    result = []
    partition = []

    def dfs(i):
        if i >= len(s):
            result.append(partition.copy())
            return
        
        for j in range(i, len(s)):
            if isPalindrome(s, i, j):
                partition.append(s[i:j+1])
                dfs(j + 1)
                partition.pop()
        
    dfs(0)
    return result

def isPalindrome(s: str, l: int, r: int):
    while l < r:
        if s[l] != s[r]:
            return False
        l = l + 1
        r = r - 1
    
    return True

if __name__ == '__main__':
    s = "aab"
    print(partition(s))