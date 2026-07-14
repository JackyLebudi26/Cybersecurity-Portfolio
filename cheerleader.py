# Step 1 — Get the word from the user
word = input("Enter your favourite word: ")

# List of vowels
vowels = ["a", "e", "i", "o", "u"]

# Step 2 — Cheer each letter
for letter in word:
    # Check if the letter is a vowel (ignore uppercase/lowercase)
    if letter.lower() in vowels:
        print(f"Give me an {letter.upper()}!")
    else:
        print(f"Give me a {letter.upper()}!")

# Step 3 — Grand finale
print(f"What does it say????? {word.upper()}!!!!!!")
