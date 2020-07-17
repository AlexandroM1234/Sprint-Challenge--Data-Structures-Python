"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# from stack import Stack
# from queue import Queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif (target < self.value ):
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # ignore left side entirelly and traverse the right side to find the maximum value
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if current node is None
        # we know we've reached the end of a recursion
        if self is None:
            return
        # check if we can go left
        if self.left is not None:
            self.left.in_order_print(node)
        # visit the node by printing its value
        print(self.value)
        # check if we can move right
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     if self is None:
    #         return
    #     # Use a queue to form a line
    #     line = Queue()
    #     # Node passed in is the root node of the tree
    #     line.enqueue(self)
    #     # while length of queue is greater than 0
    #     while line.__len__() > 0 :
    #         # dequeue item from the front of queue
    #         front_node = line.dequeue()
    #         # print that item
    #         print (front_node.value)
    #         # place current item's left node in queue if not None
    #         if front_node.left is not None:
    #             line.enqueue(front_node.left)
    #         # place current item's right node in queue if not None
    #         if front_node.right is not None:
    #             line.enqueue(front_node.right)
    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     if self is None:
    #         return
    #     # initialize an empty stack
    #     stack = Stack()
    #     # push the root node onto the stack
    #     stack.push(self)
    #     # if stack is not empty enter the while loop
    #     while stack.__len__() > 0:
    #         # pop top item off the stack
    #         top_stack = stack.pop()
    #         # print that item's value
    #         print (top_stack.value)
    #         # if there is a right subtree
    #         if top_stack.right is not None:
    #             # push right item onto the stack
    #             stack.push(top_stack.right)
    #         # if there is a left subtree
    #         if top_stack.left is not None:
    #             # push left item onto the stack
    #             stack.push(top_stack.left)
    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
