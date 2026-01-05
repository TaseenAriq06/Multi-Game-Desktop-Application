# memorygame.py
# Memory matching card game using tkinter

import random
import tkinter as tk

def memory_game():
    # Initialize window
    root = tk.Tk()
    root.title("Memory Card Game")
    root.geometry("325x620")
    root.configure(bg="#edafbf")

    # Card setup
    emojis = ["🐶","🐱","🦊","🐸","🐵","🐼","🦁","🐷"]
    card_values = emojis * 2
    random.shuffle(card_values)
    attempts = 0
    flipped = []
    matched = set()

    # Label to show attempts
    attempts_label = tk.Label(root, text=f"Attempts: {attempts}", font=("Georgia", 20), bg="#edafbf")
    attempts_label.place(x=20, y=560)

    # Function to handle flipping a card
    def flip_card(i, btn):
        if i in matched or btn['state'] == 'disabled':
            return

        btn.config(text=card_values[i], state="disabled", bg="lightgreen")
        flipped.append((i, btn))

        if len(flipped) == 2:
            for b in buttons:
                b.config(state="disabled")
            root.after(500, check_match)

    # Function to check for matching cards
    def check_match():
        nonlocal flipped, attempts
        idx1, btn1 = flipped[0]
        idx2, btn2 = flipped[1]
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if card_values[idx1] == card_values[idx2]:
            matched.update([idx1, idx2])
            btn1.config(bg="lightblue")
            btn2.config(bg="lightblue")
            for b in buttons:
                b.config(state="normal")
        else:
            btn1.config(text="", bg="SystemButtonFace")
            btn2.config(text="", bg="SystemButtonFace")
            for idx, b in enumerate(buttons):
                if idx not in matched:
                    b.config(state="normal")

        flipped = []
        if len(matched) == len(card_values):
            win_label.config(text=f"YOU WON IN {attempts} ATTEMPTS! 🎉")

    # Create buttons for cards
    buttons = []
    for i in range(16):
        btn = tk.Button(root, text="", font=("Segoe UI Emoji", 20), width=4, height=2,
                        command=lambda i=i: flip_card(i, buttons[i]))
        buttons.append(btn)

    for idx, btn in enumerate(buttons):
        btn.grid(row=idx//4, column=idx%4, padx=5, pady=5)

    # Label to show win message
    win_label = tk.Label(root, text="", font=("Georgia", 14), bg="#edafbf", fg="black")
    win_label.grid(row=4, column=0, columnspan=4, pady=10)

    # Restart game function
    def restart():
        nonlocal card_values, flipped, matched, attempts
        random.shuffle(card_values)
        flipped = []
        matched = set()
        attempts = 0
        attempts_label.config(text=f"Attempts: {attempts}")
        win_label.config(text="")
        for btn in buttons:
            btn.config(text="", state="normal", bg="SystemButtonFace")

    # Restart and Quit buttons
    tk.Button(root, text="Restart 🔄", font=("Georgia", 15), bg="lightblue", command=restart).grid(row=5, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Quit ❌", font=("Georgia", 15), bg="red", command=root.destroy).grid(row=5, column=2, columnspan=2, pady=10)

    root.mainloop()
