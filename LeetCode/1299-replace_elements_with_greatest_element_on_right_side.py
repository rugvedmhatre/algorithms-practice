"""

https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array arr, replace every element in that array with the greatest element 
among the elements to its right, and replace the last element with -1.

After doing so, return the array.


Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i] <= 10^5

"""

def replaceElements(arr: list[int]) -> list[int]:
    # if len(arr) == 1:
    #     arr[-1] = -1
    #     return arr

    currentMax = -1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > currentMax:
            arr[i], currentMax = currentMax, arr[i]
        else:
            arr[i] = currentMax
        
    return arr

if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    # arr = [400]
    print(replaceElements(arr))