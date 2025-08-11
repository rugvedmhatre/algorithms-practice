"""

https://leetcode.com/problems/most-common-word/

Given a string paragraph and a string array of the banned words banned, return the most frequent 
word that is not banned. It is guaranteed there is at least one word that is not banned, and that
the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols. 


Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the 
paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"


Constraints:
- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- banned[i] consists of only lowercase English letters.

"""

import re
from collections import defaultdict

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    banned = set(banned)
    split_chars = r"[ !?',;.]"
    words = []
    counter = defaultdict(int)
    max_count = 0
    common_word = ""

    for word in re.split(split_chars, paragraph):
        word = word.lower()
        if word not in banned and word != '':
            counter[word] += 1
            if counter[word] > max_count:
                common_word = word
                max_count = counter[word]

    return common_word

if __name__ == "__main__":
    # Test Case 1
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))

    # Test Case 2
    paragraph = "a."
    banned = []
    print(mostCommonWord(paragraph, banned))