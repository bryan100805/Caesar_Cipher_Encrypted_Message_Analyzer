# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 30/10/2023
# File for Option 5: FileBatchProcessing.py

import os
from CaesarCipher import CaesarCipher
from CipherKeyAnalyzer import CipherKeyAnalyzer
from FileReaderWriter import FileReaderWriter
from SortedList.SortedList import SortedList
from SortedList.CipherKeyNode import CipherKeyNode

import datetime

class FileBatchProcessing(CaesarCipher, CipherKeyAnalyzer, FileReaderWriter):
    def __init__(
            self, 
            folder ="", 
            input_files=[], 
            referenced_file="", 
            log="",
            output_files=[], 
            ref_freq_dict = {},
            message={}, 
            key={}
        ):
        super().__init__(message, key)
        self.folder = folder
        self.input_files = input_files
        self.referenced_file = referenced_file
        self.log = log
        self.output_files = output_files
        self.ref_freq_dict = ref_freq_dict

    # Function to get folder
    def get_folder(self):
        while True:
            folder = input("Please enter the folder name: ")

            # Checks if folder exists
            if os.path.exists(folder):
                folder_contents = os.listdir(folder)
                # Checks if folder contains files
                if folder_contents:
                    return folder
                else:
                    print("Folder is empty. Please try again.")

            else:
                print("Folder does not exist. Please try again.")
    
    # Function to read message from the file
    def get_message_from_inputFiles(self, file):
        message = self.readFile(file)

        # Store file name as key and message as the value
        self.message[file] = message
    
    # Function to get input_files from folder              
    def get_input_files(self):
        folder_contents = os.listdir(self.folder)
        for file in folder_contents:
            # Ensure that the file is not an output file or log file
            if file.endswith(".txt") and not file.startswith("file") and not file.startswith("log"):
                file_path = self.folder + "/" + file

                self.get_message_from_inputFiles(file_path)

    # Function to break down reference file into dictionary
    def get_dict_from_referencedFile(self):

        # Assumes that reference file is englishtext.txt since brief did not specify
        self.referenced_file = "englishtext.txt"

        content = self.readFile(self.referenced_file)
        lines = content.split("\n")
        for line in lines:
            if line:
                letter, value = line.strip().split(",")
                self.ref_freq_dict[letter] = float(value)
        return self.ref_freq_dict

    # Converts array to dictionary 
    def array_to_dict(self, array):
        dict ={}
        for i in range(len(array)):
            # Split by : to get the file_name and key
            file_name, key = str(array[i]).split(":")
            dict[file_name] = int(key)

        return dict    
    
    # Function to sort the files according to the cipher keys
    def sort_files(self):
        sortedList = SortedList()
        for file, key in self.key.items():
            sortedList.insert_smallest_first(CipherKeyNode(file, key))
            
        sorteditems = sortedList.get_top(len(sortedList))
        self.key = self.array_to_dict(sorteditems)

    # Function to find the best cipher key in the files
    def get_bestKeys_in_files(self):
        self.key={}
        for file in self.message:
            best_key = self.get_best_key(self.message[file], self.ref_freq_dict)
            self.key[file] = best_key    
        self.sort_files()
    
    # Function to retrieve decrypted files and write to output files
    def get_decrypted_files(self):
        self.input_files = []  # Reset input_files list
        self.output_files = []  # Reset output_files list
        file_counter = 0
        for file in self.key:
            file_counter += 1
            
            # Store file name in list
            self.input_files.append(file)

            #Function from CaesarCipher.py to decrypt message based on the cipher keys
            decrypted_message = self.get_file_decrypted(self.message[file], self.key[file])
            self.set_message_to_outputFile(decrypted_message, file_counter)

    def set_log_file(self):
        log_file = f"{self.folder}/log.txt"

        # Checks if output file exists
        if os.path.exists(log_file) and os.path.isfile(log_file):
            check_content = self.readFile(log_file)
            
            # If existing file has content, clear content for overwrite
            if check_content.strip():
                check_content = ""

        output_file_counter = 0
        self.log = ""

        # Adds the timestamp to the log file of every batch processing
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        time_stamp_message = f"Batch Processing at: {timestamp}\n"
        self.appendFile(log_file, time_stamp_message)

        # Write the log to log file
        for input_file, cipher_key in self.key.items():
            input_file = input_file.split("/")[-1]
            log = f"Decrypting: {input_file} with key: {cipher_key} as: {self.output_files[output_file_counter]}\n"

            # Updates the log file
            self.appendFile(log_file, log)
            self.log += log

            # Adds new line if not last file
            if output_file_counter < len(self.key):
                self.log += "\n"
            output_file_counter += 1

    # Function to write to the file
    def set_message_to_outputFile(self, decrypted_message, file_counter):
        output_file = f"file{file_counter}.txt"
        output_file_path = f"{self.folder}/{output_file}"

        # Checks if output file exists
        if os.path.exists(output_file_path) and os.path.isfile(output_file_path):
            existing_content = self.readFile(output_file_path)
            
            # If existing file has content, clear content for overwrite
            if existing_content.strip():
                existing_content = ""

    
        self.output_files.append(output_file)
        # Write the message to output file
        self.writeFile(output_file_path, decrypted_message)

    # Initiate the option
    def init_option(self):
        self.folder = self.get_folder()
        self.get_input_files()
        self.get_dict_from_referencedFile()
        self.get_bestKeys_in_files()
        self.get_decrypted_files()
        self.set_log_file()
        print(self.log)