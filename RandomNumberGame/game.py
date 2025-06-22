import tkinter as tk
import random
import functions

# This is a game that will have 5 empty slots in the shape of a star
# A clickable button will begin the game which will (based on probability) fill each slot with 1 of 7 below emoji's 

# 😭 😂 🥲 🧐 🤠 😍 🤑

# The aim of the game is to fill all 5 slots with the SAME smiley to create a Smiley Star
# Players can also win if they secure a half star (3 emojis to create a triangle)
# Depending on the emoji players will either win or lose - Debatable point, could just reduce the points accrued instead? 

# Anything with a face being made is a loss - anything with an outfit is a win including
# The centre emoji with the oculus allows for a replay and will be considered a null outcome

#The game will be designed so that a fixed cost of points is charged at the start - in return players have a higher chance of winning - wishing well game 

# Global variables
points = 100

# Setup window
root = tk.Tk()
root.title("Smiley Stars")
root.geometry("400x520")

# Header
header_label = tk.Label(root, text="⭐ Welcome to Smiley Stars! ⭐", font=("Helvetica", 16))
header_label.place(x=60, y=10)

# Points display
points_var = tk.StringVar(value=f"Points: {points}")
points_label = tk.Label(root, textvariable=points_var, font=("Helvetica", 14))
points_label.place(x=140, y=45)

# Bet input
bet_label = tk.Label(root, text="Enter your bet:", font=("Helvetica", 12))
bet_label.place(x=140, y=80)

bet_entry = tk.Entry(root, justify='center')
bet_entry.place(x=140, y=105, width=120)

# Spin button
play_button = tk.Button(root, text="Spin!", command=lambda: play_round(), font=("Helvetica", 12))
play_button.place(x=160, y=135)

# Emoji Labels (star-shaped layout)
emoji_labels = [tk.Label(root, text=" ", font=("Helvetica", 30)) for _ in range(5)]

emoji_labels[0].place(x=170, y=190)   # Top
emoji_labels[2].place(x=100, y=260)   # Bottom-left
emoji_labels[3].place(x=240, y=260)   # Bottom-right
emoji_labels[4].place(x=140, y=320)   # Left-center
emoji_labels[1].place(x=200, y=320)   # Right-center

# Outcome message
outcome_label = tk.Label(root, text="", font=("Helvetica", 12))
outcome_label.place(x=100, y=400)

# Game logic
def play_round():
    global points
    bet = bet_entry.get()

    if not bet.isdigit():
        outcome_label.config(text="Please enter a valid number.")
        return

    bet = int(bet)
    if bet <= 0:
        outcome_label.config(text="Bet must be greater than 0.")
        return
    if bet > points:
        outcome_label.config(text=f"Not enough points! You have {points}.")
        return

    points -= bet
    star = functions.generateEmoji()
    winnings = functions.pointsDistribute(star, bet)
    points += winnings

    # Display star
    for i, emoji in enumerate(star):
        emoji_labels[i].config(text=emoji)

    outcome_label.config(text=f"You won {winnings} points!")
    points_var.set(f"Points: {points}")

    if points <= 0:
        outcome_label.config(text="Game Over! You’re out of points.")

# Launch GUI
root.mainloop()
