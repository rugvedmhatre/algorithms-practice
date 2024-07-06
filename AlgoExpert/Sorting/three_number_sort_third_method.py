# O(n) time | O(1) space

# Example:
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]
# result = [0, 0, 0, 1, 1, 1, -1, -1]

def threeNumberSort(array, order):
    firstValue = order[0]
    secondValue = order[1]
    
    # Keep track of the indices where the values are stored
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1
    
    while secondIdx <= thirdIdx:
        value = array[secondIdx]
        
        if value == firstValue:
            swap(secondIdx, firstIdx, array)
            firstIdx += 1
            secondIdx += 1
        
        elif value == secondValue:
            secondIdx += 1
        
        else:
            swap(secondIdx, thirdIdx, array)
            thirdIdx -= 1
    
    return array
    
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
if __name__ == '__main__':
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    print(threeNumberSort(array, order))