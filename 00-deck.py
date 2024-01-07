'''
Name: Rikesh Sapkota
CSC 201
Programming Project 2--Deck Class

The Deck class represents a stadard deck of playing cards with or without two jokers.
The card files for the graphic of each card are in a folder named cards. Each card
file is named with its rank and a letter for its suit. For example, the 4 of hearts
is in the file 4h.gif while the jack of clubs is in  the file 11c.gif.


'''
from card import Card
import random

class Deck:
    '''
    Deck is a standard poker deck with either aces high or low and with or without Jokers.
    
    instance variables
    cardList (list): a list of the cards in this deck
    currentIndex (int): the index of the card that will be dealt next
    '''
    def __init__(self, acesHigh = True, useJokers = False):
        '''
        Initializes a standard poker deck of cards with either aces high or aces low and
        with or without Jokers.
    
        Params:
            acesHigh (bool): when True aces have rank 14; when False aces have rank 1
            useJokers (bool): when True jokers will be included in the deck
        '''
        if acesHigh:
            start = 2
            end = 14
        else:
            start = 1
            end = 13
        self.cardList = []
        for rank in range(start, end + 1):
            for suit in 'chsd':
                fileName = 'cards/'+ str(rank) + suit + '.gif'
                self.cardList.append(Card(fileName))
        if useJokers:
            self.cardList.append(Card('cards/0j.gif'))
            self.cardList.append(Card('cards/0j.gif'))
        self.shuffle()     # calls the shuffle method of the Deck class that you add!  
      
    def getFullDeckSize(self):
        '''
        Returns the number of cards in the deck when it is full
        
        Returns:
            the number of cards in the deck when it is full
        '''
        return (len(self.cardList))
        
    def shuffle(self):
        '''
        Shuffles the cards in the deck
        '''
        
        self.currentIndex = 0
        random.shuffle(self.cardList)
        
    def dealCard(self):
        
        '''
        Deals on card from the deck
        
        Returns:
            the card dealt from the deck
        '''
        cardDealt = self.cardList[self.currentIndex]
        self.currentIndex += 1
        return cardDealt
        
    def isEmpty(self):
     
        '''
        Determines if all of the cards have been dealt
        
        Returns:
            True when all of the cards have been dealt from the deck
        '''
        
        if self.currentIndex == len(self.cardList):
            return True
        
        else:
            return False
        
    def getNumCardsLeft(self):
        '''
        Determines the number of cards still left in the deck to deal
        
        Returns:
            The number of cards still in the deck to deal
        '''
       
        return len(self.cardList) - self.currentIndex
        
        

    def __str__(self):
        '''
        Returns a string with each card of the deck on a separate line
        '''
        result = ''
        for card in self.cardList:
            result = result + str(card) + '\n'
        return result
  
  
# Test code for the Deck class.
def main():
    deck = Deck()
    print('Print entire shuffled deck.')
    print(deck)
    print('Full deck size:', deck.getFullDeckSize())
    
    print('\nDeal first 5 cards')
    for i in range(5):
        card = deck.dealCard()
        print(card)
    
    print('\nNum cards left to deal:', deck.getNumCardsLeft())
    print('Is deck empty?', deck.isEmpty());
    
    print('\nDeal remaining cards without printing them.')
    for i in range(47):
        card = deck.dealCard()
    
    print('\nNum cards left to deal:', deck.getNumCardsLeft())
    print('Is deck empty?', deck.isEmpty());
    print()
    
    print('\nReshuffle the cards and print again.')
    deck.shuffle()
    print(deck)
    
    print('\nDeal first 5 cards')
    for i in range(5):
        card = deck.dealCard()
        print(card)
        
    
if __name__ == '__main__':
    main()
        