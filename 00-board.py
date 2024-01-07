'''
The CardRowBoard Class represents a game board of cards arranged in one long row
unless that row fills, then another row begins.

DO NOT CHANGE THIS CODE.
'''
from graphics2 import *

class CardRowBoard:
    GAP = 10             # number of pixels between cards on the board
    IMAGE_WIDTH = 73    # width of each card
    IMAGE_HEIGHT = 97   # height of each card
    NUM_ROWS = 4         # number of rows of cards
    NUM_COLS = 15         # number of columns of cards
    WINDOW_WIDTH = GAP * (NUM_COLS + 1) + NUM_COLS * IMAGE_WIDTH
    WINDOW_HEIGHT = GAP * (NUM_ROWS + 1) + NUM_ROWS * IMAGE_HEIGHT

    
    def __init__(self):
        '''
        initializes the cards on the board
        '''
        self.rowNum = 0
        self.columnNum = 0
        self.cardsOnBoardList = []
        
    def addCard(self, card, win):
        '''
        adds a card at the end of the row
        
        Params:
        card (Card)--the card to be added to the board at the end of the row
        win (GraphWin)--the window the board is draw on
        '''
        xPos = CardRowBoard.GAP + CardRowBoard.IMAGE_WIDTH/2 + self.columnNum * (CardRowBoard.IMAGE_WIDTH + CardRowBoard.GAP)
        yPos = CardRowBoard.GAP + CardRowBoard.IMAGE_HEIGHT/2 + self.rowNum * (CardRowBoard.IMAGE_HEIGHT + CardRowBoard.GAP)
        self.columnNum = self.columnNum + 1
        if self.columnNum >= CardRowBoard.NUM_COLS:
            self.rowNum = self.rowNum + 1
            self.columnNum = 0
        card.move(xPos, yPos)
        card.draw(win)
        self.cardsOnBoardList.append(card)
    
    def moveCard(self, firstCard, secondCard):
        '''
        moves the card received as the first parameter on top of the card received as the second parameter,
        then adjusts the cards on the board so that no hole remains in the row of cards
        
        Params:
        firstCard (Card)--the card to be moved on top of the second card
        secondCard (Card)--the card that will be covered with first card
        '''
        # change the position stored for the card that is moving
        secondCard.undraw()
        dx = -firstCard.getImage().getCenter().getX() + secondCard.getImage().getCenter().getX()
        dy = -firstCard.getImage().getCenter().getY() + secondCard.getImage().getCenter().getY()   
        firstCard.move(dx, dy)
        
        #adjust the cards in the list
        firstIndex = self.cardsOnBoardList.index(firstCard)
        secondIndex = self.cardsOnBoardList.index(secondCard)
        if firstIndex > secondIndex:
            del self.cardsOnBoardList[firstIndex]
            del self.cardsOnBoardList[secondIndex]          
            self.cardsOnBoardList.insert(secondIndex, firstCard)
        else:
            del self.cardsOnBoardList[secondIndex]
            del self.cardsOnBoardList[firstIndex]          
            self.cardsOnBoardList.insert(secondIndex - 1, firstCard)
                     
        # move all of the cards on the board after the moved card
        for index in range(firstIndex, len(self.cardsOnBoardList)):
            cardToMove = self.cardsOnBoardList[index]
            if cardToMove.getImage().getCenter().getX() == CardRowBoard.GAP + CardRowBoard.IMAGE_WIDTH / 2:
                cardToMove.move((CardRowBoard.NUM_COLS - 1)*(CardRowBoard.IMAGE_WIDTH + CardRowBoard.GAP), -CardRowBoard.IMAGE_HEIGHT - CardRowBoard.GAP)
            else:
                cardToMove.move(-CardRowBoard.IMAGE_WIDTH - CardRowBoard.GAP, 0)
        
        # adjust rowNum and columnNum of last card
        self.columnNum = self.columnNum - 1
        if self.columnNum < 0:
            self.columnNum = CardRowBoard.NUM_COLS - 1
            self.rowNum = self.rowNum - 1
       
    def isPointInCard(self,point):
        '''
        checks to see if the point is in some card on the board
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in some card on the board
        False if the point is in no card
        '''
        for card in self.cardsOnBoardList:
            if card.containsPoint(point):
                return True
        return False 
    
    def getCardAtPoint(self, point):
        '''
        checks to see if the point is in some card on the board
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        If the point is in a card on the board, the card is returned.
        If the point is not in any card on the board, returned None.
        '''
        for card in self.cardsOnBoardList:
            if card.containsPoint(point):
                return card
        return None
    
    def getCardIndex(self, card):
        '''
        Accesses the index of a card on the board
        
        Param:
        card (Card): the card whose index is to be determined
        
        Returns:
        The index of the card received
        '''
        return self.cardsOnBoardList.index(card)
    
    def getNumCardsOnBoard(self):
        '''
        Accesses the number of cards currently on the board
        
        Returns:
        The number of cards currentlny on the board
        '''
        return len(self.cardsOnBoardList)
 
  