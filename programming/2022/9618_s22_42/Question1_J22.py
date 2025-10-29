StackData = [-1 for _ in range(10)]  # 1D array of data type Integer, with 10 elements, GLOBAL
StackPointer = 0   # Integer, GLOBAL

def StackOutput():
    global StackPointer
    global StackData
    print(f"StackPointer = {StackPointer}")
    print(f"The stack contains the items:")
    if (StackPointer > 0) and (StackPointer<= 10):
        for index in range(0, StackPointer):
            print(StackData[index])

def Push(pItem):  # returns BOOLEAN
    global StackPointer
    global StackData
    if StackPointer >= 10:
        return False
    else:
        StackData[StackPointer] = pItem
        StackPointer += 1
        return True

def Pop():  # returns INTEGER
    global StackPointer
    global StackData
    if StackPointer <= 0:
        return -1
    else:
        item = StackData[StackPointer-1]
        StackPointer -= 1
        return item

# main

for i in range(11):
    item = int(input(f"Enter item number {i+1} : "))
    success = Push(item)
    if success:
        print("The item was added to the stack")
    else:
        print("The item was not added to the stack")
StackOutput()

for i in range(2):
    Pop()
StackOutput()