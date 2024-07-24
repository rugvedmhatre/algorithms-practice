# O(n) time | O(n) space

from bst_construction import BST

def minHeightBST(array):
    return constructMinHeightBST(array, 0, len(array) - 1)

def constructMinHeightBST(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBST(array, midIdx + 1, endIdx)
    return bst

if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    bst = minHeightBST(array)
    
    print("Input Array")
    print(array)
    
    print("Constructed Min Height BST:")
    bst.display()