""" Basic BST code for inserting (i.e. building) and printing a tree. 
"""
items=[] #items list to print the tree data
import math#used to present the tree in better format

""" Node class
"""

class Node: #class for the tree nodes
    def __init__(self, data = None): #class constructor and attributes
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def pre_order(self): #Binary Trees pre order method that calls the helper method if the root node is established
        if self.root!=None:
            self._pre_order(self.root)


    def _pre_order(self, cur_node):## helper method for the pre order method. if the cur_node is not null append the value to the items list and print nodes
        #visited
        if cur_node!=None:
            items.append(cur_node.data)
            print(items)
            if self.root.left!=None: #check if left child is null and traverse from the left child if it is not
                self._pre_order(cur_node.left)
            if self.root.right!=None:#check if right child is null and traverse from the right child if it is not
             self._pre_order(cur_node.right)

    def in_order(self): #Binary Trees in order method that calls the helper method if the root node is established
        if self.root!=None:
            self._in_order(self.root)
            
    def _in_order(self,cur_node):## helper method for the in order method. if the cur_node is not null and the left child is not null,
                                 #append the value to the items list and print the list of nodes visited
        if cur_node!=None:
            if self.root.left!=None:
                items.append(cur_node.data)
                print(items)
                self._in_order(cur_node.left)
            
            if cur_node.right!=None:
                self._in_order(cur_node.right) check if right child is null and traverse from the right child if it is not
    
    
 
    def post_order(self):#Binary Trees post order method that calls the helper method if the root node is established
        if self.root!=None:
            self._post_order(self.root)
            
    def _post_order(self,cur_node):#helper method for the pre order method. if the cur_node is not null append the value to the items list and print nodes
                                   #visited

        if cur_node!=None:#helper method for the in order method. if the cur_node is not null and the right child is not null,#append the value to the items
                          #list and print the list of nodes visited
            if self.root.left!=None:
                self._post_order(cur_node.left)
            
            if cur_node.right!=None:
                self._post_order(cur_node.right)
            items.append(cur_node.data)
            print(items)
        
    
    
        
    def __init__(self): #binary tree constructor 
        self.root = None

    def insert(self, data): #Binary tree method to insert nodes into the tree
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node): #helper method for the insert method. assigns data to the null node after checking both the left and right children
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node): #method to display the values as a tree
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):#helper method to present the tree using characters
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
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

   



#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)

##bst.insert(10)
##bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)
print(bst.pre_order()) #traversal algorithm calls
print(bst.in_order())
print(bst.post_order())



