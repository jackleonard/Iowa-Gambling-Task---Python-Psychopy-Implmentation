'''

################## MAIN.PY ########################
      © Jack Leonard 2019
      117372043 - Iowa Gambling Task Project

            Main Code & Psychopy based GUI

###################################################
'''

#       ↓ Document Imports
from participant import Participant, trialParticipant
from filemanager import FileManager, DeckFileManager

#       ↓  Psychopy/External Dependency Imports
from psychopy.visual import Window, TextStim
import psychopy.visual
from psychopy import event
from psychopy import core

#       -> Instantiating Classes

participantA = trialParticipant
deckA = DeckFileManager()
deckB = DeckFileManager()
deckC = DeckFileManager()
deckD = DeckFileManager()

#       ✎ Psychopy GUI
'''
#todo: figure out why text isn't rendering and or centred

display = Window(
    size=(600,400),
    units="pix",
    color="#06070a"
)

#create a text object
t1 = TextStim(
    win=display,
    pos=[0,0], #note this value can be a list or a tuple
    text="Hello world!!",
    color="#27e4c9",
)


t1.draw() #draw the text
display.flip() #clear the canvas and place new 'drawable' elements on the canvas
core.wait(25) #wait 7 seconds
display.close() #close the display

'''

#       ♔ Main Code

#todo: sends in a list representing the initial key pressed by the user
def runningTrial(key_pressed):
    pass

#A - while loop

char_pressed = None

#todo: Fix this code figure out how to make sure less than rows
# Sentinel Loop ?? 
while char_pressed != 'q': #or  deckA.rowNumber <= deckA.getTotalRows() or  deckB.rowNumber <= deckB.getTotalRows() or  deckC.rowNumber <= deckC.getTotalRows() or  deckD.rowNumber <= deckD.getTotalRows():
    #todo: not sure if not notation here works - check this

  # this will continue to loop until the participant clicks 'q' key
    char_pressed = input("Please enter a character: 'a', 'b', 'c' or 'd' to reveal your winnings. Type 'q' to quit: ")
    if char_pressed == 'a': # character 'a' refers to Deck A

        #obtaining winning & losing amount from Deck
        print(deckA.getWinsLoses())
        winningsLoses = deckA.getWinsLoses()
        #Obtaining the amount won as display text
        print(deckA.getWins())
        #Obtaining the amount lost as display text
        print(deckA.getLosses())
        #Recalculating the participants winnings
        participantA.setWinnings(winningsLoses)
        participantA.recordKeysPressed('a')



    elif char_pressed == 'b': # character 'b' refers to Deck B

        # obtaining winning & losing amount from Deck
        print(deckB.getWinsLoses())
        winningsLoses = deckB.getWinsLoses()
        # Obtaining the amount won as display text
        print(deckB.getWins())
        # Obtaining the amount lost as display text
        print(deckB.getLosses())
        # Recalculating the participants winnings
        participantB.setWinnings(winningsLoses)
        participantB.recordKeysPressed('b')



    elif char_pressed == 'c': # character 'c' refers to Deck C

        # obtaining winning & losing amount from Deck
        print(deckC.getWinsLoses())
        winningsLoses = deckC.getWinsLoses()
        # Obtaining the amount won as display text
        print(deckC.getWins())
        # Obtaining the amount lost as display text
        print(deckC.getLosses())
        # Recalculating the participants winnings
        participantC.setWinnings(winningsLoses)
        participantC.recordKeysPressed('c')



    elif char_pressed == 'd': # character 'd' refers to Deck UnicodeDecodeError

        # obtaining winning & losing amount from Deck
        print(deckD.getWinsLoses())
        winningsLoses = deckD.getWinsLoses()
        # Obtaining the amount won as display text
        print(deckD.getWins())
        # Obtaining the amount lost as display text
        print(deckD.getLosses())
        # Recalculating the participants winnings
        participantD.setWinnings(winningsLoses)
        participantD.recordKeysPressed('d')














