# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 29/10/2023
# File for Option 4: InferCaesarCipherKey.py

# import modules
import os
from datetime import datetime
from CaesarCipher import CaesarCipher
from CipherKeyAnalyzer import CipherKeyAnalyzer
from FileReaderWriter import FileReaderWriter

class InferCaesarCipherKey(CaesarCipher, CipherKeyAnalyzer, FileReaderWriter):
    def __init__(self, input_file="", referenced_file="", output_file="", ref_freq_dict = {}, message="", key=0):
        super().__init__(message, key)
        self.input_file = input_file
        self.referenced_file = referenced_file
        self.output_file = output_file
        self.ref_freq_dict = ref_freq_dict

    # Function to get input file
    def get_inputFile(self):
        while True:
            input_file = input("Please enter the file to analyze: ")

            # Checks if input file and path exists
            if os.path.exists(input_file) and os.path.isfile(input_file):
                self.input_file = input_file
                return
            # Repeats if input file and path does not exist
            else:
                print("Input file does not exist. Please try again.")

    # Function to read message from the file
    def get_message_from_inputFile(self):
        self.get_inputFile()
        self.message = self.readFile(self.input_file)

    # Function to get referenced file
    def get_referencedFile(self):
        while True:
            referenced_file = input("\nPlease enter the reference frequencies file: ")

            # Checks if referenced file and path exists
            if os.path.exists(referenced_file) and os.path.isfile(referenced_file):
                self.referenced_file = referenced_file
                return
            # Repeats if reference file and path does not exist
            else:
                print("Reference file does not exist. Please try again.")

    # Function to read content as a dictionary from referenced file
    def get_dict_from_referencedFile(self):
        self.get_referencedFile()

        content = self.readFile(self.referenced_file)
        lines = content.split("\n")
        for line in lines:
            if line:
                letter, value = line.strip().split(",")
                self.ref_freq_dict[letter] = float(value)
        return self.ref_freq_dict
    
    # Function to request if user wants to decrypt the file
    def get_decrypt_input(self, best_key):
        while True:
            answer = input(f'Would you like to decrypt this file using this key? y/n: ')
            if answer == "y":
                self.key = best_key
            elif answer == "n":
                self.key = self.getCipherKey()
            else:
                print("Invalid input. Please try again.")
                continue
            #Function from CaesarCipher.py
            decrypted_message = self.get_decrypted()
            return decrypted_message

    # Function to write to the file
    def set_message_to_outputFile(self, message):
        if os.path.exists(self.output_file) and os.path.isfile(self.output_file):
            existing_content = self.readFile(self.output_file)
            # Existing file has content
            if existing_content.strip():
                while True:
                    input_overwrite = input("\nContent is already in output file. Do you want to overwrite? (Y/N): ")
                    
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

    # Initiate option
    def init_option(self):
        self.get_message_from_inputFile()
        self.get_dict_from_referencedFile()

        # Function from CipherKeyAnalyzer.py
        best_key = self.get_best_key(self.message, self.ref_freq_dict)
        print(f"The inferred caesar cipher key is: {best_key}")

        decrypted_message = self.get_decrypt_input(best_key)
        self.output_file = input("\nPlease enter a output file: ")
        self.set_message_to_outputFile(decrypted_message)
