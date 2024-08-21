"""

https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n 
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is 
(2 + 3) / 2 = 2.5.
 

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

"""

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    
    left = 0
    right = len(nums1) - 1

    while True:
        i = (left + right) // 2
        j = half - i - 1 - 1

        nums1Left = nums1[i] if i >= 0 else float('-inf')
        nums1Right = nums1[i+1] if (i+1) < len(nums1) else float('inf')
        nums2Left = nums2[j] if j >= 0 else float('-inf')
        nums2Right = nums2[j+1] if (j+1) < len(nums2) else float('inf')

        if nums1Left <= nums2Right and nums2Left <= nums1Right:
            if total % 2 == 1:
                return min(nums1Right, nums2Right)
            else:
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
        elif nums1Left > nums2Right:
            right = i - 1
        else:
            left = i + 1

if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))