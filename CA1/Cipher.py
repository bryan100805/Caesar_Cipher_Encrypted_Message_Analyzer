# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 22/11/2023
# File: Cipher.py

# Creating parent class that performs use getters and setters for the keys
class Cipher:
    def __init__(self, key=0):
        self.key = key

    def get_key(self):
        return self.key
    
    def set_key(self, key):
        self.key = key