# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 30/10/2023
# File: CipherKeyAnalyzer.py

import string

# Creating parent class that analyzes the best cipher key automatically
class CipherKeyAnalyzer:
    
    # Function that uses chi-square test to calculate the key
    # Measure of how well the observed letter frequencies in a text match the expected letter frequencies
    def calculate_chi_square(self, observed, expected):
        chi_square = 0
        # Calculates how each letter contributes to the chi-square statistic and sums them
        chi_square += sum(((observed.get(letter, 0) - expected[letter]) ** 2)/expected[letter] for letter in string.ascii_uppercase)
        return chi_square
    
    # Function to calculate letter frequencies
    def calculate_letterFrequencies(self, text):
        text = text.upper()
        upperCase_alphabet = string.ascii_uppercase
        # Calculates total number of letters in text
        totalLetters = sum(text.count(letter) for letter in upperCase_alphabet)
        # Calculates the frequency of each letter in text
        letter_frequencies = {
            letter: text.count(letter) / totalLetters for letter in upperCase_alphabet
        }
        return letter_frequencies
    
    # Function to shift a letter by a given amount
    def shift_letter(self, letter, shift):
        if letter.isalpha():
            # Calculates the Unicode of the letter and subtract the specified shift value from it
            shifted_code = ord(letter) - shift
            # Checks if shifted code is less than the Unicode of A
            if shifted_code < ord("A"):
                # Adds 26 to shifted code to wrap around to the alphabet
                shifted_code += 26
            # Converts shifted code back to a letter
            return chr(shifted_code)
        else:
            return letter

    # Function to find the best Caesar Cipher key
    # master_freq_dict is the referenced file dictionary
    def find_best_caesar_key(self, encrypted_text, master_freq_dict):
        best_key = 0
        min_chi_square = float("inf")
        # Iterates through all possible keys
        for shift in range(len(string.ascii_uppercase)):
            shifted_text = "".join(
                [self.shift_letter(letter, shift) for letter in encrypted_text.upper()]
            )
            text_freq = self.calculate_letterFrequencies(shifted_text)
            chi_square = self.calculate_chi_square(text_freq, master_freq_dict)
            
            # Checks if the chi-square value is less than the current minimum chi-square value
            if chi_square < min_chi_square:
                # Updates the min chi-square value and best key
                min_chi_square = chi_square
                best_key = shift
        return best_key
    
    # Retrieve the best key
    def get_best_key(self, encrypted_text, ref_freq_dict):
        encrypted_text = encrypted_text.upper() # Encrypted text
        master_freq = ref_freq_dict  # Referenced file dictionary
        best_shift = self.find_best_caesar_key(encrypted_text, master_freq)
        return best_shift