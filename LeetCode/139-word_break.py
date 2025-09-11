"""

https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
 

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

"""

from collections import deque

def wordBreak(s: str, wordDict: list[str]) -> bool:
    q = deque([s])
    visited = set()

    while q:
        word = q.popleft()

        if word in visited:
            continue
        else:
            if word == "":
                return True
            
            visited.add(word)

            for val in wordDict:
                if word.startswith(val):
                    q.append(word[len(val):])
    
    return False

# Dynamic Programming Approach
def wordBreakDP(s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                dp[i] = dp[i + len(w)]

            if dp[i]:
                break
    
    return dp[0]

if __name__ == "__main__":
    # Test Case 1
    s = "leetcode"
    wordDict = ["leet","code"]
    print(wordBreak(s, wordDict))
    print(wordBreakDP(s, wordDict))

    # Test Case 2
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(wordBreak(s, wordDict))
    print(wordBreakDP(s, wordDict))

    # Test Case 3
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(wordBreak(s, wordDict))
    print(wordBreakDP(s, wordDict))