# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 18/10/2023
# File: CaesarCipher.py
from Cipher import Cipher

# Creating parent class that performs caesar cipher
class CaesarCipher(Cipher):
    def __init__(self, message, key=0):
        self.message = message
        super().__init__(key)

    # Request for cipher key from user
    def getCipherKey(self):
        while True:
            try:
                key = int(input("\nEnter the cipher key: "))
                # Checks if cipher key is an integer and falls between -25 and 25 and is not 0
                if isinstance(key, int) and (-25 <= key <= 25) and (key != 0):

                    self.set_key(key)
                    return self.key

                else:
                    print("Invalid cipher key. Please enter a non-zero integer between -25 and 25, excluding 0.")
            # If input is not a number
            except ValueError:
                print("Invalid Input. Please enter an integer.")

    # Function to shift each character by the cipher key
    def __shift_char(self, char, key):
        # Checks if character is alphabet letter
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            shifted_char = chr((ord(char) - base + key) % 26 + base)
            return shifted_char
        # Returns character if it is not an alphabet letter
        else:
            return char

    # Encrypt the message
    def get_encrypted(self):
        key =self.key
        encrypted_message = ''.join(self.__shift_char(char, key) for char in self.message)
        return encrypted_message
    
    # Decrypt the message
    def get_decrypted(self):
        key = -self.key
        decrypted_message = ''.join(self.__shift_char(char, key) for char in self.message)
        return decrypted_message

    # Decrypt message in each individual file
    # Assumes that key is a dictionary that stores the file as key and the cipher key as value 
    # Assumes that message is a dictionary that stores the file as key and the message to be decrypted as value
    def get_file_decrypted(self, message, key):
        decrypted_message = ''.join(self.__shift_char(char, -key) for char in message)
        return decrypted_message

    def init_option(self):
        raise NotImplementedError("Subclass must implement abstract method")