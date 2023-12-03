# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 19/11/2023
# File: SortedList.py

# Implementing a SortedList using insertion sort
class SortedList:

    def __init__(self):
        # Represents the first node in the list
        self.headNode = None
        # Represents the current node during travesal in the list (Not used)
        self.currentNode = None
        # Number of nodes in the list
        self.length = 0

    def __appendToHead(self, newNode):
        # Save the current head node as `oldHeadNode` ['B','C']
        oldHeadNode = self.headNode
        # Updates `self.headNode` to point to `newNode` ['A']
        self.headNode = newNode
        # Sets the `nextNode` of `newNode` to `oldHeadNode` ['A','B','C']
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert_largest_first(self, newNode):
        self.length += 1

        # Case 1: Empty list
        if self.headNode == None:
            # Making the new node the head node/first node
            self.headNode = newNode
            return

        # Case 2: Insert the head
        # If the new node is greater than the head node, insert it at the head
        if newNode > self.headNode:
            self.__appendToHead(newNode)
            return

        # Case 3: Insert after head (Insertion Sort)
        # Start from the head node
        leftNode = self.headNode
        # The node after the head node
        rightNode = self.headNode.nextNode

        # Traverse the list until we find the right position to insert the new node
        # not None means there is a node to traverse through
        while rightNode != None:
            # If the new node is greater than the right node,
            # insert it between the left and right nodes
            if newNode > rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        # Case 4: Insert at the end if newNode is greater than or equal to all nodes
        leftNode.nextNode = newNode


    def insert_smallest_first(self, newNode):
        self.length += 1
        if self.headNode == None:
            self.headNode = newNode
            return

        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        leftNode = self.headNode
        rightNode = self.headNode.nextNode

        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        leftNode.nextNode = newNode

    def __str__(self):
        # Traverse the list
        output = ''
        node = self.headNode
        # Boolean flag to handle adding commas between nodes in string representation
        firstNode = True
        # Continue traversing the list until we reach the end
        while node != None:
            if firstNode:
                output += str(node.__str__())
                # Set flag to False after adding the first node
                firstNode = False
            else:
                output += ', ' + str(node.__str__())
            # Updates the current node to the next node
            node = node.nextNode
        # Return the string representation of the list
        return output
    
    # Returns length of list
    def __len__(self):
        return self.length
    
    # Returns the node in front of the list
    def get_top(self, n):
        # Return the top n nodes in the list
        top_nodes = []
        node = self.headNode
        while node is not None and len(top_nodes) < n:
            top_nodes.append(node)
            node = node.nextNode
        return top_nodes