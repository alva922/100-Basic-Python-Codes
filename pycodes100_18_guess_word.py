# https://newdigitals.org/2024/02/24/100-basic-python-codes/#guess-a-word
# Guess a Word
# The function get_word returns a random word from a list of words
import random
 
def get_word():
    """
    This function returns a random word from a list of words
    """
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(word_list)
 
def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6
 
    # Loop until either the word is guessed or the lives run out
    while len(word_letters) > 0 and lives > 0:
        # Display the current state of the word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))
 
        # Get a user's guess
        user_letter = input("Guess a letter: ").lower()
 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Guess again.")
        else:
            print("Invalid character. Please enter a letter.")
 
    # The game has ended, display the result
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")
 
if __name__ == '__main__':
    play_game()
Output:
Current word:  _ _ _ _ _
Guess a letter: a
Current word:  _ _ a _ _
Guess a letter: c
Letter is not in word.
Current word:  _ _ a _ _
Guess a letter: e
Current word:  _ _ a _ e
Guess a letter: g
Current word:  g _ a _ e
Guess a letter: r
Current word:  g r a _ e
Guess a letter: p
You guessed the word grape !!
