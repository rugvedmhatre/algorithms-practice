# O(d * (n + b)) time | O(n + b) space

# Example:
# array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
# result = [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

def radixSort(array):
    if len(array) == 0:
        return array
    
    maxNumber = max(array)
    
    digit = 0
    while maxNumber / (10 ** digit) > 0:
        countingSort(array, digit)
        digit += 1
    
    return array
    
def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10
    
    digitColumn = 10 ** digit
    for num in array:
        countIdx = (num // digitColumn) % 10
        countArray[countIdx] += 1
    
    for idx in range(1, 10):
        countArray[idx] += countArray[idx - 1]
        
    # Traverse in reverse to make it a 'stable' sort
    for idx in range(len(array) - 1, -1, -1):
        countIdx = (array[idx] // digitColumn) % 10
        countArray[countIdx] -= 1
        sortedIdx = countArray[countIdx]
        sortedArray[sortedIdx] = array[idx]
    
    for idx in range(len(array)):
        array[idx] = sortedArray[idx]
        
if __name__ == '__main__':
    array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
    print(radixSort(array))