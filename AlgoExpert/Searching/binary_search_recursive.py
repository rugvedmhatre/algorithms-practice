# O(log(N)) time | O(log(N)) space

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2

    potentialMatch = array[middle]

    if potentialMatch == target:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)

if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binarySearch(array, target))