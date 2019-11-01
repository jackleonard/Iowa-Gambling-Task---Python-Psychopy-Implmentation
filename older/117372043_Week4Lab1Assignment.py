'''
1. Class definition and presentation
- Class is well presented and commented
- All methods are called in the main code
2. Correct use of public/private variables
- Good understanding of public/private variables.
3. Correct use of getters/setters and property definitions
- Appropriate getter/setters and property definitions have been added to the code.
4. Problem solving:
- Good problem solving skills applied to answer all questions, there are some minor issues that are affecting the running of the code.
- In recordKeyPress(), you used the wrong operator to increment the character key press. Look for #grading in the recordKeyPress() to
see where the error lies.

'''

'''

JACK LEONARD - 117372043
Week 4 Lab 1
Graded Assignment Submission

'''



###############################
##### Defining Class:   #######
###############################

class Participant:
    # class variables
    howManyParticipants = 0

    def __init__(self, firstName, lastName):
        # AI | First Name
        self.firstName = firstName

        # AII | Last Name
        self.lastName = lastName

        # AIII | Variable that counts how many instances of class created
        Participant.howManyParticipants += 1
        #AIV Participants Number
        self.participantsNumber = Participant.howManyParticipants

        # AV Private Variable for Winnings
        self.__winnings = 2000

        # AVI dictionary containing chars user presses as keys followed by the amount of times the participants has pressed the chars as items. This dict should be private

        self.__charsPressed = {"a":0, "b":0, "c":0, "d":0,} #TODO: Figure out how to keep track of individiual keys pressed

    def __str__(self):
        return "Object Info - Participant Name: %s %s , Participant Number:  %d" % (self.firstName, self.lastName, self.participantsNumber)

    #Getters & Setters
    def getFullName(self):
        return "%s %s" % ( self.firstName, self.lastName)

    def setFullName(self, new_full_name):
        firstName, lastName = new_full_name.split(" ")
        self.firstName = firstName
        self.lastName = lastName
    #F
    def getWinnings(self):
        return self.__winnings

    #G
    def setWinnings(self, winnings_loses): #TODO this isn't changing/setting the winnings section
        #Takes a tutle as input (amount_won,amount_lost)
        # From this the function should calculate how much money the participant has left over once the winning amount and losing amount has been applied to the participant’s overall winnings.
        winnings = self.__winnings
        newWinnings = (winnings - winnings_loses[1])+winnings_loses[0]
        self.__winnings = newWinnings

    # L - Property to call getters & setters for any key pressed



    #H - This function returns the character presses made by the participant as a list of tuples (i.e. not a dictionary).
    def getKeyPressInfo(self):
        dictlist = []
        charsPressed = self.__charsPressed
        for key, value in charsPressed.items():
            temp = [key,value]
            dictlist.append(temp)
        return dictlist

    #I - Count how many tims a participant has clicked chars ('a', 'b', 'c', 'd',)
    def recordKeysPressed(self, char_pressed): #TODO not invoked in char press yet
        charDict = self.__charsPressed
        if char_pressed == "a" or char_pressed == "b" or char_pressed == "c" or char_pressed == "d":
            charDict[char_pressed] += 1 #grading: you applied a unary operator rather than an incremental operator here.
            #grading: the code above should be: charDict[char_pressed] += 1 (not =+). =+ is the similar to an assignment operator in python.
            #debug

            #print(charDict)
        else: #this is actually superflous, I could just use the first statement but I'm leaving it here in case I need a special operation for disalowed keys
            print("Invalid Character")

        #This function is intended to count how many times a participant has clicked the characters a, b, c or d.

    #J - This function returns a list of tuples that hold the character(s) with the highest amount of key presses.
    def getMaxKeyPress(self):
        highestvalue = 0
        highestValueList = []
        dictlist = self.__charsPressed
        # find highest values
        for item in dictlist.items():
            key = item[0]
            value = item[1]
            #print("max test")
            #print(key, value)
            if value > highestvalue:
                highestvalue = value
                #print(f"Highest Value: {highestvalue}")
        # find the chars with highest value
                for k, v in dictlist.items():
                    if v == highestvalue:
                        highestValueList.append((k, v))
                        #print(highestValueList)
        return highestValueList

        # K - This function returns a list of tuples that hold the character(s) with the highest amount of key presses.
    def getMinKeyPress(self): #todo: not working, check the logic !!
        minvalue = 0
        minvalueList = []
        dictlist = self.__charsPressed
        # find min values

        for item in dictlist.items():
            key = item[0]
            value = item[1]
            #print("min test")
            #print(key, value)
            if value < minvalue:
                minvalue = value
                #print(f"Min Value: {minvalue}")
        # find the chars with highest value
        for k, v in dictlist.items():
            if v == minvalue:
                minvalueList.append((k, v))

        return minvalueList

    #L - PROPERTIES

    fullName = property(getFullName, setFullName)
    winnings = property(getWinnings, setWinnings)





