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
from psychopy.visual import Window, TextStim, ShapeStim
import psychopy.visual
from psychopy import event
from psychopy import core

#       -> Instantiating Classes

participantA = trialParticipant()
deckA = DeckFileManager()
deckB = DeckFileManager()
deckC = DeckFileManager()
deckD = DeckFileManager()

#       ✎ Psychopy GUI

#todo: figure out why text isn't rendering and or centred

display = Window(
    size=(1080,810),
    units="pix",
    color="#06070a",
)

#create "Winnings" Title Text object
winningsTitleText = TextStim(
    win=display,
    pos=(0,380), #note this value can be a list or a tuple
    text="Winnings:",
    font='Futura',
    bold=True,
    alignHoriz='center',
    color="#4A5EB9",
    height=25,
)

#create "Winnings" Variable Text object
winningsVariableText = TextStim(
    win=display,
    pos=(0,330), #note this value can be a list or a tuple
    text="Winnings:",
    font='Futura',
    alignHoriz='center',
    color="#4A5EB9",
    height=25,
)

#create "Amount Won" subtitle text
amountWonSubtitleText = TextStim(
    win=display,
    pos=(-400,290), #note this value can be a list or a tuple
    text="Amount Won:",
    font='Futura',
    bold=True,
    alignHoriz='center',
    color="#4A5EB9",
    height=15,
)

#create "Amount Won" variable text
amountWonVariableText = TextStim(
    win=display,
    pos=(-400,250), #note this value can be a list or a tuple
    text="",
    font='Futura',
    alignHoriz='center',
    color="#4A5EB9",
    height=15,
)

#create "Amount Lost" subtitle text
amountLostSubtitleText = TextStim(
    win=display,
    pos=(400,290), #note this value can be a list or a tuple
    text="Amount Lost:",
    font='Futura',
    bold=True,
    alignHoriz='center',
    color="#4A5EB9",
    height=15,
)

#create "Amount Lost" variable text
amountLostVariableText = TextStim(
    win=display,
    pos=(400,250), #note this value can be a list or a tuple
    text="",
    font='Futura',
    alignHoriz='center',
    color="#4A5EB9",
    height=15,
)

#create Deck A Title Text
deckATitleText = TextStim(
    win=display,
    pos=(-300,-20), #note this value can be a list or a tuple
    text="A",
    font='Futura',
    alignHoriz='center',
    color="#FFFFFF",
    height=45,
)

#create Deck B Title Text
deckBTitleText = TextStim(
    win=display,
    pos=(-100,-20), #note this value can be a list or a tuple
    text="B",
    font='Futura',
    alignHoriz='center',
    color="#FFFFFF",
    height=45,
)

#create Deck C Title Text
deckCTitleText = TextStim(
    win=display,
    pos=(100,-20), #note this value can be a list or a tuple
    text="C",
    font='Futura',
    alignHoriz='center',
    color="#FFFFFF",
    height=45,
)

#create Deck D Title Text
deckDTitleText = TextStim(
    win=display,
    pos=(300,-20), #note this value can be a list or a tuple
    text="D",
    font='Futura',
    alignHoriz='center',
    color="#FFFFFF",
    height=45,
)



#Creating the Main Header  Section
div = psychopy.visual.Rect(
    size=(2160, 540), #todo: for some reason resolution is being rendered @2x - clarify this with Laura
    units="pix",
    fillColor="#0a0d1c",
    lineColor='#0a0d1c',
    win=display,
    pos=(0, 350),

)


amountLostCopy = ""

#Draw Elements to the Canvas

def drawMainUI():
    #draw the main elements
    div.draw()
    winningsTitleText.draw() #draw the text
    amountWonSubtitleText.draw()
    amountLostSubtitleText.draw()

    #reset the colour to white
    deckATitleText.color = "white"
    deckBTitleText.color = "white"
    deckCTitleText.color = "white"
    deckDTitleText.color = "white"

    #draw the deckTitle elements
    deckATitleText.draw()
    deckBTitleText.draw()
    deckCTitleText.draw()
    deckDTitleText.draw()

    #draw the variable elements
    winningsVariableText.draw()
    amountLostVariableText.draw()
    amountWonVariableText.draw()


drawMainUI()
display.flip()




#       ♔ Main Code



def runningTrial(char_pressed):
    pass



char_pressed = psychopy.event.waitKeys()

