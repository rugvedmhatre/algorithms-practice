"""

https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data 
structure used to efficiently store and retrieve keys in a 
dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the 
  trie.
- boolean search(String word) Returns true if the string word 
  is in the trie (i.e., was inserted before), and false 
  otherwise.
- boolean startsWith(String prefix) Returns true if there is a
  previously inserted string word that has the prefix prefix, 
  and false otherwise.
 

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, 
  search, and startsWith.

"""

class TrieNode:
    
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))