# 13/01/25

'''
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

if num1 >= num2:
    if num1 >= num3:
        print(f"{num1} is the largest number")
    else:
        print(f"{num3} is the largest number")

else:
    if num2 >= num3:
        print(f"{num2} is the largest number")
    else:
        print(f"{num3} is the largest number")
'''

'''
DECLARE num1 : INTEGER 
DECLARE num2 : INTEGER 
DECLARE num3 : INTEGER 

IF num1 >= num2 THEN
    IF num1 >= num3 THEN
        OUTPUT num1 
    ELSE
        OUTPUT num3
    ENDIF
    
ELSE
    IF num2 >= num3 THEN
        OUTPUT num2
    ELSE
        OUTPUT num3
    ENDIF
    
ENDIF

'''

'''
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")

elif num2 >= num3 and num2 >= num1:
    print(f"{num2} is the largest number")

else:
    print(f"{num3} is the largest number")
'''

'''
ask a user for a number, print a message to indicate whether or not it is prime

20 -> 10
84 -> 42

37
2
3
4
...

'''

'''
num = int(input("Enter a number"))

remainder = -1
index = 2

while (remainder != 0) and (index <= (num//2)):

    remainder = num % index
    index += 1

if remainder == 0:
    print(f"{num} is not prime")

else:
    print(f"{num} is prime")
'''

'''

DECLARE num : INTEGER
DECLARE remainder : INTEGER
DECLARE index : INTEGER

remainder <- -1
index <- 2

WHILE (remainder <> 0) AND (index <= num DIV 2) DO
    remainder <- num MOD index
    index <- index + 1
ENDWHILE
    
IF remainder = 0 THEN
    OUTPUT num & "is not prime"
ELSE 
    OUTPUT num & "is prime" 
ENDIF

'''

'''
write a function which takes a number as paramneter and returns the factorial of the number
5! = 1x2x3x4x5 = 120

5! = 5x4x3x2x1 = 5x4! = 5x24 = 120  (a x (a-1)!)
4! = 4x3! = 4x6 = 24
3! = 3x2! = 3x2 = 6
2! = 2x1! = 2x1 = 2
1! = 1 (Base Case)



def factorial(num):
 
    count = 1
    result = 1
    while count <= num:
        result = result * count
        print(count)
        count += 1
    return result
  

    for i in range(2, num):
        num = num*i
    return num

def recursive_fact(num):
    if num == 1:
        return(num)

    return(num*recursive_fact(num-1))

print(recursive_fact(5))


a = 35
b = 15

- until the numbers are the same
- subtract the smaller from the larger
- when they are the same - they are both the gcf

write the algorithm iteratively, attempt to convert to a recursive
'''
''' 
numbers = [1, 5, 88, 2, 54, 5]

n = len(numbers)
for i in range(n):
    for j in range(n-1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        print(i, numbers)

print(numbers)

DECLARE myList : ARRAY[0:8] OF INTEGER
DELCARE temp : INTEGER
DECLARE i : INTEGER
DECLARE j : INTEGER

FOR i <- 0 TO LENGTH(myList)
    FOR j <- 0 TO (LENGTH(myList)-1-i)
        IF myList[j] > myList[j+1] THEN
            temp <- myList[j]
            myList[j] <- myList[j+1]
            myList[j+1] <- temp
        ENDIF

'''

'''def linear_search(list):
    count = 0
    target = int(input("Enter the number you want to search for"))
    found = False
    while found == False and count < len(list):
        for i in list:
            count += 1
            if i == target:
                found = True

    if found:
        print(tar   get, "is in the list")
    else:
        print("not found")

numbers = [1,5,2,3,5,7]
linear_search(numbers)'''

