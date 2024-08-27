"""

https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth
largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Can you solve it without sorting?
 

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

"""

# Heap Based Algorithm:
import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap[0]

# Quick Select Algorithm:
def partition(nums: list[int], left: int, right: int) -> int:
    pivot, fill = nums[right], left

    for i in range(left, right):
        if nums[i] <= pivot:
            nums[fill], nums[i] = nums[i], nums[fill]
            fill += 1

    nums[fill], nums[right] = nums[right], nums[fill]

    return fill

def findKthLargestUsingQuickSelect(nums: list[int], k: int) -> int:
    k = len(nums) - k
    left, right = 0, len(nums) - 1

    while left < right:
        pivot = partition(nums, left, right)

        if pivot < k:
            left = pivot + 1
        elif pivot > k:
            right = pivot - 1
        else:
            break

    return nums[k]


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest(nums, k))
    print(findKthLargestUsingQuickSelect(nums, k))