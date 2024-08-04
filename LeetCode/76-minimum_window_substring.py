"""

https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) 
is included in the window. If there is no such substring, return the empty 
string "".

The testcases will be generated such that the answer is unique.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?

"""

from collections import defaultdict

def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    
    counts = defaultdict(int)
    for char in t:
        counts[char] += 1
    
    have = 0
    need = len(counts)

    window = defaultdict(int)
    left = 0

    result = [-1, -1]
    resultLength = float('inf')

    for right in range(len(s)):
        c = s[right]
        window[c] += 1

        if c in counts and window[c] == counts[c]:
            have += 1
        
        while have == need:
            if (right - left + 1) < resultLength:
                result = [left, right]
                resultLength = right - left + 1

            window[s[left]] -= 1
            if s[left] in counts and window[s[left]] < counts[s[left]]:
                have -= 1
            
            left += 1
        
    return s[result[0]:result[1] + 1] if resultLength != float('inf') else ""

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))