# O(n) time | O(n) space

from bst_construction import BST

def minHeightBST(array):
    return constructMinHeightBST(array, None, 0, len(array) - 1)

def constructMinHeightBST(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    newBSTNode = BST(array[midIdx])
    if bst is None:
        bst = newBSTNode
    else:
        if array[midIdx] < bst.value:
            bst.left = newBSTNode
            bst = bst.left
        else:
            bst.right = newBSTNode
            bst = bst.right
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