"""

https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the 
substring of s2.


Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.

"""

def checkInclusion(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)

    if n2 < n1:
        return False
    
    s1Counts = [0] * 26
    s2Counts = [0] * 26
    
    for i in range(n1):
        s1Counts[ord(s1[i]) - ord('a')] += 1
        s2Counts[ord(s2[i]) - ord('a')] += 1
    
    matches = 0

    for i in range(26):
        matches += (1 if s1Counts[i] == s2Counts[i] else 0)
    
    left = 0
    for right in range(n1, n2):
        if matches == 26:
            return True
        
        index = ord(s2[right]) - ord('a')
        s2Counts[index] += 1
        if s1Counts[index] == s2Counts[index]:
            matches += 1
        elif s1Counts[index] + 1 == s2Counts[index]:
            matches -= 1
        
        index = ord(s2[left]) - ord('a')
        s2Counts[index] -= 1
        if s1Counts[index] == s2Counts[index]:
            matches += 1
        elif s1Counts[index] - 1 == s2Counts[index]:
            matches -= 1
        
        left += 1
    
    return matches == 26

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))