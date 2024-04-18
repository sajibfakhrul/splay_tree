# Splay tree implementation in Python

import sys

class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    

    def __search_tree_helper(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

   

    # rotate left at node x
    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # Splaying operation. It moves x to the root of the tree
    def __splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig rotation
                    self.__right_rotate(x.parent)
                else:
                    # zag rotation
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                # zag-zig rotation
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

    # joins two trees s and t
    def __join(self, s, t):
        if s == None:
            return t

        if t == None:
            return s

        x = self.maximum(s)
        self.__splay(x)
        x.right = t
        t.parent = x
        return x

    def __pre_order_helper(self, node):
        if node != None:
            sys.stdout.write(str(node.data) + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != None:
            self.__in_order_helper(node.left)
            sys.stdout.write(str(node.data) + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(str(node.data) + " ")

    def preorder(self):
        self.__pre_order_helper(self.root)

    def inorder(self):
        self.__in_order_helper(self.root)

    def postorder(self):
        self.__post_order_helper(self.root)

    def search_tree(self, k):
        x = self.__search_tree_helper(self.root, k)
        if x != None:
            self.__splay(x)

    def minimum(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node  

    def maximum(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node
    
    def find(self, key):
        if self.root is None:
            return False
    # Search for the node with the key
        x = self.__search_tree_helper(self.root, key)
        if x is not None:
            self.__splay(x)
        if self.root.data != key:
            return False
        return True



    

    def successor(self, x):
        if x.right != None:
            return self.minimum(x.right)

        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left != None:
            return self.maximum(x.left)

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    def insert(self, key):
        node =  Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.__splay(node)
        
    def findKey(self, key):
        if self.root is None:
            return None
    # Search for the node with the key
        x = self.__search_tree_helper(self.root, key)
        if x is not None:
            self.__splay(x)
        if self.root.data != key:
            return None
        return self.root.data     
    
     def remove(self, key):
        self.search_tree(key)  # Splay the node with the given key to the root
        if key != self.root.data:
            return False

        # Now delete the root.
        if self.root.left is None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            if self.root:
                self.root.parent = None
            self.__join(self.root, x)
            
     def removeValue(self, key):
        k = self.findKey(key)   
        return self.remove(k)

       


   

   


   
