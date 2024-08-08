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
playerHand = []
dealerHand = []



deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deckNumber = int(input("Please advise how many decks you want to play with: "))
cardPool = []

#The below will take the input of deckNumber and fill up cardPool 
for _ in range(deckNumber):
    if 4 <= deckNumber <= 7:
        cardPool.extend(deck)
else: 
    print("We need a number between 4 and 7 Sir!")

def shuffleCards(cardPool): 
    random.shuffle(cardPool)


#Setting up drawing a card and then appending it to the respective hand
def dealCard(cardPool, hand): 
    if cardPool:
        card = cardPool.pop(0)  # Draws a card from the card pool
        hand.append(card)      # Appends the drawn card to the player's hand
    else:
        print("No more cards left in the pool!")

def returnAllCards(cardPool):
    cardPool.extend(friendHand)
    friendHand.clear()

    cardPool.extend(playerHand) #Copies the cards back to the cardpool at the end 
    playerHand.clear()          #Deletes the cards in the players hands 

    cardPool.extend(dealerHand)
    dealerHand.clear()



shuffleCards(cardPool)
print(cardPool)

#Note: Friend is dealt first - then player, then Dealer at the end - Need to build in a hide dealer's first card function - maybe another variable to store is as a *? - Could easily just have it * at the beggining 
#then randomly pick a card - but that doesn't emulate a real world scenario 
dealCard(cardPool, friendHand)
dealCard(cardPool, playerHand)
dealCard(cardPool, dealerHand)

dealCard(cardPool, friendHand)
dealCard(cardPool, playerHand)
dealCard(cardPool, dealerHand)


print(playerHand)
print(dealerHand)
print(friendHand)

print(cardPool)
