"""

https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8

"""

def generateParenthesis(n: int) -> list[str]:
    result = []
    stack = []

    def backtrack(openCount: int, closeCount: int) -> None:
        if openCount == closeCount == n:
            result.append(''.join(stack))
            return
        
        if openCount < n:
            stack.append('(')
            backtrack(openCount + 1, closeCount)
            stack.pop()
        
        if closeCount < openCount:
            stack.append(')')
            backtrack(openCount, closeCount + 1)
            stack.pop()
        
    backtrack(0, 0)
    
    return result

if __name__ == '__main__':
    print(generateParenthesis(3))