"""

def binary_search(list):
    low = 0
    high = len(list) - 1
    target = int(input("Number to search:"))
    found = False
    print(list)
    while (found == False) and (low <= high):
        mid = (low + high) // 2
        print(low, mid, high)
        if list[mid] == target:
            found = True
        else:
            if list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    if found:
        print(target, "is in the list")
    else:
        print("not found")

ordered = [1,6,8,34,76,80]
binary_search(ordered)

def binary_search(list, item):
  found = False
  index = -1
  start = 0
  end = len(list) - 1

  while start <= end and not found:
    mid = (start + end) // 2
    if list[mid] == item:
        found = True
        index = mid
    elif list[mid] < item:
        start = mid + 1
    else:
        end = mid - 1
  return index

ordered = [1,6,8,34,76,80]
binary_search(ordered, 76)



queue = [2, 5, 4, 7, 1]


# def itr(start):
#     global queue
#     print(start)
#     if start == 0:
#         print("base case reached")
#         return queue[0]
#     else:
#         return queue[start] + itr(start-1)
#
# print(itr(4))

def fib(num):
    print(f"fib({num})")
    if num <= 1:
        print("base case reached")
        return num
    else:
        print(f"fib({num - 1}) + fib({num - 2})")
        return fib(num - 1) + fib(num - 2)


print(fib(5))

try:
    file = open("data.txt", "r")
    line = file.readline()
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print("Result:", result)
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    try:
        file.close()
    except:
        pass  # file might not have opened


# Linear Search

def linear_search(list, item):
    index = -1
    for i in range(len(list)):
        if list[i] == item:
            index = i
            break  # Stop the loop once the item is found
    return index


for i in range(1):
    print(i)

def Bubble(array):
    swap = True
    top = len(array) - 1  # 8
    while (swap == True) and (top > 0):
        print("start Cycle")
        print("     before ",array, top)
        print("     ", swap)
        swap = False
        for i in range(top):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap = True
        top = top - 1

        print("     after ", array, top)
        print("     ", swap)

    return array

myarray = [2, 5, 4, 7, 87, 45, 3, 5, 1]
print(myarray)
Bubble(myarray)
print(myarray)


def insertion_sort(data):
    for i in range(1, len(data)):
        item = data[i]
        position = i
        while position > 0 and data[position - 1] > item:
            data[position] = data[position - 1]
            position -= 1
        data[position] = item
    return data

print(insertion_sort(myarray))



stack = [None for index in range(0,10)]
print(stack)
basePointer = 0
topPointer = -1
stackFull = 10
item = None

def pop():
    global topPointer, basePointer, item
    if topPointer == basePointer -1:
       print("Stack is empty,cannot pop")
    else:
        item = stack[topPointer]
        topPointer = topPointer -1

def push(item):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[topPointer] = item
    else:
        print("Stack is full, cannot push")

class Stack:
    def __init__(self, capacity):
        self.__stackFull = capacity
        self.__stack = [None for index in range(capacity)]
        self.__topPointer = -1
        self.__basePointer = 0

    def pop(self):
        if self.__topPointer < self.__basePointer:
            print("Stack is empty")
            return None
        else:
            self.__topPointer = self.__topPointer - 1
            return self.__stack[self.__topPointer + 1]

    def push(self, item):
        if self.__topPointer + 1 < self.__stackFull:
            self.__topPointer = self.__topPointer + 1
            self.__stack[self.__topPointer] = item
        else:
            print("stack is full")

    def show(self):
        print(self.__stack)

    def top_pointer(self):
        print(self.__topPointer)


mystack = Stack(5)



queue = [None for index in range(0,10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0

def enQueue(item):
    global queueLength, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
        queueLength = queueLength + 1
        queue[rearPointer] = item
    else:
        print("Queue is full, cannot enqueue")


def deQueue():
    global queueLength, frontPointer, item
    if queueLength == 0:
        print("Queue is empty,cannot dequeue")
    else:
        item = queue[frontPointer]
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
    queueLength = queueLength -1

"""
"""
# Question 3(a)

myLinkedList = []  # global
heapStartPointer = 0
startPointer = -1
capacity = 5

for i in range(capacity):
    myLinkedList.append([-1, i + 1])

myLinkedList[capacity-1][1] = -1

print(myLinkedList)

# Question 3(b)

def InsertData(item):
    global myLinkedList
    global heapStartPointer
    global startPointer

    if heapStartPointer == -1:
        print("List is full")
    else:
        tempPointer = startPointer
        startPointer = heapStartPointer
        heapStartPointer = myLinkedList[heapStartPointer][1]
        myLinkedList[startPointer][0] = item
        myLinkedList[startPointer][1] = tempPointer


# Question 3(c)(i)

def OutputLinkedList():
    global myLinkedList
    global heapStartPointer
    global startPointer
    current_pointer = startPointer
    found = False
    item = int(input("What item are you searching for?"))

    if startPointer == -1:
        print("List is empty")
    else:
        while (found == False) and  (current_pointer != -1):
            if myLinkedList[current_pointer][0] == item:
                print("Item found at ", current_pointer)
                found = True
            else:
                current_pointer = myLinkedList[current_pointer[1]]

        if current_pointer == -1:
            print("item not in list")

# Question 3(c)(ii)

def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == -1:
        print("Linked List empty")
    else:
        index = startPointer
        oldindex = -1
        while( myLinkedList[index][0] != itemDelete) and (index != -1):
            oldindex = index
            index = myLinkedList[index][1]

        if oldindex == -1:
            startPointer = myLinkedList[index][1]
            myLinkedList[index][0] = None
            myLinkedList[index][1] = heapStartPointer
            heapStartPointer = index
        else:
            if index == -1:
                print("Item ", itemDelete, " not found")

            else:
                myLinkedList[index][0] = None
                tempPointer = myLinkedList[index][1]
                myLinkedList[index][1] = heapStartPointer
                heapStartPointer = index
                myLinkedList[oldindex][1] = tempPointer


# Question 3(d)(i)

# def RemoveData(target_data):
#     global myLinkedList
#     global heapStartPointer
#     global startPointer
#
#     if startPointer == -1:
#         print("List is empty")
#     else:
#         current_pointer = startPointer
#         previous_pointer = current_pointer
#         while myLinkedList[current_pointer][0] != target_data:
#             previous_pointer = current_pointer
#             current_pointer = myLinkedList[current_pointer][1]
#
#         if previous_pointer != current_pointer:
#             myLinkedList[previous_pointer][1] = myLinkedList[current_pointer][1]
#             myLinkedList[current_pointer][0] = -1
#             myLinkedList[current_pointer][1] = heapStartPointer
#             heapStartPointer = current_pointer
#         else:
#             startPointer = myLinkedList[current_pointer][1]
#             myLinkedList[current_pointer][0] = -1
#             myLinkedList[current_pointer][1] = heapStartPointer
#             heapStartPointer = current_pointer


# Question 3(d)(ii)

"""

