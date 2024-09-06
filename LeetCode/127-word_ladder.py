"""

https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord
using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord
  does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary 
wordList, return the number of words in the shortest 
transformation sequence from beginWord to endWord, or 0 if no 
such sequence exists.
 

Example 1:
Input: 
beginWord = "hit", 
endWord = "cog", 
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is
"hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: 
beginWord = "hit", 
endWord = "cog", 
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore 
there is no valid transformation sequence.
 

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase 
  English letters.
- beginWord != endWord
- All the words in wordList are unique.

"""

from collections import defaultdict, deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0
    
    adjacent = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + '*' + word[j+1:]
            adjacent[pattern].append(word)
    
    visited = set([beginWord])
    q = deque([beginWord])

    result = 1

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return result
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                for adjacentWord in adjacent[pattern]:
                    if adjacentWord not in visited:
                        visited.add(adjacentWord)
                        q.append(adjacentWord)
        result += 1
    
    return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(ladderLength(beginWord, endWord, wordList))