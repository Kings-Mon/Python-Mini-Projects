# Main HangMan Game Solution :- 
# ================================================================================================================================================ #

import random
import word_file
import hangman_stages

print("- : Welcome To HangMan : -")

chosen_word = random.choice(word_file.words)
print(chosen_word)

display = ['_'] * len(chosen_word)
print(display)

game_over = False
max_attempts = 6
guessed_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        max_attempts -= 1
        print("Incorrect guess. Attempts left:", max_attempts)

    print("Current state: ", " ".join(display))
    print(hangman_stages.stages[max_attempts])

    if max_attempts == 0:
        game_over = True
        print("Sorry, you've run out of attempts. The word was:", chosen_word)
    elif set(guessed_letters) == set(chosen_word):
        game_over = True
        print("Congratulations! You've guessed the word:", chosen_word)

# ================================================================================================================================================ #