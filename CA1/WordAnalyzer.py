# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 19/11/2023
# File for Option 6: WordAnalyzer.py

import os, string, datetime
from FileReaderWriter import FileReaderWriter
from SortedList.SortedList import SortedList
from SortedList.FrequencyWordNode import FrequencyWordNode
from RecursiveBarGraph import RecursiveBarGraph

class WordAnalyzer(FileReaderWriter):
    def __init__(self, input_file="", word_freq={}):
        self.input_file = input_file
        self.word_freq = word_freq

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
        text = self.get_stopwordInput(text)
        self.word_freq_counter(text)
        sorted_freq = self.sort_frequency()
        return sorted_freq
    
    # Function to remove any stop words from the text. Source for stop words: https://www.ranks.nl/stopwords
    def remove_stop_words(self, text):
        stop_words = ['i', 'me', 'my', 'mysel', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", 
            "you'll", "you'd", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
            "she", "she's", "her", "hers", "herself", "it", "it's", "its", "itself", "they", "them", "their",
            "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "that'll", "these", "those",
            "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does",
            "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
            "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", 
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
            "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", 
            "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same",
            "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "don't", "should", "should've", "now",
            "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "aren't", "couldn", "couldn't", "didn", "didn't", "doesn",
            "doesn't", "hadn", "hadn't", "hasn", "hasn't", "haven", "haven't", "isn", "isn't", "ma", "mightn", "mightn't", "mustn", 
            "mustn't", "needn", "needn't", "shan", "shan't", "shouldn", "shouldn't", "wasn", "wasn't", "weren", "weren't", "won", 
            "won't", "wouldn", "wouldn't"]
        # Remove stop words
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        
        return ' '.join(filtered_words)
    
    # Function to remove stop words from the text
    def get_stopwordInput(self, text_file):
        while True:
            answer = input("Do you want to remove stop words? (Y/N): ")
            if answer == "Y":
                text = self.remove_stop_words(text_file)
                return text
            elif answer == "N":
                return text_file
            else:
                print("Invalid input. Please try again.")
                

    # Function to remove any punctuations from the text
    def remove_punctuations(self, text):
        # Remove punctuations
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text
    
    # Function to count the number of words in the text
    def word_freq_counter(self, text):
        # Remove any punctuations from the text
        text = self.remove_punctuations(text)
        # Split the text into words
        words = text.split()
        # Create a dictionary to store the word and its frequency
        self.word_freq = {}

        for word in words:
            word = word.lower()
            # If the word is not in dictionary, add it to the dictionary
            if word not in self.word_freq:
                self.word_freq[word] = 1
            # If the word is in dictionary, increment its frequency
            else:
                self.word_freq[word] += 1
        return self.word_freq

    # Sorting the top 5 frequencies in descending order
    def sort_frequency(self):
        sortedList = SortedList()
        for key, value in self.word_freq.items():
            sortedList.insert_largest_first(FrequencyWordNode(key, value))

        # Return the top 5 Frequencies
        top5_freq = sortedList.get_top(5)
        return top5_freq
    
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
        initial_heading = f"Number of Occurences of Words in {self.input_file}\n"
        self.writeFile(self.output_file, initial_heading)
        self.format_content(self.output_file, message)

    # Function to update the file with content
    def format_content(self, file, content):
        for item in content:
            self.appendFile(file, f"{str(item)}\n")

    # Initiate Option
    def init_option(self):
        self.get_inputFile()
        sorted_freq = self.load_inputFile()
        self.output_file = input("\nPlease enter a output file: ")
        self.set_message_to_outputFile(sorted_freq)

        # Draw the bar graph
        bar_graph = RecursiveBarGraph()
        bar_graph.draw_bar_graph(sorted_freq)