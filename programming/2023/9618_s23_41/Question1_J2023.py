def PrintArray(pArray):
    for item in pArray:
        print(f"{item}  ", end="")
    print("\n")

def LinearSearch(pArray, pGoal):  # returns INTEGER
    count = 0  # INTEGER
    for item in pArray:
        if int(item) == int(pGoal):
            count += 1
    return count

DataArray = []  # 1D ARRAY of type INTEGER with 25 elements

try:
    with open("Data.txt", "r") as file:
        content = file.read()
        lines = content.split("\n")
    for line in lines:
        DataArray.append(line)
except FileNotFoundError:
    print("Error: File not found")

# try:
#     DataFile = open("Data.txt",'r')
#     for Line in DataFile:
#         DataArray.append(int(Line))
#     DataFile.close()
# except IOError:
#     print("Could not find file")

PrintArray(DataArray)

goal = int(input("Enter a whole number between 0 and 100 inclusive"))
while (goal < 0) or (goal > 100):
    goal = int(input("Enter a whole number between 0 and 100 inclusive"))

count = LinearSearch(DataArray, goal)
print(f"The number {goal} is found {count} times.")
