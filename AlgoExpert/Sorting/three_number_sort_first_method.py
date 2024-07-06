# O(n) time | O(1) space

# Example:
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]
# result = [0, 0, 0, 1, 1, 1, -1, -1]

def threeNumberSort(array, order):
    valueCounts = [0, 0, 0]
    
    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1
    
    for i in range(3):
        value = order[i]
        count = valueCounts[i]
        
        numElementsBefore = sum(valueCounts[:i])
        
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value

    return array

if __name__ == '__main__':
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    print(threeNumberSort(array, order))