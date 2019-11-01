
import csv

class FileManager:



  def __init__(self, file_path):
    self.__path = file_path
    self.__file_object = None
    self.lineNumbers = 0


#getTotalRowsFunction
  def getTotalRows(self):
    return len(list(csv.reader(open(self.__path)))) #super hacky and this is not going to scale for larger docs
    #REFERENCE: The basis of this assumption was Referenced from StackOverflow: https://stackoverflow.com/questions/28973207/get-length-of-csv-file-without-ruining-reader
    #Access Date: 30/10/2019 @ 14:00
    #Author: "Joran Beasley"

  def readRow(self, r):
    row_num = 0
    with open(self.__path) as csv_file:
      reader = csv.reader(csv_file)
      for row in reader:
        if row_num == r:
          return row
        row_num += 1
      return None # this means None will return, and will only happen if the row number is not in range.



class DeckFileManager(FileManager):

  instanceCount = 0

  def __init__(self):

      super().__init__('Decks.csv') #calling filepath from init FileManager

      # instanceCountVariables Part i
      DeckFileManager.instanceCount += 1
      self.decknumber = DeckFileManager.instanceCount  # decknumber variable
      self.rowNumber = 1

      # Winning Losing Amount
      self.winningLosing = ()

  def getWins(self):
    return self.winningLosing[0]

  def getLosses(self):
      return self.winningLosing[1]

  def getDeckNumber(self):
      return self.decknumber

  def getRowNumber(self):
      return self.rowNumber

  def setRowNumber(self, new_row_num):
      #should reset row number
      #Only reset if greater than 1 and less than total number of rows
      if self.getRowNumber() > 1 and self.getRowNumber() < self.getTotalRows():
          self.rowNumber = new_row_num
          print(self.rowNumber)

      pass

  def getWinsLoses(self):
      # This function should return the win amount and lose amount of that particular deck at a particular row number.
      # When the win and lose amount of that particular row has been read, the row number for that deck should increment by 1.
      # If there are no more row numbers to read for that particular deck, the function should return -1.

    if self.decknumber == 1: #DeckA
        winLose = self.readRow(self.rowNumber)[:2]
        self.rowNumber = self.rowNumber + 1
        print(f"Row number is {self.rowNumber}")
        print(winLose)
        self.winningLosing = tuple(winLose)
        print("Winning losing")
        print(self.winningLosing)
        return winLose

    if self.decknumber == 2: #DeckB
        winLose =  self.readRow(self.rowNumber)[2:4]
        self.rowNumber = self.rowNumber + 1
        print(f"Row number is {self.rowNumber}")
        print(winLose)
        self.winningLosing = tuple(winLose)
        print("Winning losing")
        print(self.winningLosing)
        return winLose

    if self.decknumber == 3: #DeckC
        winLose = self.readRow(self.rowNumber)[4:6]
        print(f"Row number is {self.rowNumber}")
        print(winLose)
        self.winningLosing = tuple(winLose)
        print("Winning losing")
        print(self.winningLosing)
        return winLose

    if self.decknumber == 4: #DeckD
        winLose = self.readRow(self.rowNumber)[6:8]
        self.rowNumber = self.rowNumber + 1
        print(f"Row number is {self.rowNumber}")
        print(winLose)
        self.winningLosing = tuple(winLose)
        print("Winning losing")
        print(self.winningLosing)
        return winLose

    if self.readRow(rowNumber) is None:
        return -1

#Q1(B) String representation of Objects Instance
  def __str__(self): #ERROR oVerides Method in Object!?

      if self.decknumber == 1:
          self.deckname = "Deck A"
      elif self.decknumber == 2:
          self.deckname = "Deck B"
      elif self.decknumber == 3:
          self.deckname = "Deck C"
      elif self.decknumber == 4:
          self.deckname = "Deck D"

      return "Object Info - Deck Name: %s" % (self.deckname)
