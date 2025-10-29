def ChooseCard():  # returns INTEGER
    global selected_card_index_array
    pIndex = int(input("Enter an array index from 1 to 30 inclusive: "))
    while ((pIndex < 1) or (pIndex > 30)) or (pIndex in selected_card_index_array) :
        print("That card is unavaliable")
        pIndex = int(input("Enter a different array index from 1 to 30 inclusive: "))

    selected_card_index_array.append(pIndex)
    return pIndex


class Card:
    # Number INTEGER, PRIVATE
    # Colour STRING, PRIVATE
    def __init__(self, pNumber, pColour):
        self.__Number = pNumber
        self.__Colour = pColour

    def GetNumber(self):  # returns INTEGER
        return self.__Number

    def GetColour(self):  # returns STRING
        return self.__Colour

card_values_array = []  # 1D array of type Card, 30 elements
selected_card_index_array = []  # 1D array of type Integer, 30 elements, global

try:
    with open("CardValues.txt", "r") as file:
        content = file.read()
        lines = content.split("\n")
    for index in range(0,len(lines), 2):
        card_values_array.append(Card(lines[index], lines[index + 1]))
except IOError:
    print("Error: file not found")

Player1 = []  # 1D array of type Card, 4 elements
for _ in range(4):
    Player1.append(card_values_array[ChooseCard()-1])

for card in Player1:
    print(f"Colour: {card.GetColour()}, Number: {card.GetNumber()}")
