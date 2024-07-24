# O(nlog(n)) time | O(n) space

from bst_construction import BST

def minHeightBST(array):
    return constructMinHeightBST(array, None, 0, len(array) - 1)

def constructMinHeightBST(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:	
        bst.insert(valueToAdd)
    constructMinHeightBST(array, bst, startIdx, midIdx - 1)
    constructMinHeightBST(array, bst, midIdx + 1, endIdx)
    return bst

if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    bst = minHeightBST(array)
    
    print("Input Array")
    print(array)
    
    print("Constructed Min Height BST:")
    bst.display()