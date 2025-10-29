
def PushAnimal(pData):  # returns BOOLEAN
    global Animal
    global AnimalTopPointer

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = pData
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():  # returns STRING
    global Animal
    global AnimalTopPointer
    ReturnData = ""  # STRING
    if AnimalTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

def ReadData():
    try:
        with open("AnimalData.txt", "r") as file:
            content = file.read()
            lines = content.split("\n")
        for line in lines:
            PushAnimal(line)
    except FileNotFoundError:
        print("Error: File not found")

    try:
        with open("ColourData.txt", "r") as file:
            content = file.read()
            lines = content.split("\n")
        for line in lines:
            PushColour(line)
    except FileNotFoundError:
        print("Error: File not found")

def PushColour(pData):  # returns BOOLEAN
    global Colour
    global ColourTopPointer

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = pData
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():  # returns STRING
    global Colour
    global ColourTopPointer
    ReturnData = ""  # STRING
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

def OutputItem():
    colour = PopColour()
    animal = PopAnimal()

    if (colour == "") and (animal != ""):
        print("No colour")
        PushAnimal(animal)
    else:
        if (colour != "") and (animal == ""):
            print("No animal")
            PushColour(colour)
        else:
            if (colour != "") and (animal != ""):
                print(f"{colour} {animal}")

Animal = ["" for _ in range(20)]  # 1D array of type STRING, 20 elements, global
Colour = ["" for _ in range(10)]  # 1D array of type STRING, 10 elements, global

AnimalTopPointer = 0  # INTEGER, global
ColourTopPointer = 0  # INTEGER, global

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()