###############################
##### Main Code:   #######
###############################

p1 = Participant("Jane", "Doe")

char_pressed = None
while char_pressed != 'q':
# this will continue to loop until the participant clicks 'q' key
    char_pressed = input("Please enter a character: 'a', 'b', 'c' or 'd' to reveal your winnings. Type 'q' to quit: ")
    # This is pretty ugly code, I code wrap some of this in a function and just recall

    ''' reusable functin  
    def keyPressedOperation(): 
        p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        p1.getMaxKeyPress()
        p1.getMinKeyPress()
    '''

    if char_pressed == 'a':
        # keyPressedOperation()
        #class functions
        p1.winnings = (100, 200)
        print(p1.getKeyPressInfo())
        p1.recordKeysPressed(char_pressed)
        g = p1.getKeyPressInfo()
        #print(g)
        print("max key press: %s" % p1.getMaxKeyPress())
        print(p1.getMinKeyPress())
        #debug
        print(f"character a has been pressed. Winnings: {p1.getWinnings()}")
    elif char_pressed == 'b':
        # keyPressedOperation()
        #class functions
        p1.winnings = (50, 40)
        print(p1.getKeyPressInfo())
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        print("max key press: %s" %p1.getMaxKeyPress())
        print(p1.getMinKeyPress())
        #debug
        print(f"character b has been pressed. Winnings: {p1.getWinnings()}")
    elif char_pressed == 'c':
        # keyPressedOperation()
        #class functions
        p1.winnings = (100, 50)
        print(p1.getKeyPressInfo())
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        print("max key press: %s" %p1.getMaxKeyPress())
        print(p1.getMinKeyPress())
        #debug
        print(f"character c has been pressed. Winnings: {p1.getWinnings()}")
    elif char_pressed == 'd':
        # keyPressedOperation()
        # class functions
        p1.winnings = (80, 20)
        print(p1.getKeyPressInfo())
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        print("max key press: %s" %p1.getMaxKeyPress())
        print(p1.getMinKeyPress())
        # debug
        print(f"character d has been pressed. Winnings: {p1.getWinnings()}")
    else:
        #class functions
        # keyPressedOperation()
        print(p1.getKeyPressInfo())
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        print(p1.getMaxKeyPress())
        print(p1.getMinKeyPress())
        #debug
        print("Invalid character pressed. Please enter a character: 'a', 'b', 'c' or 'd' ")



###################### Testing: Getters, Setters & Properties  ##########

if __ Name __ == '__ Main__':

    # Creating instance of class
    p1 = Participant("Jane", "Doe")

    ## Testing Getters & Setters

    #testing fullname Property
    p1.fullName = "Janette Doe"
    print(p1.fullName)

    #testing misc
    print(p1.setWinnings((100,50))) #works !!
    print(p1.getKeyPressInfo()) # works !!

