"""

https://neetcode.io/problems/foreign-dictionary/

There is a foreign language which uses the latin alphabet, but
the order among letters is not "a", "b", "c" ... "z" as in 
English.

You receive a list of non-empty strings words from the 
dictionary, where the words are sorted lexicographically based
on the rules of this new language.

Derive the order of letters in this language. If the order is
invalid, return an empty string. If there are multiple valid
order of letters, return any of them.

A string a is lexicographically smaller than a string b if 
either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and 
a.length < b.length.


Example 1:
Input: ["z","o"]
Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:
Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"
Explanation:
from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"


Constraints:
- The input words will contain characters only from lowercase 
  'a' to 'z'.
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100

"""

def foreignDictionary(words: list[str]) -> str:
    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    
    visited = {}
    result = []

    def dfs(c):
        if c in visited:
            return visited[c]
        
        visited[c] = True

        for nei in adj[c]:
            if dfs(nei):
                return True
        
        visited[c] = False
        result.append(c)
    
    for c in adj:
        if dfs(c):
            return ""
    
    result.reverse()

    return "".join(result)

if __name__ == '__main__':
    words = ["hrn","hrf","er","enn","rfnn"]
    print(foreignDictionary(words))