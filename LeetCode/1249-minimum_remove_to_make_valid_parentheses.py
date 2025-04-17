"""

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that 
the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '(' , ')', or lowercase English letter.

"""

def minRemoveToMakeValid(s: str) -> str:
    count = 0
    filtered_s = []

    for char in s:
        if char == '(':
            count += 1
        if char == ')':
            if count == 0:
                continue
            else:
                count -= 1
        filtered_s.append(char)

    if count == 0:
        return ''.join(filtered_s)
    
    result = []

    for char in reversed(filtered_s):
        if char == '(' and count > 0:
            count -= 1
            continue
        result.append(char)
    
    return ''.join(result[::-1])

if __name__ == "__main__":
    # Test Case 1
    s = "lee(t(c)o)de)"
    print(minRemoveToMakeValid(s))

    # Test Case 2
    s = "a)b(c)d"
    print(minRemoveToMakeValid(s))

    # Test Case 3
    s = "))(("
    print(minRemoveToMakeValid(s))