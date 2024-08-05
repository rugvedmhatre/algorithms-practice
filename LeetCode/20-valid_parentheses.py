"""

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', 
'{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the 
   same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

"""

def isValid(s: str) -> bool:
    brackStack = list()
    brackMap = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in brackMap:
            if len(brackStack) != 0 and brackStack[-1] == brackMap[char]:
                brackStack.pop()
            else:
                return False
        else:
            brackStack.append(char)
    
    return len(brackStack) == 0

if __name__ == '__main__':
    s = "()[]{}"
    print(isValid(s))