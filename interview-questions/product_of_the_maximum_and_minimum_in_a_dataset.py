"""

Starting with an empty set of integers named elements,
perform the following query operations:
- The command push x inserts the value of x into elements
- The command pop x removes the value of x from elements

The integers in elements need to be ordered in such a way
that after each operation is performed, the product of the
maximum and minimum values in the set can be easily
calculated.

"""

def maxMin(operations, x):
    result = []
    
    class ElementSet():
        def __init__(self):
            self.elements = []
        
        def push(self, x):
            self.elements.append(x)
            self.elements.sort()
        
        def pop(self, x):
            self.elements.remove(x)
            self.elements.sort()
        
        def maxMinProd(self):
            return self.elements[0] * self.elements[-1]
    
    elementSet = ElementSet()

    for operation, val in zip(operations, x):
        if operation == 'push':
            elementSet.push(val)
        elif operation == 'pop':
            elementSet.pop(val)
        result.append(elementSet.maxMinProd())
    
    return result


def testCase0():
    operations = ['push', 'push', 'push', 'pop']
    x = [1, 2, 3, 1]
    result = maxMin(operations, x)
    print(result)
    assert(result == [1, 2, 3, 6])

def testCase1():
    operations = ['push', 'push']
    x = [3, 2]
    result = maxMin(operations, x)
    print(result)
    assert(result == [9, 6])

if __name__ == '__main__':
    testCase0()
    testCase1()