# O(log(n)) time | O(1) space

# Your goal is to find the range of indices that contain our target number.
# Example: array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# Output: [4, 9]

def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, goLeft=True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, goLeft=False)
    return finalRange
    
def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    while left <= right:
        middle = (left + right) // 2
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            if goLeft:
                if middle == 0 or array[middle - 1] != target:
                    finalRange[0] = middle
                    return
                else:
                    right = middle - 1
            else:
                if middle == len(array) - 1 or array[middle + 1] != target:
                    finalRange[1] = middle
                    return
                else:
                    left = middle + 1

if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    target = 45
    print(searchForRange(array, target))