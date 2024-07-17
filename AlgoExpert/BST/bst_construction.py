class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Average: O(log(N)) time | O(1) space
    # Worst: O(N) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
    
    # Average: O(log(N)) time | O(1) space
    # Worst: O(N) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
        
    # Average: O(log(N)) time | O(1) space
    # Worst: O(N) time | O(1) space
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        # You should replace in this specific order - right first and left last
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    if currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        # You should replace in this specific order - left first and right last
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    if currentNode.left is not None:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.left = currentNode.right
                elif parentNode.right == currentNode:
                    if currentNode.left is not None:
                        parentNode.right = currentNode.left
                    else:
                        parentNode.right = currentNode.right
                break
        return self

    # Average: O(log(N)) time | O(1) space
    # Worst: O(N) time | O(1) space
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    # Code to print BST from stackoverflow: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
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

    # Inserting 12 in the BST
    print("Inserting 12 in the BST")
    bst.insert(12)
    bst.display()

    print("")

    # Removing 1 from the BST
    print("Removing 1 from the BST")
    bst.remove(1)
    bst.display()

    print("")

    # Resetting the BST...
    print("Resetting the BST")
    bst.insert(1)
    bst.display()

    print("")

    # Removing 2 from the BST
    print("Removing 2 from the BST")
    bst.remove(2)
    bst.display()

    print("")

    # Removing 10 from the BST
    print("Removing 10 from the BST")
    bst.remove(10)
    bst.display()