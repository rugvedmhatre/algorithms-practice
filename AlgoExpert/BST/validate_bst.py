# O(n) time | O(d) space

from bst_construction import BST

def validateBST(tree):
    return validateBSTHelper(tree, float('-inf'), float('inf'))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)

    return leftIsValid and validateBSTHelper(tree.right, tree.value, maxValue)

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

    print("Validating BST...")
    print("Result: ", validateBST(bst))