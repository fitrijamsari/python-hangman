import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly pick any word from list
    while '-' in word or ' ' in word:
        word = random.choice(words) #selagi - and space ada dlm list, keep itterating

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join['a', 'b', 'cd'] --> 'a b cd'
        print('You have', lives, 'lives left and  you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter \n').upper()
        if user_letter in alphabet - used_letters: #if user input yg valid dalam alphabet xde dalam used_letter, then add masuk dlm used_letter
            used_letters.add(user_letter)
            if user_letter in word_letters: #if user input ada dalam word_letter, then remove user input letter dari word letter
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already use this character. Please guess other character')

        else:
            print('\nInvalid character. Please try again')
    
    # get here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

print(hangman())