# Binary Trees

class Node:
    def __init__(self, data):
        self.__data = data
        self.__leftPointer = None
        self.__rightPointer = None

    def insertData(self, data):
        if self.__data is None:
            self.__data = data
        else:
            if data < self.__data:
                if self.__leftPointer is None:
                    self.__leftPointer = Node(data)
                else:
                    self.__leftPointer.insertData(data)
            elif data > self.__data:
                if self.__rightPointer is None:
                    self.__rightPointer = Node(data)
                else:
                    self.__rightPointer.insertData(data)

    def inOrderTraverse(self, traversal=[]):
        if self.__leftPointer:
            self.__leftPointer.inOrderTraverse(traversal)
        traversal.append(self.__data)
        if self.__rightPointer:
            self.__rightPointer.inOrderTraverse(traversal)
        return traversal

    def preOrderTraverse(self, traversal=[]):
        traversal.append(self.__data)
        if self.__leftPointer:
            self.__leftPointer.preOrderTraverse(traversal)
        if self.__rightPointer:
            self.__rightPointer.preOrderTraverse(traversal)
        return traversal

    def printTree(self):
        if self.__leftPointer:
            self.__leftPointer.printTree()
        print(self.__data)
        if self.__rightPointer:
            self.__rightPointer.printTree()

root = Node(2)
root.insertData(6)
root.insertData(14)
root.insertData(3)
root.insertData(8)
print(root.inOrderTraverse([]))
print(root.preOrderTraverse([]))
root.printTree()

# class BinaryTree:
#     def __init__(self, root):
#         self.__root = Node(root)
#
#     def preOrderTraverse(self,startNode, traversal):
#         if startNode:
#             traversal += (str(startNode) + "-")
#             traversal = self.preOrderTraverse(startNode.__leftPointer, traversal)
#             traversal = self.preOrderTraverse(startNode.__rightPointer, traversal)
#         return traversal
#
#     def inOrderTraverse(self,startNode, traversal):
#         if startNode is not None:
#             traversal = self.preOrderTraverse(startNode.__leftPointer, traversal)
#             traversal += (str(startNode.__data) + "-")
#             traversal = self.preOrderTraverse(startNode.__rightPointer, traversal)
#         return traversal



# node1 = BinaryTree(15)
# node1.insertData(10)
# node1.insertData(12)
# node1.insertData(45)
# node1.insertData(98)
# node1.insertData(2)
# print(node1.inOrderTraverse(0, ""))

#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
#https://www.youtube.com/watch?v=NtqCPtdTbdc
#https://www.youtube.com/watch?v=j_c21K8WsrI


"""

def fib(num):
    print(f"fib({num})")
    if num <= 1:
        print("base case reached")
        return num
    else:
        print(f"fib({num - 1}) + fib({num - 2})")
        return fib(num - 1) + fib(num - 2)

print(fib(5))

"""
"""
queue = [0 for i in range(100)]
headPointer = -1
tailPointer = 0

def Enqueue(Data): # Returns boolean
    global queue
    global tailPointer
    global headPointer
    if(tailPointer < 100):
        if headPointer == -1:
            headPointer = 0
        queue[tailPointer] = Data
        tailPointer = tailPointer + 1
        return True
    return False

Success = False
for Count in range(1,21):
    Success = Enqueue(Count)
    if Success == False:
        print("Unsuccessful")
    else:
        print("Successful")

print(queue)

def RecursiveOutput(Start):
    if(Start == 0):
        return queue[Start]
    else:
        return queue[Start] + RecursiveOutput(Start - 1)

print(RecursiveOutput(19))
"""
