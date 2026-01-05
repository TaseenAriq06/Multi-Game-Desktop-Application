# main.py - Game Hub
# This file is the main launcher for all three games: Rock-Paper-Scissors, Hangman, and Memory Game.

from rockpaper import rock_paper_scissors
from hangman import hangman
from memorygame import memory_game

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Play A Game")
root.geometry("400x300")
root.configure(bg="Moccasin")

# Title label
title = tk.Label(root, text="Choose A Game To Play 🎮", font=("Georgia", 18), bg="Moccasin")
title.pack(pady=15)

# Functions to start each game
def start_rps():
    root.destroy()          # Close the hub window
    rock_paper_scissors()   # Launch RPS game

def start_hangman():
    root.destroy()
    hangman()               # Launch Hangman game

def start_memory():
    root.destroy()
    memory_game()           # Launch Memory Game

# Buttons for each game
tk.Button(root, text="       Rock, Paper, Scissors 🪨📃✂️", bg="purple", fg="white", font=("Georgia", 14), width=25, command=start_rps).pack(pady=10)
tk.Button(root, text="Hangman 🪢", bg="green", fg="white", width=25, font=("Georgia", 14), command=start_hangman).pack(pady=10)
tk.Button(root, text="Memory Game 🧠", bg="blue", fg="white", width=25, font=("Georgia", 14), command=start_memory).pack(pady=10)
tk.Button(root, text="Quit ❌", bg="red", fg="white", width=25, font=("Georgia", 14), command=root.destroy).pack(pady=10)

root.mainloop()
