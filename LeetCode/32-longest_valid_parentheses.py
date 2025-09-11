"""

https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', return the length of the longest valid 
(well-formed) parentheses substring.
 

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0


Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.

"""

def longestValidParentheses(s: str) -> int:
    lc = rc = maxLen = 0

    for i in range(len(s)):
        if s[i] == '(':
            lc += 1
        else:
            rc += 1
        
        if lc == rc:
            maxLen = max(maxLen, lc + rc)
        elif rc > lc:
            lc = rc = 0
    
    lc = rc = 0

    for i in range(len(s)-1, -1, -1):
        if s[i] == '(':
            lc += 1
        else:
            rc += 1
        
        if lc == rc:
            maxLen = max(maxLen, lc + rc)
        elif lc > rc:
            lc = rc = 0

    return maxLen

if __name__ == "__main__":
    # Test Case 1
    s = "(()"
    print(longestValidParentheses(s))

    # Test Case 2
    s = ")()())"
    print(longestValidParentheses(s))

    # Test Case 3
    s = ""
    print(longestValidParentheses(s))