import string
from words import words
import random

def valid_word(words):
    valid_word = random.choice(words)
    while '-' in valid_word or ' ' in valid_word:
        valid_word = random.choice(words)
    
    return valid_word.upper()


def hangman():
    word = valid_word(words)
    word_letters = set(word)
    used_letters =set()
    alphabet = set(string.ascii_uppercase)
    life = 6
    print(word)
    print(word_letters)
    while len(word_letters) > 0 and life > 0:
        print("Eneterd words are :"+ ' '.join(used_letters))
        current_Word = [letter if letter in used_letters else '_' for letter in word ]
        print(current_Word)
        user_letters = input('Guess the letter : ')
        if user_letters in alphabet-used_letters:
            used_letters.add(user_letters)
            if(user_letters in word_letters):
                word_letters.remove(user_letters)

            else:
                print("Enter any other letter")
                life = life-1
        elif(user_letters in used_letters):
            print("Alreday used this letter")
        else:
            print("Invalid token")
    if(len(word_letters) == 0):
        print(f"You won! Word is {word}")
    if(life == 0 ):
        print(f"You failed")




    

        


hangman()