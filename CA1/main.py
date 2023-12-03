# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 18/10/2023
# File: main.py

# Import modules
from MessageCaesarCipher import MessageCaesarCipher
from FileCaesarCipher import FileCaesarCipher
from AnalyzeLetterFrequencyDistribution import AnalyzeLetterFrequencyDistribution
from InferCaesarCipherKey import InferCaesarCipherKey
from FileBatchProcessing import FileBatchProcessing
from WordAnalyzer import WordAnalyzer
from FileVignereCipher import FileVignereCipher

# Function to display title bar
def display_title_bar():
    title_bar = f"""
{'*'*57}
* ST1507 DSAA: Welcome to:                              *
*{' '*55}*
*    ~ Caesar Cipher Encrypted Message Analyzer ~       *
*{' '*55}*
*  - Done by: Tan Wen Tao Bryan(2214449)                *
*  - Class DAAA/2B/01                                   *
{'*'*57}


"""
    print(title_bar)


# Function to display selection menu
def display_menu():
    selection_menu = input(
        f"""
Please select your choice: (1,2,3,4,5,6,7,8)
        1. Encrypt/Decrypt Message
        2. Encrypt/Decrypt File
        3. Analyze letter frequency distribution
        4. Infer caesar cipher key from file
        5. Analyze, and sort encrypted files
        6. Analyze word frequency in files
        7. Vigènere File Encryption/Decryption
        8. Exit
Enter choice: """
    )
    return selection_menu



# Run the app
def run():
    display_title_bar()
    input("Please enter key, to continue....")

    # Create instance of classes
    messageCaesarCipher = MessageCaesarCipher()
    fileCaesarCipher = FileCaesarCipher()
    letterFrequencyAnalyzer = AnalyzeLetterFrequencyDistribution()
    cipherKeyAnalyzer = InferCaesarCipherKey()
    fileBatchProcessing = FileBatchProcessing()
    wordAnalyzer = WordAnalyzer()
    fileVignereCipher = FileVignereCipher()

    # Dictionary of menu option to choose from
    menu_options = {
        "1": messageCaesarCipher.init_option,
        "2": fileCaesarCipher.init_option,
        "3": letterFrequencyAnalyzer.init_option,
        "4": cipherKeyAnalyzer.init_option,
        "5": fileBatchProcessing.init_option,
        "6": wordAnalyzer.init_option,
        "7": fileVignereCipher.init_option
    }

    while True:
        choice = display_menu()
        print()
        if choice in menu_options:
            selected_choice = menu_options[choice]
            # Run the selected choice
            selected_choice()
            input("\nPlease enter key, to continue....")
        elif choice == "8":
            print(
                f"Bye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer"
            )
            break
        else:
            print("Invalid Option. Please select the available options (1-8)")


# Runs if the program is the main, checks if the script being run directly as the main program
if __name__ == "__main__":
    run()
