import random
words = ["love", "mango", "elephant", "biscuit", "sunflower", "green"]
secret_word = random.choice(words)
display = ["_"] * len(secret_word)
attempts = 6
print(" ".join(display))

while "_" in display and attempts > 0:
    guess = input("Guess a letter: ").lower()

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            display[i] = guess

    print(" ".join(display))

    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts = attempts - 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if "_" not in display:
    print("You won! The word was:", secret_word)
else:
    print("You lost! The word was:", secret_word)
