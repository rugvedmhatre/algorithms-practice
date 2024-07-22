# O(n) time | O(d) space

from bst_construction import BST

def inOrderTraverse(tree, result=[]):
    if tree is not None:
        inOrderTraverse(tree.left, result)
        result.append(tree.value)
        inOrderTraverse(tree.right, result)
    return result

def preOrderTraverse(tree, result=[]):
    if tree is not None:
        result.append(tree.value)
        preOrderTraverse(tree.left, result)
        preOrderTraverse(tree.right, result)
    return result

def postOrderTraverse(tree, result=[]):
    if tree is not None:
        postOrderTraverse(tree.left, result)
        postOrderTraverse(tree.right, result)
        result.append(tree.value)
    return result

if __name__ == '__main__':
    # Constructing BST:
    bst = BST(10)
    bst.insert(5)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(15)
    bst.insert(22)
    
    print("Initial BST")
    bst.display()

    print("")

    print("In Order Traversal:")
    print(inOrderTraverse(bst))

    print("")

    print("Pre Order Traversal:")
    print(preOrderTraverse(bst))

    print("")

    print("Post Order Traversal:")
    print(postOrderTraverse(bst))