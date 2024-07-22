# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

from bst_construction import BST

def findClosestValueInBST(tree, target):
    closest = float('inf')
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

if __name__ == '__main__':
    # Constructing BST:
    bst = BST(10)
    bst.insert(5)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(15)
    bst.insert(13)
    bst.insert(22)
    bst.insert(14)
    
    print("Initial BST")
    bst.display()

    print("")

    target = 12
    print(f"Finding closest value to {target} in the BST")
    print(findClosestValueInBST(bst, target))