"""

https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and
c.


Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are
"abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are
"aaacb", "aacb" and "acb".

Example 3:
Input: s = "abc"
Output: 1


Constraints:
- 3 <= s.length <= 5 x 10^4
- s only consists of a, b or c characters.

"""

from collections import defaultdict


def numberOfSubstrings(s: str) -> int:
    substring_count = 0
    l = 0
    n = len(s)

    letter_set = defaultdict(int)

    for r in range(n):
        letter_set[s[r]] += 1

        if len(letter_set.keys()) == 3:
            substring_count += n - r

        while l < r and len(letter_set.keys()) == 3:
            letter_set[s[l]] -= 1

            if letter_set[s[l]] == 0:
                del letter_set[s[l]]

            if len(letter_set.keys()) == 3:
                substring_count += n - r

            l += 1

    return substring_count


if __name__ == "__main__":
    # Test Case 1
    s = "abcabc"
    print(numberOfSubstrings(s))

    # Test Case 2
    s = "aaacb"
    print(numberOfSubstrings(s))

    # Test Case 3
    s = "abc"
    print(numberOfSubstrings(s))
