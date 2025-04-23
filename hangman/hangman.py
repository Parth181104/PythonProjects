import random

# List of words
words = ['UMBRELLA', 'TELESCOPE', 'SMARTPHONE']
word = random.choice(words)

# Initialize variables
total_chances = 7
guessed_word = "-" * len(word)

print("Word to guess:", guessed_word)

# Main game loop
while total_chances > 0:
    letter = input("Guess a Letter: ").upper()

    if letter in word:
        # Update guessed_word
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]
        print("Good guess!", guessed_word)
    else:
        total_chances -= 1
        print("Incorrect guess!")
        print("The remaining chances are:", total_chances)

    # Check if the player has won
    if guessed_word == word:
        print("Congratulations, you won!!!")
        break

# If the game ends and the word wasn't guessed
if guessed_word != word:
    print("GAME OVER")
    print("YOU LOSE")
    print("ALL CHANCES EXHAUSTED")
    print("The correct word was:", word)
