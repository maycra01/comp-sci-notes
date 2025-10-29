
# Question 1(a)

def ReadData():
    my_data = []
    try:
        with open("Data_w24_41.txt", "r") as data:
            lines = data.readlines()
        for line in lines:
            my_data.append(line.strip())
        return my_data
    except FileNotFoundError:
        print("No file found")
    return my_data


# Question 1(b)(i)

def FormatArray(array):
    concatenated_array = ""
    for string in array:
        concatenated_array += string + " "
    return concatenated_array


# Question 1(b)(ii)

colours = ReadData()
print(FormatArray(colours))


# Question 1(c)

def CompareStrings(string_a, string_b):
    count = 0
    while True:
        if string_a[count] == string_b[count]:
            count += 1
        elif string_a[count] < string_b[count]:
            return 1
        else:
            return 2


# Question 1(d)(i)

def Bubble(array):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(array)-1):
            if CompareStrings(array[i], array[i+1]) == 2:
                array[i], array[i+1] = array[i+1], array[i]
                swap = True
    return array


# Question 1(d)(ii)

print(FormatArray(Bubble(colours)))




# Question 2(a)(i)

class Horse:
    def __init__(self, PName, PMaxFenceHeight, PPercentageSuccess):
        self.__Name = PName  # string
        self.__MaxFenceHeight = PMaxFenceHeight  # integer
        self.__PercentageSuccess = PPercentageSuccess  # integer

    # Question 2(a)(ii)

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    # Question 2(d)

    def Success(self, Height, Risk):
        modifiers = {1: 1.0, 2: 0.9, 3: 0.8, 4: 0.7, 5: 0.6}
        if Height > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2

        else:
            return self.__PercentageSuccess * modifiers[Risk]


# Question 2(b)

Horses = []
Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))


# Question 2(c)(i)

class Fence:
    def __init__(self, PHeight, PRisk):
        self.__Height = PHeight  # integer
        self.__Risk = PRisk  # integer

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk


# Question 2(c)(ii)

Course = []
for i in range(4):
    height = int(input(f"Enter the height of fence number {i + 1} :"))
    while (height < 70) or (height > 180):
        print("Height has to be between 70cm and 180cm inclusive")
        height = int(input(f"Enter the height of fence number {i + 1} :"))

    risk = int(input(f"Enter the risk of fence number {i + 1} :"))
    while (risk < 1) or (risk > 5):
        print("Risk has to be a whole number between 1 and 5")
        risk = int(input(f"Enter the risk of fence number {i + 1} :"))

    Course.append(Fence(PHeight=height, PRisk=risk))


# Question 2(e)(i)

# for horse in Horses:
#     for fence in Course:
#         print(f"The horse {horse.GetName()} at fence {Course.index(fence)+1} has a "
#               f"{horse.Success(fence.GetHeight(), fence.GetRisk())}% of success")


# Question 2(e)(ii)

averages = []
for horse in Horses:
    success_total = 0
    for fence in Course:
        print(f"The horse {horse.GetName()} at fence {Course.index(fence) + 1} has a "
              f"{horse.Success(fence.GetHeight(), fence.GetRisk())}% of success")
        success_total += horse.Success(fence.GetHeight(), fence.GetRisk())

    print(f"The horse {horse.GetName()} has an average {success_total/4}% chance of "
          f"jumping over all four fences")
    averages.append(success_total/4)


index_of_max = averages.index(max(averages))
print(f"The horse {Horses[index_of_max].GetName()} has the highest chance of success")


# Question 3(a)

myLinkedList = []  # global
heapStartPointer = 0
startPointer = -1

for i in range(20):
    myLinkedList.append([-1, i + 1])

myLinkedList[19][1] = -1


# Question 3(b)

def InsertData():
    global myLinkedList
    global heapStartPointer
    global startPointer

    for _ in range(5):
        if FirstEmpty != -1:
            next_empty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("enter the number:"))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = next_empty


# Question 3(c)(i)

def OutputLinkedList():
    global myLinkedList
    global heapStartPointer
    global startPointer
    current_pointer = FirstNode
    if FirstNode != -1:
        while current_pointer != -1:
            print(LinkedList[current_pointer][0])
            current_pointer = LinkedList[current_pointer][1]


# Question 3(c)(ii)

InsertData()
OutputLinkedList()


# Question 3(d)(i)

def RemoveData(target_data):
    global myLinkedList
    global heapStartPointer
    global startPointer
    current_pointer = FirstNode
    previous_pointer = current_pointer
    while LinkedList[current_pointer][0] != target_data:
        previous_pointer = current_pointer
        current_pointer = LinkedList[current_pointer][1]

    if previous_pointer != current_pointer:
        LinkedList[previous_pointer][1] = LinkedList[current_pointer][1]
        LinkedList[current_pointer][0] = -1
        LinkedList[current_pointer][1] = FirstEmpty
        FirstEmpty = current_pointer
    else:
        FirstNode = LinkedList[current_pointer][1]
        LinkedList[current_pointer][0] = -1
        LinkedList[current_pointer][1] = FirstEmpty
        FirstEmpty = current_pointer


# Question 3(d)(ii)

RemoveData(5)
print("After")
OutputLinkedList()
