#  linear search
"""
found = False
myarray = [1, 4, 5, 2, 6]
index = 0
goal = int(input("Enter the item to be searched for"))
while (found == False) and (index < len(myarray)-1):
    if myarray[index] == goal:
        print(f"The item {goal} is in the list at index {index}")
        found = True
    index += 1
if not found:
    print("Item is not in list")
"""

# binary search
"""
myarray = [1, 4, 5, 7, 8, 10, 34, 85]
found = False
l_bound = 0
u_bound = len(myarray) - 1
goal = int(input("Enter the item to be searched for"))

while (found != True) and (l_bound <= u_bound):
    mid = (l_bound + u_bound) // 2
    if myarray[mid] == goal:
        print(f"item {goal} was found at index {mid}")
        found = True
    elif goal > myarray[mid]:
        l_bound = mid + 1
    else:
        u_bound = mid - 1

if not found:
    print("Item is not in list")
"""

# bubble sort
"""
myarray = [1, 4, 76, 5, 8, 3, 34, 85, 19]

swap = True
top = len(myarray) - 1
while swap == True:
    swap = False
    for i in range (0, top):
        if myarray[i+1] < myarray[i]:
            temp = myarray[i+1]
            myarray[i+1] = myarray[i]
            myarray[i] = temp
            swap = True
    top -= 1
print(myarray)

arr = [1, 4, 76, 5, 8, 3, 34, 85, 19]
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            # arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
"""

# insertion sort

"""
arr = [1, 4, 76, 5, 8, 3, 34, 85, 19]
n = len(arr)

for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        
print(arr)
"""
"""
class Dog():
    def __init__(self, pName, pBreed):
        self.__Name = pName
        self.__Breed = pBreed
        self.__DOB = 0
        self.__Age = 0

    def GetAge(self):
        return self.__Age

    def GetBreed(self):
        return self.__Breed

    def GetDOB(self):
        return self.__DOB

    def GetName(self):
        return self.__Name

    def SetDOB(self, pDOB):
        self.__DOB = pDOB

    def SetAge(self, pAge):
        self.__Age = pAge

    def IncreaseAge(self):
        self.__Age += 1

dog1 = Dog("name", "breed")

"""


