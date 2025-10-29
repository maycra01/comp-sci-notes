class Picture:
    def __init__(self, pDescription, pWidth, pHeight, pFrameColour):
        self.__description = pDescription  # STRING, private
        self.__width = pWidth  # INTEGER, private
        self.__height = pHeight  # INTEGER, private
        self.__frame_colour = pFrameColour  # STRING, private

    def GetDescription(self):  # returns STRING
        return self.__description

    def GetHeight(self):  # returns INTEGER
        return self.__height

    def GetWidth(self):  # returns INTEGER
        return self.__width

    def GetColour(self):  # returns STRING
        return self.__frame_colour

    def SetDescription(self, pDesc):
        self.__description = pDesc


picture_array = []  # of type Picture with 100 elements
for i in range(100):
    picture_array.append(Picture("",0,0,""))

def ReadData():  # returns INTEGER
    global picture_array
    content = ""  # STRING
    lines = []  # ARRAY
    num_pictures = 0  # INTEGER
    try:
        with open("pictures_w24_41", "r") as data:
            content = data.read()
            lines = content.split("\n")

    except FileNotFoundError:
        print(f"Error: file not found")

    for i in range(0, len(lines) - 1, 4):
        picture_array[i] = Picture(lines[i], lines[i + 1], lines[i + 2], lines[i + 3])

    num_pictures = len(picture_array)
    return num_pictures


num_of_pictures = 0  # INTEGER
num_of_pictures = ReadData()
print(f"The number of pictures in the array is {num_of_pictures}")

req_width = 0  # INTEGER
req_length = 0  # INTEGER
req_colour = ""  # STRING

req_colour = input("Please enter the colour of the picture frame").lower()
req_width = int(input("Please enter the maximum width of the picture"))
req_height = int(input("Please enter the maximum height of the picture"))

for picture in picture_array:
    if ((picture.GetColour().lower() == req_colour) and
            (int(picture.GetWidth()) <= req_width) and
            (int(picture.GetHeight()) <= req_height)):

        print(f"Picture description: {picture.GetDescription()} \n"
              f"Picture width: {picture.GetWidth()} \n"
              f"Picture height: {picture.GetHeight()} \n")
