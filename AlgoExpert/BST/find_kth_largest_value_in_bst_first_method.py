# O(n) time | O(n) space

from bst_construction import BST

def findKthLargestValueInBST(tree, k):
    sortedNodeValues = []
    inOrderTraversal(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraversal(node, sortedNodeValues):
    if node == None:
        return
    
    inOrderTraversal(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraversal(node.right, sortedNodeValues)
    
if __name__ == '__main__':
    tree = BST(15)
    tree.insert(5)
    tree.insert(20)
    tree.insert(17)
    tree.insert(22)
    tree.insert(2)
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    
    tree.display()
    
    print()

    k = 3
    print(f"Kth Largest Value in Tree (K = {k}): ")
    print(findKthLargestValueInBST(tree, k))