#1.Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file():
    try:
        with open("ABC.txt", "r") as file:
            for line in file:
                print(line.strip())  
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")
read_file()

#2.Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words():
    try:
        with open("ABC.txt", "r") as file:
            word_count = sum(len(line.split()) for line in file)
        print(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")
count_words()

#3.Write a function in Python to count uppercase character in a text file “ABC.txt”

def count_uppercase():
    try:
        with open("ABC.txt", "r") as file:
            uppercase_count = sum(sum(1 for char in line if char.isupper()) for line in file)
        print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")
count_uppercase()

#4.Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters

def display_words():
    try:
        with open("story.txt", "r") as file:
            for line in file:
                words = [word for word in line.split() if len(word) < 4]
                print(" ".join(words))
    except FileNotFoundError:
        print("Error: The file 'story.txt' was not found.")
display_words()
