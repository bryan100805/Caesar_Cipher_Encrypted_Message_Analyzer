# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 31/10/2023
# File for Option 6: FileVigenereCipher.py

# import modules
import os
from datetime import datetime
from VignereCipher import VignereCipher
from FileReaderWriter import FileReaderWriter


# Creating child class using inheritance from VignereCipher parent class
class FileVignereCipher(VignereCipher, FileReaderWriter):
    def __init__(self, input_file="", output_file="", message="", key="DEFAULT"):
        super().__init__(key)
        self.message = message
        self.input_file = input_file
        self.output_file = output_file

    def get_inputFile(self, choice):
        while True:
            if choice == "E":
                input_file = input("\nPlease enter the file you want to encrypt: ")
            elif choice == "D":
                input_file = input("\nPlease enter the file you want to decrypt: ")
            # Checks if input file and path exists
            if os.path.exists(input_file) and os.path.isfile(input_file):
                self.input_file = input_file
                return
            # Repeats if input file and path does not exist
            else:
                print("Input file does not exist. Please try again.")

    # Function to read from the file
    def get_message_from_inputFile(self, choice):
        self.get_inputFile(choice)
        self.message = self.readFile(self.input_file)

    # Function to write to the file
    def set_message_to_outputFile(self, message):
        if os.path.exists(self.output_file) and os.path.isfile(self.output_file):
            existing_content = self.readFile(self.output_file)

            # Existing file has content
            if existing_content.strip():
                while True:
                    input_overwrite = input(
                        "\nContent is already in output file. Do you want to overwrite? (Y/N): "
                    )

                    # Automatically creates a new file with the same name and current timestamp
                    if input_overwrite == "N":
                        base, ext = os.path.splitext(self.output_file)
                        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                        self.output_file = f"{base}_{timestamp}{ext}"
                        break

                    # Overwrites exisiting file
                    elif input_overwrite == "Y":
                        existing_content = ""
                        break
                    
                    else:
                        print("Invalid input. Please try again.")

        # Write the message to output file
        self.writeFile(self.output_file, message)

    def init_option(self):
        # What is Vignere Cipher?
        print(
            "The Vigenère Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.\n"
            "A polyalphabetic cipher uses multiple substitution alphabets to encrypt the plain text, making it more secure than \n"
            "a simple Caesar Cipher.\n")

        # How Vigènere Cipher works?
        print(
            "How Vigènere Cipher works?\n"
            "1) The Vigenère Cipher uses a 26x26 table with A to Z as the row heading and column heading\n"
            "2) The key is a word or phrase that is used to encrypt the message. The key is repeated until it matches the length of the message\n"
            "3) The first letter of the message is encrypted using the first letter of the key, and so on\n"
            "4) The encrypted message is decrypted by reversing the process\n"
        )

        while True:
            choice = input("Enter 'E' for Encrypt or 'D' for Decrypt: ")
            if(choice == "E"):
                self.get_message_from_inputFile(choice)
                self.key = self.getVignereCipherKey()
                encrypted_message = self.encrypt(self.message)
                self.output_file = input("\nPlease enter a output file: ")
                self.set_message_to_outputFile(encrypted_message)
                return
                
            elif(choice == "D"):
                self.get_message_from_inputFile(choice)
                self.key = self.getVignereCipherKey()
                decrypted_message = self.decrypt(self.message)
                self.output_file = input("\nPlease enter a output file: ")
                self.set_message_to_outputFile(decrypted_message)
                return

            else:
                print("Invalid input. Please try again.")
