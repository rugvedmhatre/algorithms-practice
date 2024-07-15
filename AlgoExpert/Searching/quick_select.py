# O(n) time | O(1) space

def quickselect(array, k):
    position = k - 1
    return quickselecthelper(array, 0, len(array) - 1, position)
     
def quickselecthelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Algorithm should never arrive here!")
        
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
            
        swap(pivotIdx, rightIdx, array)
        
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1
                
def swap(one, two, array):
    array[one], array[two] = array[two], array[one]

if __name__ == '__main__':
    array = [8, 5, 2, 9, 7, 6, 3]
    # Find the third smallest number
    k = 3
    print(quickselect(array, k))