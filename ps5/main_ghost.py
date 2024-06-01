from src.ps5_ghost import *

if __name__ == '__main__':
    # Actually load the dictionary of words and point to it with 
    # the wordlist variable so that it can be accessed from anywhere
    # in the program.
    wordlist = load_words()
    ghost(wordlist)