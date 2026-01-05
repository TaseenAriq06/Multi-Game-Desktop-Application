# hangman.py
# This project uses NLTK. Before running, install NLTK and download the words corpus:
# pip install nltk
# python -m nltk.downloader words

import random
import tkinter as tk
import nltk
from nltk.corpus import words

# Make a word list of valid words (4-9 letters, alphabetic only)
word_list = [w.lower() for w in words.words() if w.isalpha() and 4 <= len(w) <= 9]

def hangman():
    # Initialize game variables
    word = random.choice(word_list)
    guessed_letters = set() # letters guessed so far
    lives = 10
    display_word = ["_" for _ in word]

    # Function to update labels in GUI
    def update_display(message="", color="black"):
        word_label.config(text=" ".join(display_word))
        lives_label.config(text=f"Lives: " + "❌" * lives)
        guessed_label.config(text="Guessed: " + ", ".join(sorted(guessed_letters)))
        message_label.config(text=message, fg=color)
    
    # Function to restart game
    def restart():
            nonlocal word, display_word, guessed_letters, lives
            word = random.choice(word_list)
            display_word = ["_" for _ in word]
            guessed_letters = set()
            lives = 10
            guess_button.config(state="normal")
            update_display("Game Restarted!")
            return
    
    # Function to handle a guess
    def guess_letter():
        nonlocal lives

        guess = entry.get().lower()
        entry.delete(0, tk.END)
        
        # Check for valid input
        if not guess.isalpha():
            update_display("Letters only.")
            return
        
        # Full word guess
        if len(guess) == len(word):
            if guess == word:
                for i in range(len(word)):
                    display_word[i] = word[i]
                update_display(f"Nice guess, the word was {word}")
                guess_button.config(state="disabled")
            else:
                lives -= 1
                update_display("Wrong full word guess!")

        # Single letter guess
        elif len(guess) == 1:
            if guess in guessed_letters:
                update_display("Already guessed.")
                return
            guessed_letters.add(guess)
            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        display_word[i] = guess
                update_display("Correct!", color="green")
            else:
                lives -= 1
                update_display("Wrong!", color="red")
        else:
            update_display("Guess 1 letter or the full word ONLY")
            return
        
        # Check win/lose conditions
        if "_" not in display_word:
            update_display(f"You won! Word was: {word}")
            guess_button.config(state="disabled")
        elif lives <= 0:
            display_word[:] = list(word)
            update_display(f"You lost! Word was: {word}")
            guess_button.config(state="disabled")

    # Setup GUI
    root = tk.Tk()
    root.title("Hangman")
    root.geometry("400x300")
    root.configure(bg="#e7cef5")

    tk.Label(root, text="Hangman", font=("Georgia", 20),bg="#e7cef5").pack(pady=10)

    word_label = tk.Label(root, text=" ".join(display_word), font=("Courier", 24), bg="#e7cef5")
    word_label.pack(pady=10)

    lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Georgia", 14), bg="#e7cef5")
    lives_label.pack()

    guessed_label = tk.Label(root, text="Guessed:", font=("Georgia", 12), bg="#e7cef5")
    guessed_label.pack(pady=5)

    message_label = tk.Label(root, text="", font=("Georgia", 12), bg="#e7cef5", fg="black")
    message_label.pack(pady=5)

    entry = tk.Entry(root, font=("Georgia", 14), width=5)
    entry.pack(pady=10)

    guess_button = tk.Button(root, text="Guess", font=("Georgia", 14), command=guess_letter)
    guess_button.pack()

    tk.Button(root, text="Quit", font=("Georgia", 14), fg="red", command=root.destroy).place(x=0, y=260)
    tk.Button(root, text="Restart", font=("Georgia", 14), fg="blue", command=restart).place(x=320, y=260)
    update_display()
    root.mainloop()
