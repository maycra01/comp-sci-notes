def RecursiveInsertion(IntegerArray, NumberElements):  # returns ARRAY
    # LastItem as INTEGER
    # CheckItem as INTEGER
    # LoopAgain as BOOlEAN
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2

    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False

    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    for i in range(1, NumberElements):
        j = i - 1
        value = IntegerArray[i]
        while (IntegerArray[j] > value) and (j >= 0):
            IntegerArray[j+1] = IntegerArray[j]
            j -= 1
        IntegerArray[j+1] = value
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):  # Returns INTEGER
    Mid = (First + Last) // 2
    while First <= Last:
        if IntegerArray[Mid] == ToFind:
            return Mid
        elif IntegerArray[Mid] < ToFind:
            return BinarySearch(IntegerArray, Mid + 1, Last, ToFind)
        else:
            return BinarySearch(IntegerArray, First, Last - 1, ToFind)
    return -1


#  main
NumberArray = []  # 1D array of type INTEGER, with 7 elements
NumberArray = [100, 85, 644, 22, 15, 8, 1]

SortedArray = RecursiveInsertion(NumberArray, 7)
print("Recursive")
for item in SortedArray:
    print(f"{item} ", end="")
print()

SortedArray = IterativeInsertion(NumberArray, 7)
print("Iterative")
for item in SortedArray:
    print(f"{item} ", end="")
print()

found_index = BinarySearch(NumberArray, 0, 6, 644)
if found_index == -1:
    print("Not found")
else:
    print(found_index)

