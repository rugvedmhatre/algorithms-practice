# O(n) time | O(1) space

# Example:
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]
# result = [0, 0, 0, 1, 1, 1, -1, -1]

def threeNumberSort(array, order):
    firstValue = order[0]
    thirdValue = order[2]
    
    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            swap(firstIdx, idx, array)
            firstIdx += 1
            
    thirdIdx = len(array) - 1
    for idx in range(len(array) - 1, -1, -1):
        if array[idx] == thirdValue:
            swap(thirdIdx, idx, array)
            thirdIdx -= 1
            
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
if __name__ == '__main__':
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    print(threeNumberSort(array, order))