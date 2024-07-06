# O(nlog(n)) time | O(n) space

# Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
# If the array is already sorted, then the inversion count is 0, but if the array is sorted 
# in reverse order, the inversion count is the maximum.

# Given an array 'array'. The task is to find the inversion count of 'array'. 
# Where two elements array[i] and array[j] form an inversion if array[i] > array[j] and i < j.

# Example:
# array = [2, 3, 3, 1, 9, 5, 6]
# result = 5

def countInversions(array):
    return countSubArrayInversions(array, 0, len(array))
    
def countSubArrayInversions(array, start, end):
    if end - start <= 1:
        return 0
    
    middle = start + (end - start) // 2
    leftInversions = countSubArrayInversions(array, start, middle)
    rightInversions = countSubArrayInversions(array, middle, end)
    mergedArrayInversions = mergeSortAndCountInversions(array, start, middle, end)
    return leftInversions + rightInversions + mergedArrayInversions
    
def mergeSortAndCountInversions(array, start, middle, end):
    sortedArray = []
    left = start
    right = middle
    inversions = 0
    
    while left < middle and right < end:
        if array[left] <= array[right]:
            sortedArray.append(array[left])
            left += 1
        else:
            inversions += middle - left
            sortedArray.append(array[right])
            right += 1
    
    sortedArray += array[left:middle] + array[right:end]
    for idx, num in enumerate(sortedArray):
        array[start + idx] = num
        
    return inversions

if __name__ == '__main__':
    array = [2, 3, 3, 1, 9, 5, 6]
    print(countInversions(array))