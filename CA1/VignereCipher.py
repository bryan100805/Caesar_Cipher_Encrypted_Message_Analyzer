# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 30/10/2023
# File: VignereCipher.py
from Cipher import Cipher

# Creating parent class for Vigènere cipher
class VignereCipher(Cipher):
    def __init__(self, key=""):
        self.key = key

    # Function to get key'
    def getVignereCipherKey(self):
        while True:
            key = input("\nEnter the cipher key (Word or Phrases): ")
            # Checks if cipher key contains only alphabetic characters
            if key.isalpha():
                self.__key=key
                return self.__key
                
            else:
                print(
                    "Invalid input. Please enter a key with alphabetic characters only."
                )

    # Extend key to the length of the message
    def _extend_key(self, message):
        extended_key = self.__key
        while len(extended_key) < len(message):
            extended_key += self.__key
        extended_key = extended_key[:len(message)]
        return extended_key
    
    # Encrypt the message
    def encrypt(self, message):
        encrypted_message = []
        extended_key = self._extend_key(message)
        for i in range(len(message)):
            char = message[i]
            if char.isalpha():
                # Create the shift value
                shift = ord(extended_key[i].upper()) - ord("A")

                # Helps to encrypt by shifting uppercase letter
                if char.isupper():
                    encrypted_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
                
                # Helps to encrypt by shifting lowercase letter
                else:
                    encrypted_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
                
                encrypted_message.append(encrypted_char)
            
            else:
                encrypted_message.append(char)
        # Join the encrypted message
        return "".join(encrypted_message)
    
    # Decrypt the message
    def decrypt(self, message):
        decrypted_message = []
        extended_key = self._extend_key(message)
        for i in range(len(message)):
            char = message[i]
            if char.isalpha():
                # Create the shift value
                shift = ord(extended_key[i].upper()) - ord("A")

                # Helps to encrypt by shifting uppercase letter
                if char.isupper():
                    encrypted_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))

                # Helps to encrypt by shifting lowercase letter
                else:
                    encrypted_char = chr(((ord(char) - ord("a") - shift) % 26) + ord("a"))
                
                decrypted_message.append(encrypted_char)
            
            else:
                decrypted_message.append(char)
        return "".join(decrypted_message)