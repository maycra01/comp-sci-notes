"""
DataArray = [0 for _ in range(100)]  # INTEGER, GLOBAL

def ReadFile():
    global DataArray
    with open("IntegerData", "r") as file:
        content = file.read()
        lines = content.split("\n")

    for i in range(len(lines)):
        DataArray[i] = int(lines[i])


def FindValues():  # Returns INTEGER
    global  DataArray
    count = 0  # INTEGER
    goal = 0  # INTEGER
    goal = int(input("Enter a whole number to search for, between 1 and 100 inclusive"))
    while (goal < 1) or (goal > 100):
        print("Enter a whole number between 1 and 100 inclusive")
        goal = int(input("Enter a whole number to search for, between 1 and 100"))

    for number in DataArray:
        if number == goal:
            count += 1
    return count

ReadFile()
print(f"The number entered appears {FindValues()} times")

def BubbleSort():
    global DataArray
    swap = True
    top = len(DataArray) - 1
    while swap == True:
        swap = False
        for index in range(0, top):
            if DataArray[index+1] < DataArray[index]:
                temp = DataArray[index + 1]
                DataArray[index + 1] = DataArray[index]
                DataArray[index] = temp
                swap = True
        top -= 1
    print(DataArray)

BubbleSort()
"""
"""
class Card:
    def __init__(self, pNumber, pColour):
        self.__Number = pNumber  # INTEGER, PRIVATE
        self.__Colour = pColour  # STRING, PRIVATE

    def GetNumber(self):  # returns INTEGER
        return self.__Number

    def GetColour(self):
        return self.__Colour



class Hand:
    def __init__(self, card1, card2, card3, card4, card5):
        self.__Cards = [Card(0,"") for _ in range(10)]
        # 1D ARRAY of 10 elements of type Card
        self.__FirstCard = 0  # INTEGER, PRIVATE
        self.__NumberCards = 5  # INTEGER, PRIVATE
        self.__Cards[0] = card1
        self.__Cards[1] = card2
        self.__Cards[2] = card3
        self.__Cards[3] = card4
        self.__Cards[4] = card5

    def GetCard(self, pIndex):  # returns Card
        return self.__Cards[pIndex]

def CalculateValue(pHand):  # returns integer
    score = 0  # integer
    card = Card(0, "")  # Card
    for i in range(5):
        card = pHand.GetCard(i)
        score += card.GetNumber()
        if card.GetColour() == "red":
            score += 5
        if card.GetColour() == "blue":
            score += 10
        if card.GetColour() == "yellow":
            score += 15

    return score

c_red_1 = Card(1, "red")
c_red_2 = Card(2, "red")
c_red_3 = Card(3, "red")
c_red_4 = Card(4, "red")
c_red_5 = Card(5, "red")
c_blue_1 = Card(1, "blue")
c_blue_2 = Card(2, "blue")
c_blue_3 = Card(3, "blue")
c_blue_4 = Card(4, "blue")
c_blue_5 = Card(5, "blue")
c_yellow_1 = Card(1, "yellow")
c_yellow_2 = Card(2, "yellow")
c_yellow_3 = Card(3, "yellow")
c_yellow_4 = Card(4, "yellow")
c_yellow_5 = Card(5, "yellow")

player_1 = Hand(c_red_1, c_red_2, c_red_3, c_red_4, c_yellow_1)
player_2 = Hand(c_yellow_2, c_yellow_3, c_yellow_4, c_yellow_5, c_blue_1)

p1_value = CalculateValue(player_1)
p2_value = CalculateValue(player_2)
if p1_value > p2_value:
    print("Player 1 wins")
elif p1_value < p2_value:
    print("Player 2 wins")
else:
    print("It is a draw")
"""

ArrayNodes = [[-1 for _ in range(3)] for _ in range(20)]
# GLOBAL 2D array of INTEGER
ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]
FreeNode = 6  # integer
RootPointer = 0  # integer

def SearchValue(root, value_to_find):  # returns INTEGER
    global ArrayNodes
    if root == -1:
        return -1
    else:
        if ArrayNodes[root][1] == value_to_find:
            return root
        else:
            if ArrayNodes[root][1] == -1:
                return -1
    if ArrayNodes[root][1] >= value_to_find:
        return SearchValue(ArrayNodes[root][0], value_to_find)
    if ArrayNodes[root][1] < value_to_find:
        return SearchValue(ArrayNodes[root][2], value_to_find)

def PostOrder(root):
    global ArrayNodes
    if ArrayNodes[root][0] != -1:
        PostOrder(ArrayNodes[root][0])
    if ArrayNodes[root][2] != -1:
        PostOrder(ArrayNodes[root][2])
    print(ArrayNodes[root][1])

position = SearchValue(RootPointer, 15)
if position == -1:
    print("Value was not found")
else:
    print(f"Value was found at index {position}")
PostOrder(RootPointer)

