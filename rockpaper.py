# rockpaper.py
# Rock Paper Scissors game with extended options (Fire and Water)

import random
import tkinter as tk

def rock_paper_scissors():
    score = {"Player": 0, "Computer": 0, "Ties": 0}

    emoji_map = {
        "Rock": "🪨",
        "Paper": "📃",
        "Scissors": "✂️",
        "Fire": "🔥",
        "Water": "💦"
    }

    # Function to handle player's choice
    def play(player_choice):
        result_label.config(text="Computer is thinking...")
        computer = random.choice(["Rock", "Paper", "Scissors", "Fire", "Water"])
        root.after(1000, lambda: finish_turn(player_choice, computer))

    # Function to evaluate result
    def finish_turn(player_choice, computer):
        color = "black"
        # Tie
        if player_choice == computer:
            result = "IT'S A TIE 💀!"
            score["Ties"] += 1
            emoji_text = f"{emoji_map[player_choice]} = {emoji_map[computer]}"
        # Player wins
        elif (
            (player_choice == "Rock" and computer == "Scissors") or
            (player_choice == "Paper" and computer == "Rock") or
            (player_choice == "Scissors" and computer == "Paper") or
            (player_choice == "Fire" and computer == "Scissors" or computer == "Paper") or
            (player_choice == "Water" and computer == "Paper" or computer == "Scissors" or computer == "Fire")
        ):
            result = "YOU WIN! 🎉"
            color = "green"
            score["Player"] += 1
            emoji_text = f"{emoji_map[player_choice]} > {emoji_map[computer]}"
        # Computer wins
        else:
            result = "COMPUTER WINS! ☹️"
            color = "red"
            score["Computer"] += 1
            emoji_text = f"{emoji_map[player_choice]} < {emoji_map[computer]}"

        # Update result and score labels
        result_label.config(
            text=f"Player chose: {player_choice}\n"
                 f"Computer chose: {computer}\n"
                 f"{result}\nScores: Player {score['Player']} | Computer {score['Computer']} | Ties {score['Ties']}"
        )
        emoji_label.config(text=emoji_text)

    # Setup GUI
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.geometry("400x300")
    root.configure(bg="lightblue")

    # Buttons for choices
    tk.Button(root, text="Rock 🪨", bg="gray", fg="black", font=("Georgia", 15),
              command=lambda: play("Rock")).place(x=0, y=200)
    tk.Button(root, text="Paper 📃", bg="lightgreen", fg="black", font=("Georgia", 15),
              command=lambda: play("Paper")).place(x=145, y=200)
    tk.Button(root, text="Scissors ✂️", bg="purple", fg="white", font=("Georgia", 15),
              command=lambda: play("Scissors")).place(x=285, y=200)
    tk.Button(root, text="Quit ❌", bg="red", fg="black", font=("Georgia", 15),
              command=root.destroy).place(x=147, y=250)
    tk.Button(root, text="Fire 🔥", bg="orange", fg="black", font=("Georgia", 15),
              command=lambda: play("Fire")).place(x=5, y=250)
    tk.Button(root, text="Water 💦", bg="blue", fg="white", font=("Georgia", 15),
              command=lambda: play("Water")).place(x=290, y=250)

    # Labels for results and emojis
    result_label = tk.Label(root, text="", font=("Georgia", 12), bg="lightblue")
    result_label.pack(pady=20)
    emoji_label = tk.Label(root, text="", font=("Segoe UI Emoji", 30), bg="lightblue")
    emoji_label.pack()

    root.mainloop()
