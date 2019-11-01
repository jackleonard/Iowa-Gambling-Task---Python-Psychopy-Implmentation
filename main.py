'''

################## MAIN.PY ########################
      © Jack Leonard 2019
      117372043 - Iowa Gambling Task Project

            Main Code & Psychopy based GUI

###################################################
'''

# ↓ Document Imports
from participant import Participant, trialParticipant
from filemanager import FileManager, DeckFileManager

# ↓  Psychopy/External Dependency Imports
from psychopy.visual import Window, TextStim
import psychopy.visual
from psychopy import event
from psychopy import core

# -> Instantiating Classes

participantA = trialParticipant()
deckA = DeckFileManager()
deckB = DeckFileManager()
deckC = DeckFileManager()
deckD = DeckFileManager()

# Psychopy GUI

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







