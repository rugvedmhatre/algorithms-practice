# O(log(n)) time | O(log(n)) space

def indexEqualsValue(array):
    return indexEqualsValueHelper(array, 0, len(array) - 1)
    
def indexEqualsValueHelper(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    
    middleIdx = (leftIdx + rightIdx) // 2
    middleVal = array[middleIdx]
    
    if middleVal < middleIdx:
        return indexEqualsValueHelper(array, middleIdx + 1, rightIdx)
    elif middleVal == middleIdx and middleIdx == 0:
        return middleIdx
    elif middleVal == middleIdx and array[middleIdx - 1] < middleIdx - 1:
        return middleIdx
    else:
        return indexEqualsValueHelper(array, leftIdx, middleIdx - 1)

if __name__ == '__main__':
    array = [-5, -3, 0, 3, 4, 5, 9]
    print(indexEqualsValue(array))