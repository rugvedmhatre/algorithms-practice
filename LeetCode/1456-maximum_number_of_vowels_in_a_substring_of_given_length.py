"""

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string s and an integer k, return the maximum number of vowel letters in any 
substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length

"""

def maxVowels(s: str, k: int) -> int:
    vowels = 'aeiou'
    currentVowelsCount = 0

    for char in s[:k]:
        if char in vowels:
            currentVowelsCount += 1
    
    maxVowelsCount = currentVowelsCount

    i = 0
    
    while i < (len(s) - k):
        currentVowelsCount = currentVowelsCount - (s[i] in vowels) + (s[i + k] in vowels)
        maxVowelsCount = max(currentVowelsCount, maxVowelsCount)
        i += 1
    
    return maxVowelsCount

if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    print(maxVowels(s, k))