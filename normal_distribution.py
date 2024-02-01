"Simulation of Montecarlo"
import collections
import random

STICKS = ['sword', 'heart', 'diamond', 'clover'] 
VALUES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'joker', 'queen', 'king']

def create_deck():
    deck = []
    for stick in STICKS:
        for value in VALUES:
            deck.append((stick, value))
    return deck

def get_hand(deck, hand_size):
    hand = random.sample(deck, hand_size)
    return hand

def main(hand_size, tries):
    deck = create_deck()
    hands = []
  
    for _ in range(tries):
        hand = get_hand(deck, hand_size)
        hands.append(hand)
    
    pairs = 0
    
    for hand in hands:
        values = []
        for card in hand:  # Change 'hands' to 'hand' here
            values.append(card[1])
    
        counter = dict(collections.Counter(values))
        for val in counter.values():
            if val == 2:
                pairs += 1
                break

            
    probability_pair = pairs / tries
    print(f'The probability of obtain a pair in a deck of {hand_size} cards is {probability_pair}')

if __name__ == '__main__':

    hand_size = int(input('How many cards will be in the hand: '))
    tries = int(input('How many tries to calculate the probability: '))
    
    main(hand_size, tries)