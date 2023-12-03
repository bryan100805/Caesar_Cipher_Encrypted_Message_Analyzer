# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 19/11/2023
# File: CipherKeyNode.py

from SortedList.Node import Node

# Child class to sort the cipher key and file name for Batch Processing
class CipherKeyNode(Node):
    def __init__(self, file, cipher_key):
        self.file = file
        self.cipher_key = cipher_key
        super().__init__()

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'CipherKeyNode' and 'NoneType'"
            )
        # Checks if self cipher_key is smaller than otherNode's cipher_key
        elif self.cipher_key < otherNode.cipher_key:
            return True
        # Checks if self cipher_key is larger than otherNode's cipher_key
        elif self.cipher_key < otherNode.cipher_key:
            return False
        # If equal, compare the characters
        else:
            return self.file < otherNode.file

    # String representation of the node
    def __repr__(self):
        s = f"{self.file}: {self.cipher_key}"
        return s
