# O(log(n)) time | O(1) space

def indexEqualsValue(array):
    leftIdx = 0
    rightIdx = len(array) - 1 
    
    while leftIdx <= rightIdx:	
        middleIdx = (leftIdx + rightIdx) // 2
        middleVal = array[middleIdx]
        
        if middleVal < middleIdx:
            leftIdx = middleIdx + 1
        elif middleVal == middleIdx and middleIdx == 0:
            return middleIdx
        elif middleVal == middleIdx and array[middleIdx - 1] < middleIdx - 1:
            return middleIdx
        else:
            rightIdx = middleIdx - 1
            
    return -1

if __name__ == '__main__':
    array = [-5, -3, 0, 3, 4, 5, 9]
    print(indexEqualsValue(array))