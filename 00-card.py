'''
Name: Rikesh Sapkota
CSC 201
Programming Project 2--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank
and a suit. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.




'''
from graphics2 import *
import time

class Card:
    '''
    Card represents one standard poker card with an image to display
    
    instance variables:
    image (Image): the Image that will be displayed for the card
    rank (int): the rank of the card (ace is 1 or 14, jack is 11, queen is 12, king is 13, joker is 0)
    suit (str): the suit of the card ('h' is hearts, 'd' is diamonds, 's' is spades, 'c' is clubs, 'j' is joker) 
    '''
    def __init__(self, fileName):
        self.image = Image(Point(0, 0), fileName)
        file = fileName.split('/')
        card_name = file[1]
        self.rank = int(card_name[:-5])
        self.suit = card_name[-5]
        
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def getImage(self):
        return self.image
    
    def draw(self, window):
        self.image.draw(window)
        
    def undraw(self):
        self.image.undraw()
        
    def move(self, dx, dy):
        self.image.move(dx, dy)
        
    def containsPoint(self, point):
        image_centerX = self.image.getCenter().getX()
        image_centerY = self.image.getCenter().getY()
        image_height = self.image.getHeight()
        image_width = self.image.getWidth()
        
        
        left_side = image_centerX - image_width / 2
        right_side = image_centerX + image_width / 2
        top_side = image_centerY - image_height / 2
        bottom_side = image_centerY + image_height / 2
        
        if point.getX() > left_side and point.getX() < right_side and point.getY() > top_side and point.getY() < bottom_side:
            return True
        
        else:
            return False
        
    def __str__(self):
      return f'suit = {self.suit}, rank = {self.rank}, Center = {self.image.getCenter()}'
      return f'rank = {self.rank}'
      return f'Center = {self.image.getCenter()}'
        
    

# test code for the Card class
def main():  
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    rank = card.getRank()
    if type(rank) is int:
        print('Rank is an int as it should be.')
    elif type(rank) is str:
        print('ERROR. Rank should be an int. Yours is a string!')
    else:
        print('ERROR. Rank should be an int.')
        
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click on card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click on card should move it 200 pixels right
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 0)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Diamonds card
    fileName = 'cards/2d.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    
    # move card to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        