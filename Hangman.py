
import random
import hangman_words
import art
chosen_word=random.choice(hangman_words.word_list)
from art import stages
from art import logo
print(logo)
# instead of above two lines you can just use "from hangman_words import word_list"
length = len(chosen_word)
correct_letters=[]
game_over=False
lives = 6
while not game_over:
    guess=input("Guess a letter ").lower()
    display = "" 
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
                display += letter
        else:
            display += "_"
    print (display)
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
    if guess not in chosen_word:
        lives -= 1
    print(stages[lives])
    if lives == 0:
        game_over = True
        print("You lose.")
        print(f"The word was {chosen_word}.")
    else:
        print(stages[lives])
    if "_" not in display:
            game_over = True
            print("You win!")

        
