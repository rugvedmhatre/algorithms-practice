# O(log(n)) time | O(1) space

# You begin with a sorted array, but it has been shifted by a certain value.
# Example: array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
# Your goal is to find the target value (for example: 33) and return it’s 
# index (in the above case the answer is 8)

def shiftedBinarySearch(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
    
        leftNum = array[left]
        rightNum = array[right]
    
        if target == potentialMatch:
            return middle
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target > potentialMatch and target <= rightNum:
                left = middle + 1
            else:
                right = middle - 1

    return -1

if __name__ == '__main__':
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
    target = 33
    print(shiftedBinarySearch(array, target))