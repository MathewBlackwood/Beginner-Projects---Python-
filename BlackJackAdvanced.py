#Need to create a way to store a holding of 5-9 decks of cards that will:
  # Shuffle completely at the start of a game 
  # Maintain their order as the game goes on 
  # can be randomly re-shuffled 

#Need to create a dealer that takes to random cards from the 6 decks in order 
  #Dealer has the option to reshuffle the deck if he's losing money 
  #Dealer needs to reveal his cards before the player and if it's blackjack all players lose

#Need to Setup the player class with the option of 6 positions
  #Player needs the basic functions Hit, Double, Split 
  #Player needs a "Ask for advice" option 

#Need to setup the "Friend" who's a gambling expert and will you advise on what to do
  #Expert will be based on advise from a popular blackjack website - could potentially use the +1, +0, -1 system, though i think
  #there should be a more mathematically sound option for each response variable based on which card the dealer is showing
  #e.g. if he's showing 16 and you're showing 15, but the count is at a certain point where 6 of each card between 6-9 has already been presented 
  #Statistically you're better off standing because the next card is a guaruanteed to be a 10 meaning a dealer bust - which means you should 
  #bet as much as you possibly can 


import random

friendHand = []
friendBet = 0

playerHand = []
playerBet = 0 
playerBalance = 1000
gameInPlay = False
betMade = False

dealerHand = []


deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deckNumber = 0
cardPool = []

#Functions below - maybe add them to the dealer class? 
def shuffleCards(cardPool): 
    random.shuffle(cardPool)

def returnAllCards(cardPool):
    cardPool.extend(friendHand)
    friendHand.clear()

    cardPool.extend(playerHand) #Copies the cards back to the cardpool at the end 
    playerHand.clear()          #Deletes the cards in the players hands 

    cardPool.extend(dealerHand)
    dealerHand.clear()

#Setting up drawing a card and then appending it to the respective hand
def dealCard(cardPool, hand): 
    if cardPool:
        card = cardPool.pop(0)  # Draws a card from the card pool
        hand.append(card)       # Appends the drawn card to the player's hand
    else:
        print("No more cards left in the pool!")

#Setting up the ability for python to calculate the players hand 

def calculateHand(hand): 
    value = 0 
    aceCounter = 0 

    for card in hand: 
        if card in hand ["J", "Q", "K"]:
                value += 10
            

def calculateHand(hand):
    value = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            value += 11
            ace_count += 1
        else:
            value += card
    
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    
    return value

def checkForBlackJack(hand): 
    if len(hand) == 2: 
        if ("A" in hand) and any(card in hand for card in [10,"J","Q","K"]): 
            return True
        else: 
            return False

def calculateHand(hand):
    value = 0
    aceCounter = 0

    for card in hand: 
        if card in ["J","Q","K"]: 
            value += 10 

        elif card == ["A"]:
            aceCounter += 1 
            value = 11

        else: 
            value += card 

    while value > 21 and aceCounter:
        value -= 10
        ace_count -= 1

    return value

#Running the game itself: 

#Step 1 - Deciding the number of decks to play with: 

#The below will take the input of deckNumber and fill up cardPool and then Shuffle the cards using the shared function
while not (4 <= deckNumber <= 7):
    deckNumber = int(input("Please advise how many decks you want to play with (between 4 and 7): "))
    if not (4 <= deckNumber <= 7):
        print("We need a number between 4 and 7 Sir!")

for _ in range(deckNumber):
    cardPool.extend(deck)
    shuffleCards(cardPool)

print(cardPool)

#GAME 
#Start with the option to create a bet and tie it to the game itself

while not betMade:
    playerBet = int(input("Please confirm the amount you wish to bet with, Sir: "))
    
    if playerBet > playerBalance:
        print("Apologies sir, but you do not have enough funds to supplement your bet.")
    elif playerBet <= 0:
        print("Please enter a valid bet amount greater than 0.")
    else:
        #If the bet is Valid - The below will: 1. Update and print the balance, then deal the cards. 
        print("Thank you Sir, We will now begin dealing cards.")
        playerBalance = playerBalance - playerBet
        print(f"You have: {playerBet} on the table, and your remaining balance is {playerBalance}")
        gameInPlay = True
        betMade = True
        break  # Exit the loop

if betMade & gameInPlay: 

    dealCard(cardPool, friendHand)
    dealCard(cardPool, playerHand)
    dealCard(cardPool, dealerHand)

    dealCard(cardPool, friendHand)
    dealCard(cardPool, playerHand)
    dealCard(cardPool, dealerHand)

    print(f"Player cards are:{playerHand}")
    print(f"Dealer cards are: *,{dealerHand[0]}",)
    print(f"Friends cards are:{friendHand}")

while gameInPlay: 
    action = input(print("Please Advise: Hit, Double, Stand?"))

    match action: 
        case "Hit", "hit": 
            dealCard(cardPool, playerHand)
            print(playerHand)

            if calculateHand(playerHand) > 21: 
                print("Bust!")
                gameInPlay = False


