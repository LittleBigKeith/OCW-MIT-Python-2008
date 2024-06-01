import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "src/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

def ghost_continue(fragment, wordlist, players_turn):
    # Forming a word longer than 3 letters ("PEA" is ok, but "PEAR" is not).
    if len(fragment) > 3 and fragment.lower() in wordlist:
        print(f"Player {players_turn % 2 + 1} loses because '{fragment}' is a word!")
        return False
    # Creating a fragment (of any size) which cannot become a word by adding more letters (for example, "QZ").
    for word in wordlist:
        if word.startswith(fragment.lower()):
            return True
    print(f"Player {players_turn % 2 + 1} loses because no word begins with '{fragment}'!")
    return False

def ghost(wordlist):
    current_word_fragment = ""
    players_turn = 1
    print("Welcome to Ghost!")
    print("Player 1 goes first.")

    while True:
        print(f"Current word fragment: '{current_word_fragment}'")
        if len(current_word_fragment) > 0:
            if not ghost_continue(current_word_fragment, wordlist, players_turn):
                print(f"Player {players_turn} wins!")
                break
            print(f"Player {players_turn}'s turn.")
        alphabet = input(f"Player {players_turn} says letter: ").strip()
        if len(alphabet) != 1:
            print("Please say exactly one letter")
            print()
            continue
        if not alphabet in string.ascii_letters:
            print(f"{alphabet} is not a valid letter")
            print()
            continue
        current_word_fragment += alphabet.upper()
        players_turn = players_turn % 2 + 1
        print()