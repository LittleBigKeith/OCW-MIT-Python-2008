import random
import math
import time
from itertools import combinations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WORDLIST_FILENAME = "src/words.txt"

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
rearrange_dict = dict()
points_dict = dict()

time_limit = 0

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES.get(letter)
    if len(word) == n:
        score += 50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")              # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = math.ceil(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = dict()
    for letter in hand:
        if hand.get(letter) > word.count(letter):
            new_hand.update({letter: hand.get(letter) - word.count(letter)})
    return new_hand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    if word.strip().lower() not in points_dict:
        return False
    for letter in word:
        if not hand.get(letter) or hand.get(letter) < word.count(letter):
            return False
    return True
    

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    total_score = 0
    word_time = 0
    time_left = time_limit
    while True:
        # * The sum of the word scores is displayed when the hand finishes.
        if len(hand) == 0:
            print(f"Total score: {total_score:.2f} points.")
            break

        # * The hand is displayed.
        print("Current Hand:", end=" ")
        display_hand(hand)

        # * The user may input a word.
        start_time = time.time()
        #current_word = input("Enter word, or a . to indicate that you are finished: ")
        current_word = pick_best_word_faster(hand)
        end_time = time.time()
        word_time += end_time - start_time

        # * The hand finishes when there are no more unused letters.
        #   The user can also finish playing the hand by inputing a single
        #   period (the string '.') instead of a word.
        if current_word.strip() == ".":
            # * The final score is displayed.
            print(f"Total score: {total_score:.2f} points.")
            break

        # * An invalid word is rejected, and a message is displayed asking
        #   the user to choose another word.
        if not is_valid_word(current_word, hand):
            print("Invalid word, please try again.")
            continue

        print(f"It took {word_time:.2f} seconds to provide an answer.")
        time_left -= word_time
        if time_left <= 0:
            print(f"Total time exceeds {time_limit} seconds. You scored {total_score:.2f} points.")
            break
        # * When a valid word is entered, it uses up letters from the hand.
        hand = update_hand(hand, current_word)

        # * After every valid word: the score for that word and the total
        #   score so far are displayed, the remaining letters in the hand 
        #   are displayed, and the user is asked to input another word.
        # * The player had 1 second to input an answer and get max possible score
        scaled_word_time = max(word_time, 1)
        word_time = 0
        word_score = get_word_score(current_word, HAND_SIZE) / scaled_word_time
        total_score += word_score
        print(f"{current_word} earned {word_score:.2f} points. Total: {total_score:.2f} points")


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    get_words_to_points(word_list)
    get_words_to_rearrange(word_list)
    global time_limit
    '''
    while True:
        time_limit = input("Enter time limit, in seconds, for players: ").strip()
        try:
            time_limit = int(time_limit)
        except ValueError:
            try:
                time_limit = float(time_limit)
            except ValueError:
                print("Time limit must be a number!")
                continue
        if time_limit <= 0:
            print("Time limit must be greater than 0!")
        else:
            break
    '''
    time_limit = get_time_limit(0.9)
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print()
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print()
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")

# Build data structures used for entire session and play game

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value. 
    """
    global points_dict
    for word in word_list:
        score = 0
        for letter in word:
            score += SCRABBLE_LETTER_VALUES.get(letter)
        points_dict.update({word: score})

def get_words_to_rearrange(word_list):
    """
    Return a dict that maps every letter combination in word_list to a word.
    """
    global rearrange_dict
    for word in word_list:
        sorted_word = "".join(sorted(word))
        rearrange_dict.update({sorted_word: word})

def pick_best_word(hand):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """
    current_best = ('.', 0)
    for word in points_dict:
        if is_valid_word(word, hand) and get_word_score(word, HAND_SIZE) > current_best[1]:
            current_best = (word, points_dict.get(word))
    return current_best[0]

def pick_best_word_faster(hand):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """
    current_best = ('.', 0)
    for combo in get_combinations_from_hand(hand):
        if combo in rearrange_dict:
            word = rearrange_dict.get(combo)
            points = points_dict.get(word)
            if points > current_best[1]:
                current_best = (word, points)
    return current_best[0]

def get_time_limit(k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

def get_combinations_from_hand(hand):
    letter_list = []
    for letter in hand:
        for _ in range(hand.get(letter)):
            letter_list.append(letter)

    combinations_list = []
    for length in range(HAND_SIZE):
        combinations_list += list(set("".join(sorted(t)) for t in combinations(letter_list, length + 1)))
    
    return combinations_list

## Problem 5 ##
# The time complexity of pick_best_word is
# O(size of word_list)
# The for loop inside pick_best_word compares
# the current best word and every single word
# from word_list one by one.
#
# The time complexity of pick_best_word_faster is
# O(2^(number of letters in a hand)), since this is
# the time compelxity of finding all possible combinations
# of letters of length 1 up to n.
# [nC1 + nC2 + ... + nCn == 2^n - 1]