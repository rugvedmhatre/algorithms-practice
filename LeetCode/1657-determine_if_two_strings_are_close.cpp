/*

https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:
- Operation 1: Swap any two existing characters.
  - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, 
  and do the same with the other character.
  - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
 

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.

*/

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

bool closeStrings(string word1, string word2) {
    vector<int> counter1(26, 0);
    vector<int> counter2(26, 0);

    for (char letter : word1) {
        counter1[letter - 'a']++;
    }

    for (char letter : word2) {
        counter2[letter - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if ((counter1[i] == 0 && counter2[i] != 0) || (counter1[i] != 0 && counter2[i] == 0)) {
            return false;
        }
    }

    sort(counter1.begin(), counter1.end());
    sort(counter2.begin(), counter2.end());

    for (int i = 0; i < 26; i++) {
        if (counter1[i] != counter2[i]) {
            return false;
        }
    }

    return true;
}

int main() {
    // Test Case 1
    string word1 = "abc";
    string word2 = "bca";
    
    bool result = closeStrings(word1, word2);
    cout << result << endl;

    // Test Case 2
    word1 = "a";
    word2 = "aa";

    result = closeStrings(word1, word2);
    cout << result << endl;

    // Test Case 3
    word1 = "cabbba";
    word2 = "abbccc";

    result = closeStrings(word1, word2);
    cout << result << endl;

    return 0;
}