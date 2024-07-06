# O(log(n)) time | O(log(n)) space

# Your goal is to find the range of indices that contain our target number.
# Example: array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# Output: [4, 9]

def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, goLeft=True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, goLeft=False)
    return finalRange
    
def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    if left > right:
        return
    middle = (left + right) // 2
    
    if array[middle] < target:
        alteredBinarySearch(array, target, middle + 1, right, finalRange, goLeft)
    elif array[middle] > target:
        alteredBinarySearch(array, target, left, middle - 1, finalRange, goLeft)
    else:
        if goLeft:
            if middle == 0 or array[middle - 1] != target:
                finalRange[0] = middle
            else:
                alteredBinarySearch(array, target, left, middle - 1, finalRange, goLeft)
        else:
            if middle == len(array) - 1 or array[middle + 1] != target:
                finalRange[1] = middle
            else:
                alteredBinarySearch(array, target, middle + 1, right, finalRange, goLeft)

if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    target = 45
    print(searchForRange(array, target))