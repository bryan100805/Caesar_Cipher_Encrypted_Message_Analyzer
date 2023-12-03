# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 18/10/2023
# File for Option 1: MessageCaesarCipher.py

# import modules
from CaesarCipher import CaesarCipher


# Creating child class using inheritance from CaesarCipher parent class
class MessageCaesarCipher(CaesarCipher):
    def __init__(self, message="", key=0):
        super().__init__(message, key)

    def getMessage(self, choice):
        if choice == "E":
            self.message = input("\nPlease type text you want to encrypt:\n")
        elif choice == "D":
            self.message = input("\nPlease type text you want to decrypt:\n")

    def print_ciphered(self, choice, ciphered_message):
        if choice == "E":
            print(f"Plaintext:     {self.message}")
            print(f"Ciphertext:    {ciphered_message}")
        elif choice == "D":
            print(f"Ciphertext:    {self.message}")
            print(f"Plaintext:     {ciphered_message}")

    def init_option(self):
        while True:
            choice = input("Enter 'E' for Encrypt or 'D' for Decrypt: ")
            if(choice == "E"):
                self.getMessage(choice)
                self.key = self.getCipherKey()
                print()
                encrypted_message = self.get_encrypted()
                self.print_ciphered(choice, encrypted_message)
                return
            
            elif(choice == "D"):
                self.getMessage(choice)
                self.key = self.getCipherKey()
                print()
                decrypted_message = self.get_decrypted()
                self.print_ciphered(choice, decrypted_message)
                return

            else:
                print("Invalid input. Please try again.\n")
