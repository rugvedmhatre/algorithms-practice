"""

https://leetcode.com/problems/remove-invalid-parentheses/

Given a string s that contains parentheses and letters, remove the minimum number of invalid 
parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return
the answer in any order.
 

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]
 

Constraints:
- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.longest_string = -1
        self.res = set()
        
        self.dfs(s, 0, [], 0, 0)
        
        return list(self.res)
    
    def dfs(self, string, cur_idx, cur_res, l_count, r_count):
        if cur_idx >= len(string):
            if l_count == r_count:
                if len(cur_res) > self.longest_string:
                    self.longest_string = len(cur_res)
                    self.res = set()
                    self.res.add("".join(cur_res))
                elif len(cur_res) == self.longest_string:
                    self.res.add("".join(cur_res))
        else:
            cur_char = string[cur_idx]
            if cur_char == "(":
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count + 1, r_count)
                cur_res.pop()
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
            elif cur_char == ")":
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                
                if l_count > r_count:
                    cur_res.append(cur_char)
                    self.dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)
                    cur_res.pop()
            else:
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                cur_res.pop()

if __name__ == "__main__":
    # Test Case 1
    s = "()())()"
    sol = Solution()
    print(sol.removeInvalidParentheses(s))

    # Test Case 2
    s = "(a)())()"
    sol = Solution()
    print(sol.removeInvalidParentheses(s))

    # Test Case 3
    s = ")("
    sol = Solution()
    print(sol.removeInvalidParentheses(s))