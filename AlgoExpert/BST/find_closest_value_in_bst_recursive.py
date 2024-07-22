# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

from bst_construction import BST

def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float('inf'))

def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    else:
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