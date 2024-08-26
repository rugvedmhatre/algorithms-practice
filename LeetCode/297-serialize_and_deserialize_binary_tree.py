"""

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in a
file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

Clarification: The input/output format is the same as how
LeetCode serializes a binary tree. You do not necessarily need to
follow this format, so please be creative and come up with
different approaches yourself.


Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
 

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

"""

from data_structures import TreeNode

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        dataList = data.split(',')

        def dfs():
            if dataList[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(dataList[self.i]))
            self.i += 1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()

if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    print("Tree:")
    tree.display()
    print("")
    
    serializer = Codec()
    deserializer = Codec()

    encoded_tree = serializer.serialize(tree)
    print("Serialized Tree:", encoded_tree)
    print("")

    decoded_tree = deserializer.deserialize(encoded_tree)
    print("Deserialized Tree:")
    decoded_tree.display()