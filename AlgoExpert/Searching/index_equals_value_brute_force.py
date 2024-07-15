# O(n) time | O(1) space

def indexEqualsValue(array):
    for index in range(len(array)):
        value = array[index]
        if index == value:
            return index
            
    return -1

if __name__ == '__main__':
    array = [-5, -3, 0, 3, 4, 5, 9]
    print(indexEqualsValue(array))