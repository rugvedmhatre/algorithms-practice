"""

https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

 

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form 
"AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

"""

from collections import defaultdict

# # Method 1: O(n) time | O(n) space
# def characterReplacement(s: str, k: int) -> int:
#     count = defaultdict(int)
#     result = 0

#     left = 0
    
#     for right in range(len(s)):
#         count[s[right]] += 1
    
#         while (right - left + 1) - max(count.values()) > k:
#             count[s[left]] -= 1
#             left += 1
        
#         result = max(result, right - left + 1)
    
#     return result

# Method 2: O(n) time [faster] | O(n) space
def characterReplacement(s: str, k: int) -> int:
    count = defaultdict(int)
    result = 0

    left = 0
    maxFreq = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        maxFreq = max(maxFreq, count[s[right]])
    
        while (right - left + 1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1
        
        result = max(result, right - left + 1)
    
    return result

if __name__ == '__main__':
    s = "ABAB"
    k = 2
    print(characterReplacement(s, k))