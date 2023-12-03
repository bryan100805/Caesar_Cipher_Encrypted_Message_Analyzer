# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 18/11/2023
# File: FileReaderWriter.py

# Creating parent class that read input files and write content to output file
class FileReaderWriter:
    def readFile(self, file):
        with open(file, "r") as file:
            return file.read()
        
    def writeFile(self, file, message):
        # Write the message to output file
        with open(file, "w") as file:
            file.write(message)

    def appendFile(self, file, message):
        # Append the message to file
        with open(file, "a") as file:
            file.write(message)