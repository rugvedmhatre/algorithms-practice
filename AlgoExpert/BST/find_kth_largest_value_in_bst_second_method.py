# O(h + k) time | O(h) space

from bst_construction import BST

class TreeInfo():
    def __init__(self, numberOfNodesVisited: int, latestVisitedNodeValue: int) -> None:
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue

def findKthLargestValueInBST(tree: BST, k: int) -> int:
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraversal(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraversal(node: BST, k: int, treeInfo: TreeInfo) -> None:
    if node == None or treeInfo.numberOfNodesVisited >= k:
        return
    
    reverseInOrderTraversal(node.right, k, treeInfo)

    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraversal(node.left, k, treeInfo)
    
    
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