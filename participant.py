
'''

################## PARTICIPANT.PY ########################
      © Jack Leonard 2019
      117372043 - Iowa Gambling Task Project

    Two classes: Participant and TrialParticipant.
    A cleaned up version of /older/117372043_Week4Lab1Assignment.py

##########################################################
'''


class Participant:
    #This is the main Participant Class; Trial Participant Inherits from this

    howManyParticipants = 0

    def __init__(self, firstName, lastName):
        # Participants First Name
        self.firstName = firstName

        # Participants Last Name
        self.lastName = lastName

        #Participants Full Name
        self.fullName = self.firstName + " " + self.lastName

        ##todo: not sure if this is needed for project or not (Not in req statement) clarify with Laura Maye

        # AIII | Variable that counts how many instances of class created
        Participant.howManyParticipants += 1
        # AIV Participants Number
        self.participantsNumber = Participant.howManyParticipants

    #Getters & Setters

    def setFirstName(self, new_firstName):
        self.firstName = new_firstName

    def setLastName(self, new_lastName):
        self.lastName = new_lastName

    # Class String Representation
    def __str__(self):
        return "Object Info - Participants Full Name: %s, Participant Number:  %d" % (self.fullName, self.participantsNumber)



class trialParticipant(Participant):

    #Initializer for trialParticipant Class
    def __init__(self):

        # Dragging in initializer from Participant Class
        super(trialParticipant, self).__init__()

        self.charsPressed = {"a": 0, "b": 0, "c": 0, "d": 0,}
        self.__winnings = 0 #todo: I added this in, because it was in old file. Not set in this.




    def getWinnings(self):
        return self.__winnings




    def setWinnings(self, winnings_loses):  # TODO this isn't changing/setting the winnings section
         # Takes a tutle as input (amount_won,amount_lost)
        # From this the function should calculate how much money the participant has left over once the winning amount and losing amount has been applied to the participant’s overall winnings.
        winnings = self.__winnings
        newWinnings = (winnings - winnings_loses[1]) + winnings_loses[0]
        self.__winnings = newWinnings

        # H - This function returns the character presses made by the participant as a list of tuples (i.e. not a dictionary).

    def getKeyPressInfo(self):
        dictlist = []
        charsPressed = self.__charsPressed
        for key, value in charsPressed.items():
            temp = [key, value]
            dictlist.append(temp)
        return dictlist

    # I - Count how many tims a participant has clicked chars ('a', 'b', 'c', 'd',)
    def recordKeysPressed(self, char_pressed):  # TODO not invoked in char press yet
        charDict = self.__charsPressed
        if char_pressed == "a" or char_pressed == "b" or char_pressed == "c" or char_pressed == "d":
            charDict[char_pressed] += 1



        # This function is intended to count how many times a participant has clicked the characters a, b, c or d.

    # J - This function returns a list of tuples that hold the character(s) with the highest amount of key presses.
    def getMaxKeyPress(self):
        highestvalue = 0
        highestValueList = []
        dictlist = self.__charsPressed
        # find highest values
        for item in dictlist.items():
            key = item[0]
            value = item[1]
            # print("max test")
            # print(key, value)
            if value > highestvalue:
                highestvalue = value
                # print(f"Highest Value: {highestvalue}")
                # find the chars with highest value
                for k, v in dictlist.items():
                    if v == highestvalue:
                        highestValueList.append((k, v))
                        # print(highestValueList)
        return highestValueList

        # K - This function returns a list of tuples that hold the character(s) with the highest amount of key presses.

    def getMinKeyPress(self):
        minvalue = 0
        minvalueList = []
        dictlist = self.__charsPressed
        # find min values

        for item in dictlist.items():
            key = item[0]
            value = item[1]
            # print("min test")
            # print(key, value)
            if value < minvalue:
                minvalue = value
                # print(f"Min Value: {minvalue}")
        # find the chars with highest value
        for k, v in dictlist.items():
            if v == minvalue:
                minvalueList.append((k, v))

        return minvalueList

