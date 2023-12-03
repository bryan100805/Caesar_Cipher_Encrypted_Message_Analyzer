# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 18/10/2023
# File for Option 2: FileCaesarCipher.py

# import modules
import os
from datetime import datetime
from CaesarCipher import CaesarCipher
from FileReaderWriter import FileReaderWriter

# Creating child class using inheritance from CaesarCipher parent class
class FileCaesarCipher(CaesarCipher, FileReaderWriter):
    def __init__(self, input_file="", output_file="",  message="", key=0):
        super().__init__(message, key)
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
            # Read for existing content in output file
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

                    # Overwrites existing file
                    elif input_overwrite == "Y":
                        existing_content = ""
                        break
                    
                    else:
                        print("Invalid input. Please try again.")
        # Creates a new file if output file does not exist
        # Write message to output file
        self.writeFile(self.output_file, message)

    def init_option(self):
        while True:
            choice = input("Enter 'E' for Encrypt or 'D' for Decrypt: ")
            if(choice == "E"):
                self.get_message_from_inputFile(choice)
                self.key = self.getCipherKey()
                encrypted_message = self.get_encrypted()
                self.output_file = input("\nPlease enter a output file: ")
                self.set_message_to_outputFile(encrypted_message)
                return
                
            elif(choice == "D"):
                self.get_message_from_inputFile(choice)
                self.key = self.getCipherKey()
                decrypted_message = self.get_decrypted()
                self.output_file = input("\nPlease enter a output file: ")
                self.set_message_to_outputFile(decrypted_message)
                return

            else:
                print("Invalid input. Please try again.")
