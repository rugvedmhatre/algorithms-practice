"""

https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and
return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear
in both lower and upper cases, more than once.
 

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 

Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.

"""

def reverseVowels(s: str) -> str:
    left = 0
    right = len(s) - 1

    s_list = list(s)

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1

        while left < right and s_list[right] not in vowels:
            right -= 1
        
        if (s_list[left] in vowels) and (s_list[right] in vowels):
            s_list[left], s_list[right] = s_list[right], s_list[left]

        left += 1
        right -= 1

    return ''.join(s_list)

if __name__ == '__main__':
    s = "hello"
    print(reverseVowels(s))