# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 19/11/2023
# File: FrequencyWordNode.py

from SortedList.Node import Node

# Child class to sort the word and frequency for Word Analysis
class FrequencyWordNode(Node):
    def __init__(self, word, frequency):
        self.word = word
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
            return self.word < otherNode.word

    # String representation of the node
    def __repr__(self):
        s = f"{self.word} - {self.frequency} Occurrence(s)"
        return s