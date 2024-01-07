'''
Name: Rikesh Sapkota
CSC 201
Programming Project 2--skip3.py

Skip 3 Solitaire uses one long row of cards dealt on card at a time. The
objective is to consolidate the cards into one pile using the following
rules. Two adjacent cards or two cards that are 3 apart (ie two cards
inbetween) can be consolidated into one pile is they have the same
suit or the same rank.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):
I recieved assistance from Professor Mueller for comparing the index, rank and suit of cards.


'''
from graphics2 import *
from board import CardRowBoard
from deck import Deck
from button import Button 
import time

def showDirections():
    """
    Gives the directions for Skip 3 Solitaire. The "Click to begin" button
    must be clicked to continue to the game.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Skip-3 Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the same pile following these rules.\n\n"
                "If two cards with the same suit or the same rank\n"
                "are either next to each other or have two cards\n"
                "between them, then click the two cards and the \n"
                "card clicked first will be placed on top of the\n"
                "card clicked second consolidating the piles.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 200, 40, "Click to begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    """
    Draws the board and the button to deal the cards. It also initializes
    the board and deck of cards.
    
    Returns:
    the window for the game, the button to deal a card, the board for the game, and the deck of cards
    
    """
    window = GraphWin('Skip3 Solitare', CardRowBoard.WINDOW_WIDTH, CardRowBoard.WINDOW_HEIGHT)
    window.setBackground('green')
    
    dealCardButton = Button(Point(CardRowBoard.WINDOW_WIDTH - 100, CardRowBoard.WINDOW_HEIGHT - 30), 100, 40, "Deal Card")
    dealCardButton.draw(window)
    dealCardButton.activate()
    
    gameBoard = CardRowBoard()
    deck = Deck(False)
        
    return window, dealCardButton, gameBoard, deck

def giveMessage(window, words, numSecs):
    """
    Displays a message in the window for the number of seconds received
    
    Parameters:
    window (GraphWin): the window for the card game
    words (str): the message to be displayed in the window
    numSecs (int): the number of seconds to display the message
    """
    message = Text(Point(750, 350), words)
    message.setSize(18)
    message.setFill('red')
    message.draw(window)
    time.sleep(numSecs)
    message.undraw()
    
def initialClicks(window, gameBoard, dealCardButton, deck):
    """
    Two cards must be initially dealt to begin the game. The cards are dealt
    by clicking on a Deal Card button
    
    Parameters:
    window (GraphWin): the window for the card game
    gameBoard (CardRowBoard): the board managing the movement of the cards
    dealCardButton (Button): the button to click to deal a card
    deck (Deck): the deck of cards for the game
    
    """
    click = window.getMouse()
    while not dealCardButton.isClicked(click):
        giveMessage(window, 'You must click Deal Card twice to start the game!', 1)     
        click = window.getMouse()
    card = deck.dealCard()
    gameBoard.addCard(card, window)
    
    click = window.getMouse()
    while not dealCardButton.isClicked(click):
        giveMessage(window,'You must click Deal Card again to start the game!',1)    
        click = window.getMouse()
    card = deck.dealCard()
    gameBoard.addCard(card, window)
    
def clicks(window, gameBoard, dealCardButton, deck):
    '''
    Cards are dealt by clicking on a Deal Card button and their Rank, suit and index are
    compared with each another to make a legal move.
    
    Parameters:
    window (GraphWin): the window for the card game
    gameBoard (CardRowBoard): the board managing the movement of the cards
    dealCardButton (Button): the button to click to deal a card
    deck (Deck): the deck of cards for the game
    
    '''
    click1 = window.getMouse()
    if dealCardButton.isClicked(click1):
        card = deck.dealCard()
        gameBoard.addCard(card, window)
    
    elif gameBoard.isPointInCard(click1):
        card1 = gameBoard.getCardAtPoint(click1)
        click2 = window.getMouse()
        if gameBoard.isPointInCard(click2):
            card2 = gameBoard.getCardAtPoint(click2)
            
            if (abs(gameBoard.getCardIndex(card1) - gameBoard.getCardIndex(card2))) == 1 or (abs((gameBoard.getCardIndex(card1) - gameBoard.getCardIndex(card2))) == 3):
                if card1.getRank() == card2.getRank() or card1.getSuit() == card2.getSuit():
                    gameBoard.moveCard(card1, card2)
                    
                else:
                    giveMessage(window, "That's not a legal move!!", 1)
                
            else:
                giveMessage(window, "That's not a legal move!!", 1)
                
        else:
           giveMessage(window, "You have to click on another card to make a legal move", 1) 
                                                        
           
    else:
        giveMessage(window, "You have to click on Deal Card button to deal a card", 1)
        
        
        
def closingWindow(gameBoard):
    '''
    Main game window is closed and the small window is poped up giving the
    message to player about their ramaining piles of cards on game board.
    
    Parameter:
    gameBoard (CardRowBoard): the board managing the movement of the cards
    
    '''
    
    window_end = GraphWin("End Game!", 600, 400)
    window_end.setBackground('white')
    rem_pile_card = gameBoard.getNumCardsOnBoard()
    
    message1 = Text(Point(300, 100), f'You have end the game but you had {rem_pile_card} remaining piles of card on your Game Board.')
    message1.setSize(16)
    message1.draw(window_end)
    
    if rem_pile_card == 1:
        message2 = Text(Point(300, 150), "Excellent Gameplay. Keep it up!")
        message2.setSize(16)
        message2.draw(window_end)
    
    elif 2 <= rem_pile_card <= 4:
        message3 = Text(Point(300, 150), "Great Job. You did it well!")
        message3.setSize(16)
        message3.draw(window_end)

    elif 5 <= rem_pile_card <= 14:
        message4 = Text(Point(300,150), "Good Try. You can do well next time.")
        message4.setSize(16)
        message4.draw(window_end)
            
    elif rem_pile_card > 14:
        message5 = Text(Point(300, 150), "Try again!! There were still so many piles to Play")
        message5.setSize(16)
        message5.draw(window_end)
        
    time.sleep(2)
    window_end.close()

        
        
def endGame(window, gameBoard):
    '''
    End Game button comes when the deck is empty and the player is given a chance to make any final moves.
    If the player makes a illegal moves then message pops out.
    
    Parameters:
    window (GraphWin): the window for the card game
    gameBoard (CardRowBoard): the board managing the movement of the cards
    
    '''
    
    endCardButton = Button(Point(CardRowBoard.WINDOW_WIDTH - 100, CardRowBoard.WINDOW_HEIGHT - 30), 100, 40, "End Game")
    endCardButton.draw(window)
    endCardButton.activate()
    giveMessage(window, "Deck is Empty!", 1)
    
    click1 = window.getMouse()
    
    while not endCardButton.isClicked(click1):
        if gameBoard.isPointInCard(click1):
            card1 = gameBoard.getCardAtPoint(click1)
            click2 = window.getMouse()
        
            if gameBoard.isPointInCard(click2):
                card2 = gameBoard.getCardAtPoint(click2)
            
                if (abs(gameBoard.getCardIndex(card1) - gameBoard.getCardIndex(card2))) == 1 or (abs((gameBoard.getCardIndex(card1) - gameBoard.getCardIndex(card2))) == 3):
                    if card1.getRank() == card2.getRank() or card1.getSuit() == card2.getSuit():
                        gameBoard.moveCard(card1, card2)
                
                    else:
                        giveMessage(window, "That's not a legal move!!", 1)
                
                else:
                    giveMessage(window, "That's not a legal move!!", 1)
                    
            else:
                giveMessage(window, "You have to click on another card to make a legal move", 1)
                
        else:
            giveMessage(window, "You have to either click on cards to play a move or click on End Game to end the game", 1)
            
        click1 = window.getMouse()
        
    window.close()
    closingWindow(gameBoard)
        

def main():
    showDirections()
    
    window, dealCardButton, gameBoard, deck = setUpGame()

    initialClicks(window, gameBoard, dealCardButton, deck)
    

    while not deck.isEmpty():
        clicks(window, gameBoard, dealCardButton, deck)

        
    endGame(window, gameBoard)
    
           
        
    
    
    
if __name__ == '__main__':
    main()    