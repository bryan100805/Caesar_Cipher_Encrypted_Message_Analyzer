# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 19/11/2023
# File: FrequencyCharNode.py

from SortedList.Node import Node

# Child class to sort the character and frequency for Character Analysis
class FrequencyCharNode(Node):
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        super().__init__()

    def __gt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'>' not supported between instances of 'FrequencyCharNode' and 'NoneType'"
            )
        # Checks if self frequency is smaller than otherNode's frequency
        elif self.frequency < otherNode.frequency:
            return False
        # Checks if self frequency is larger than otherNode's frequency
        elif self.frequency > otherNode.frequency:
            return True
        # If equal, compare the characters
        else:
            return self.char < otherNode.char

    # String representation of the node
    def __str__(self):
        s = f"\t| {self.char}- {self.frequency:.2f}%"
        return s