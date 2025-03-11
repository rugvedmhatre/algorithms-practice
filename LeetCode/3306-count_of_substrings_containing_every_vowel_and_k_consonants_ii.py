"""

https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii

You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u')
at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:
- word[0..5], which is "ieaouq".
- word[6..11], which is "qieaou".
- word[7..12], which is "ieaouq".


Constraints:
- 5 <= word.length <= 2 * 10^5
- word consists only of lowercase English letters.
- 0 <= k <= word.length - 5

"""

from collections import defaultdict


def countOfSubstrings(word: str, k: int) -> int:
    vowel_counts = defaultdict(int)
    for letter in "aeiou":
        vowel_counts[letter] = 0

    vowels = set("aeiou")

    next_con = [len(word)] * len(word)
    next_con_idx = len(word)

    for i in range(len(word) - 1, -1, -1):
        next_con[i] = next_con_idx
        if word[i] not in vowels:
            next_con_idx = i

    l = 0
    substrings = 0
    con_count = 0

    for r in range(len(word)):
        cur_letter = word[r]
        if cur_letter in vowels:
            vowel_counts[cur_letter] += 1
        else:
            con_count += 1

        while con_count > k and l <= r:
            left_letter = word[l]
            if left_letter in vowels:
                vowel_counts[left_letter] -= 1
            else:
                con_count -= 1
            l += 1

        while (
            l <= r and con_count == k and all(val > 0 for val in vowel_counts.values())
        ):
            substrings += next_con[r] - r

            left_letter = word[l]
            if left_letter in vowels:
                vowel_counts[left_letter] -= 1
            else:
                con_count -= 1
            l += 1

    return substrings


if __name__ == "__main__":
    # Test Case 1
    word = "aeioqq"
    k = 1
    print(countOfSubstrings(word, k))

    # Test Case 2
    word = "aeiou"
    k = 0
    print(countOfSubstrings(word, k))

    # Test Case 3
    word = "ieaouqqieaouqq"
    k = 1
    print(countOfSubstrings(word, k))
