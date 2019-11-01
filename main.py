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





