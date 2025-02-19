"""

https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.

"""

def findAnagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    
    sCount, pCount = {}, {}

    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)
    
    if pCount == sCount:
        result = [0]
    else:
        result = []
    
    left_ptr = 0
    
    for right_ptr in range(len(p), len(s)):
        sCount[s[right_ptr]] = 1 + sCount.get(s[right_ptr], 0)
        sCount[s[left_ptr]] -= 1

        if sCount[s[left_ptr]] == 0:
            sCount.pop(s[left_ptr])
        
        left_ptr += 1
        
        if sCount == pCount:
            result.append(left_ptr)
        
    return result

if __name__ == "__main__":
    # Test Case 1
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p)) # Output: [0, 6]

    # Test Case 2
    s = "abab"
    p = "ab"
    print(findAnagrams(s, p)) # Output: [0, 1, 2]