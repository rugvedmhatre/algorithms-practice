# O(log(N)) time | O(1) space

def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1


if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binarySearch(array, target))