while char_pressed != ['q'] and True:
#This is a sentinel controlled while loop, it'll break when the user quits or we run out of rows

    if deckA.rowNumber > (deckA.getTotalRows() - 1): #subtracting one to account for row headers in first column
        print("You have completed the game!")
        break
    elif deckB.rowNumber > (deckB.getTotalRows() -1): #todo: do I need to do anything here to get this to work with Psychopy?
        print("You have completed the game!")
        break
    elif deckC.rowNumber > (deckC.getTotalRows() -1):
        print("You have completed the game!")
        break
    elif deckD.rowNumber > (deckC.getTotalRows() -1):
        print("You have completed the game!")
        break



  # this will continue to loop until the participant clicks 'q' key
    char_pressed = psychopy.event.waitKeys() #input("Please enter a character: 'a', 'b', 'c' or 'd' to reveal your winnings. Type 'q' to quit: ")
    if char_pressed == ['a']: # character 'a' refers to Deck A



        #obtaining winning & losing amount from Deck
        winningsLoses = deckA.getWinsLoses()
        print(f"This is winnings Loses {winningsLoses} of type: {type(winningsLoses)}")
        print(f"This is winnings  {int(winningsLoses[0])} of type: {type(int(winningsLoses[0]))}")
        #winning losing amount display text
        winningsVariableText.text = participantA.getWinnings() #todo check how winnings are being calculated and make sure they are correct
        #Obtaining the amount won as display text
        amountWonVariableText.text = str(deckA.getWins())
        #amountWonVariableText.draw() #todo: investigate is this going to cut it or do I need to display flip or refresh as well?
        #Obtaining the amount lost as display text
        amountLostVariableText.text = str(deckA.getLosses()) #todo: check if winningLoses are correct
        #Recalculating the participants winnings
        participantA.setWinnings(winningsLoses) #todo: requires two actions? positional argument 'winnings_loses')
        participantA.recordKeysPressed('a')
        print(f"The total row number is {deckA.getTotalRows()} of type {type(deckA.getTotalRows())}")

        #change colour of deck key

        drawMainUI()
        deckATitleText.color = "green"
        deckATitleText.draw()
        display.flip()




    elif char_pressed == ['b']: # character 'b' refers to Deck B

        # obtaining winning & losing amount from Deck
        print(deckB.getWinsLoses())
        winningsLoses = deckB.getWinsLoses()
        #winningLosing amount display text
        winningsVariableText.text = participantA.getWinnings()
        # Obtaining the amount won as display text
        amountWonVariableText.text = str(deckB.getWins())
        # Obtaining the amount lost as display text
        amountLostVariableText.text = str(deckB.getLosses())
        # Recalculating the participants winnings
        participantA.setWinnings(winningsLoses)
        participantA.recordKeysPressed('b')

        # change colour of deck key

        drawMainUI()
        deckBTitleText.color = "green"
        deckBTitleText.draw()
        display.flip()




    elif char_pressed == ['c']: # character 'c' refers to Deck C

        # obtaining winning & losing amount from Deck
        print(deckC.getWinsLoses())
        winningsLoses = deckC.getWinsLoses()
        #winningLosing amount display text
        winningsVariableText.text = participantA.getWinnings()
        # Obtaining the amount won as display text
        amountWonVariableText.text = str(deckC.getWins())
        # Obtaining the amount lost as display text
        amountLostVariableText.text = str(deckC.getLosses())
        # Recalculating the participants winnings
        participantA.setWinnings(winningsLoses)
        participantA.recordKeysPressed('c')

        # change colour of deck key

        drawMainUI()
        deckCTitleText.color = "green"
        deckCTitleText.draw()
        display.flip()



    elif char_pressed == ['d']: # character 'd' refers to Deck UnicodeDecodeError

        # obtaining winning & losing amount from Deck
        print(deckD.getWinsLoses())
        winningsLoses = deckD.getWinsLoses()
        #winningLosing draw text
        winningsVariableText.text = participantA.getWinnings()
        # Obtaining the amount won as display text
        amountWonVariableText.text = str(deckD.getWins())
        # Obtaining the amount lost as display text
        amountLostVariableText.text = str(deckD.getLosses())
        # Recalculating the participants winnings
        participantA.setWinnings(winningsLoses)
        participantA.recordKeysPressed('d')

        # change colour of deck key

        drawMainUI()
        deckDTitleText.color = "green"
        deckDTitleText.draw()
        display.flip()


core.wait(5) #wait 7 seconds
winningsVariableText.text = "Thanks for Participating"
deckDTitleText.text = participantA.getWinnings()
deckDTitleText.color = "#4A5EB9"
deckATitleText.text = "Trial Over"
#todo: Need to add some more lines of text to this ( see video ) Trial is over, thanks for participanting etc
deckDTitleText.draw()
deckATitleText.draw()
winningsVariableText.draw()
display.flip()
core.wait(10) #hold screen for 10 seconds
display.close() #close the display











