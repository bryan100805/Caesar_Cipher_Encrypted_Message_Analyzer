# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 21/10/2023
# File for Option 3: AnalyzeLetterFrequencyDistribution.py
import os, string, math
from FileReaderWriter import FileReaderWriter
from SortedList.SortedList import SortedList
from SortedList.FrequencyCharNode import FrequencyCharNode

# Displays the letter frequency distribution in the form of a graph
class AnalyzeLetterFrequencyDistribution(FileReaderWriter):
    def __init__(
        self,
        inputFile="",
        char_frequency={},
        char_frequency_percentage ={},
        star_frequency={},
        graph=[],
        alphabet_counter=0,
        height=27,
        width=78,
    ):
        self.inputFile = inputFile
        self.char_frequency = char_frequency
        self.char_frequency_percentage = char_frequency_percentage
        self.star_frequency = star_frequency
        self.graph = graph
        self.alphabet_counter = alphabet_counter
        self.height = height
        self.width = width

    # Function to get input file
    def get_inputFile(self):
        while True:
            self.input_file = input("Please enter the file you want to analyse: ")
            # Checks if input file and path exists
            if os.path.exists(self.input_file) and os.path.isfile(self.input_file):
                return
            # Repeats if input file and path does not exist
            else:
                print("Input file does not exist. Please try again.")

    # Function to load input file like reading the message in the file
    def load_inputFile(self):
        text = self.readFile(self.input_file)
        # Function from caesar_cipher.py
        self.calculate_frequency(text)
        self.calculate_percentage()
        self.calculate_no_of_stars(self.char_frequency_percentage)


    # Function to set default frequency of each alphabet to 0
    def setDefaultCharFrequency(self):
        alphabet_upper = string.ascii_uppercase
        for char in alphabet_upper:
            self.char_frequency[char] = 0

    # Function to calculate frequency of each alphabet
    def calculate_frequency(self, text):
        self.setDefaultCharFrequency()

        # Store frequency of each character in a dictionary
        for char in text:
            # Check if character is an alphabet
            if char.isalpha():
                # Turn all the alphabet to uppercase
                char = char.upper()
                # Retrive the frequency of the character and add 1 to in everytime present in text
                self.char_frequency[char] = self.char_frequency.get(char, 0) + 1

    def calculate_percentage(self):
        # Sum up total number of alphabets frequency
        total = sum(self.char_frequency.values())

        if total == 0:
            print("No content detected in text file. Please try again.")
            self.get_inputFile()

        for char in self.char_frequency:
            # Convert to percentage and round off to 2 decimal places
            self.char_frequency_percentage[char] = round(
                (self.char_frequency[char] / total * 100), 2
            )
        return self.char_frequency_percentage

    # Calculate the number of stars to be displayed
    def calculate_no_of_stars(self, character_dict):
        # Treat the height of the graph to be 100%
        for key, value in character_dict.items():
            self.star_frequency[key] = math.ceil(value / 100 * (self.height - 1))

    # Sorting the top 5 frequencies in descending order
    def sort_frequency(self):
        sortedList = SortedList()
        for key, value in self.char_frequency_percentage.items():
            sortedList.insert_largest_first(FrequencyCharNode(key, value))

        # Return the top 5 Frequencies
        top5_freq = sortedList.get_top(5)
        return top5_freq

    # Function to generate letter frequency distribution graph
    def drawBorders(self):
        # Reinitalize the variables
        # 2D graph to store the graph
        self.graph = []
        self.alphabet_counter = 0
        alphabet_upper = string.ascii_uppercase

        # Draw the borders of the graphs (right and bottom)
        for row in range(self.height + 1):
            row_output = []
            for col in range(self.width + 1):
                # Take cares of the columns within the "_" line
                if col != self.width:
                    # Bottom border
                    if row == self.height - 1:
                        row_output.append("_")
                    # Last row
                    elif row == self.height:
                        # Ensure alphabets are printed every (col+2) % 3==0 column
                        if (col + 2) % 3 == 0:
                            row_output.append(
                                alphabet_upper[self.alphabet_counter]
                            )
                            self.alphabet_counter += 1
                        # Intervals between alphabets in the x-axis
                        else:
                            row_output.append(" ")
                    # Spaces in around the graph
                    else:
                        row_output.append(" ")

                # Take cares of the columns after the "_" line
                else:
                    # Right border
                    if row != self.height:
                        row_output.append("| ")

                    # After every column of the graph, print the frequency
                    if 0 <= row < len(alphabet_upper):
                        letter = alphabet_upper[row]
                        freq_percentage = self.char_frequency_percentage[letter]
                        # Print the percentage frequency of the alphabet
                        row_output.append(f"{letter}- {freq_percentage:.2f}%")
                        if row == 10:
                            row_output.append("\tTOP 5 FREQ")
                        if row == 11:
                            row_output.append(f"\t{'-'*10}")
                        # Add the top 5 frequencies to the graph
                        row_freq = 12
                        for node in self.sort_frequency():
                            if row == row_freq:
                                row_output.append(f"{node}")
                            row_freq += 1

            # Append the row to the 2D graph
            self.graph.append(row_output)

    # Function to draw the stars
    def drawStars(self):
        self.drawBorders()

        # Set the starting position of the stars
        firstStar_position = self.height - 2
        col_offset = 1

        # Loop through the dictionary to assess the stars to be drawn
        for stars in self.star_frequency.values():
            for star in range(stars + 1):
                if star != 0:
                    row = firstStar_position
                    # Draw the stars
                    self.graph[row][col_offset] = "*"
                    # Move the row up by 1 if there are more stars to be drawn
                    firstStar_position -= 1
            # Reset the starting position of the stars
            firstStar_position = self.height - 2
            # Move the column to the next letter
            col_offset += 3
        return self.graph

    # Display the graph
    def display_letter_frequency(self):
        for row in self.drawStars():
            print("".join(row))

    # Function to initialize option
    def init_option(self):
        self.get_inputFile()
        self.load_inputFile()
        print()
        self.display_letter_frequency()