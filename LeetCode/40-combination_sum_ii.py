"""

https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a 
target number (target), find all unique combinations in 
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the 
combination.

Note: The solution set must not contain duplicate combinations.


Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

"""

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    candidates.sort()

    def dfs(i: int, current: list, total: int):
        if total == target:
            result.append(current.copy())
            return
        
        if total > target or i >= len(candidates):
            return
        
        current.append(candidates[i])
        dfs(i + 1, current, total + candidates[i])

        current.pop()
        while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
            i += 1
        dfs(i + 1, current, total)

    dfs(0, [], 0)

    return result

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combinationSum2(candidates, target))