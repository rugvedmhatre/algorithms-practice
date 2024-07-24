"""

https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagramGroups = defaultdict(list)
    
    for word in strs:
        sortedWord = ''.join(sorted(word))
        anagramGroups[sortedWord].append(word)
    
    return anagramGroups.values()

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))