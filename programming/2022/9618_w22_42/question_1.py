# QUESTION 1
"""
NumberOfJobs = 0  # Integer, GLOBAL
Jobs = [[0 for _ in range(2)] for _ in range(100)]  # GLOBAL, 2D ARRAY of type Integer 100 by 2 elements

def Initialise():
    global Jobs
    global NumberOfJobs
    NumberOfJobs = 0
    for job in Jobs:
        job[0] = -1
        job[1] = -1

def AddJob(pNum, pPri):
    global Jobs
    global NumberOfJobs
    added = False
    index = 0
    if NumberOfJobs == 100:
        print("Not added")
    else:
        while (added == False) and (index < 100):
            if (Jobs[index][0] == -1) and (Jobs[index][1] == -1):
                Jobs[index][0] = pNum
                Jobs[index][1] = pPri
                NumberOfJobs += 1
                added = True
            index += 1
        if added == True:
            print("Added")
        else:
            print("Not Added")

def InsertionSort():
    global Jobs
    global NumberOfJobs
    n = len(Jobs)
    i = 0
    for i in range(1, n):
        j = i - 1
        key_num = Jobs[i][0]
        key_pri = Jobs[i][1]
        if (key_num != -1) and (key_pri != -1):
            while (Jobs[j][1] > key_pri) and (j >= 0):
                Jobs[j+1][0] = Jobs[j][0]
                Jobs[j+1][1] = Jobs[j][1]
                j -= 1
            Jobs[j+1][0] = key_num
            Jobs[j+1][1] = key_pri

def PrintArray():
    global Jobs
    for job in Jobs:
        if job[0] != -1 and job[1] != -1:
            print(f"{job[0]} priority {job[1]}")

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

InsertionSort()
PrintArray()

"""
# QUESTION 2
"""
class Character:
    def __init__(self, pName, pX, pY):
        self.__Name = pName  # STRING, PRIVATE
        self.__XCoordinate = int(pX)  # INTEGER, PRIVATE
        self.__YCoordinate = int(pY)  # INTEGER, PRIVATE

    def GetName(self):  # returns STRING
        return str(self.__Name)

    def GetX(self):  # returns INTEGER
        return int(self.__XCoordinate)

    def GetY(self):  # returns INTEGER
        return int(self.__YCoordinate)

    def ChangePosition(self, pXChange, pYChange):
        self.__YCoordinate = self.__YCoordinate + pYChange
        self.__XCoordinate = self.__XCoordinate + pXChange

characters = [Character("", 0, 0) for _ in range(10)]
# 2D ARRAY of data type Character

try:
    with open("Characters.txt", "r") as file:
        data = file.read()
        lines = data.split("\n")
    i = 0
    while i < len(lines):
        characters[i // 3] = Character(lines[i], lines[i + 1], lines[i + 2])
        i += 3

except FileNotFoundError:
    print("Error: file not found")

# or

# Characters = []
# TextFile = "Characters.txt"
# try:
#     File = open(TextFile, 'r')
#     for X in range(0, 10):
#         Name = File.readline().strip()
#         XCoord = File.readline().strip()
#         YCoord = File.readline().strip()
#         TempC = Character(Name, int(XCoord), int(YCoord))
#         Characters.append(TempC)
#     File.close()
# except:
#     print("File not found")


found = False
char_pos = 0
char_name = input("Enter the name of the character you wish to search for").lower()
while found == False:
    index = 0
    while (index < len(characters)) and (found == False):
        if characters[index].GetName().lower() == char_name:
            char_pos = index
            found = True
        else:
            index += 1
    if found == False:
        char_name = input("Enter the name of the character you wish to search for")

valid_inputs = ["A", "W", "S", "D"]

valid = False
keyboard_input = input("Enter the direction of movement: A,W,S,D")
while keyboard_input not in valid_inputs:
    keyboard_input = input("Enter the direction of movement: A,W,S,D")

if keyboard_input == "A":
    characters[char_pos].ChangePosition(-1, 0)
elif keyboard_input == "W":
    characters[char_pos].ChangePosition(0, 1)
elif keyboard_input == "S":
    characters[char_pos].ChangePosition(0, -1)
else:
    characters[char_pos].ChangePosition(1, 0)

print(f"{characters[char_pos].GetName()} has changed coordinates to X = {characters[char_pos].GetX()}"
      f" and Y = {characters[char_pos].GetY()}")
"""
# QUESTION 3

def Enqeue(pdata):  # Returns BOOLEAN
    global head_pointer
    global tail_pointer
    global Queue
    # if tail_pointer == -1:
    #     return False
    # else:
    #     if head_pointer == -1:
    #         head_pointer = 0
    #         Queue[tail_pointer] = pdata
    #         tail_pointer += 1
    #         return True
    #     else:
    #         Queue[tail_pointer] = pdata
    #         tail_pointer += 1
    #         return True
    if tail_pointer < 100:
        if head_pointer == -1:
            head_pointer = 0
        Queue[tail_pointer] = pdata
        tail_pointer += 1
        return True
    return False

def RecursiveOutput(pStart):  # Returns INTEGER
    global head_pointer
    global tail_pointer
    global Queue
    if pStart == head_pointer:
        return Queue[pStart]
    else:
        return RecursiveOutput(pStart - 1) + Queue[pStart]

Queue = [-1 for _ in range(100)]  # GLOBAL
head_pointer = -1  # GLOBAL
tail_pointer = 0  # GLOBAL

status = "Successful"
for num in range(1, 21):
    if Enqeue(num) == False:
        status = "Unsuccessful"
print(status)

print(Queue)
print(f"Queue total is {RecursiveOutput(tail_pointer-1)}")


