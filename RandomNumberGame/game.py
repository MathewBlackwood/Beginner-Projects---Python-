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


def game():

    #Variabls
    points = 100
    

    #Introduction header
    print("🌟⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️🌟")
    print("⭐️  Welcome to Smily Stars! ⭐️")
    print("🌟⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️🌟")

    print(f"You currently have {points} points!")
    #Short way to check if the game is ok to proceed 

    #Game running loop
    while points > 0: 
        #Take the players bet as an input
        bet = input("Please input the amount of points you wish to play! ")
        
        #Base case 1 - dealing with invalid inputs from the player
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        #Convert from a string number to an integer 
        bet = int(bet)

        #Base case 2 - dealing with amount higher than the players point count
        if bet > points: 
            print(f"Please enter an amount lower than your current point tally: {points}")
            continue 
        
        #Game variables
        star = functions.generateEmoji()
        winnings = functions.pointsDistribute(star, bet)
        
        points -= bet
        print("🎰 Result:", " ".join(star))
        print(f"Player has won {winnings}")

        points += winnings
        print(f"Current point Tally {points}")


game()