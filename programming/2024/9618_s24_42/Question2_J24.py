class Node():
    # LeftPointer as INTEGER, PRIVATE
    # Data as INTEGER, PRIVATE
    # RightPointer as INTEGER, PRIVATE
    def __init__(self, pData):
        self.__LeftPointer = -1
        self.__Data = pData
        self.__RightPointer = -1

    def GetLeft(self):  # returns INTEGER
        return self.__LeftPointer

    def GetRight(self):  # returns INTEGER
        return self.__RightPointer

    def GetData(self):  # returns INTEGER
        return self.__Data

    def SetData(self, pData):
        self.__Data = pData

    def SetLeft(self, pLeft):
        self.__LeftPointer = pLeft

    def SetRight(self, pRight):
        self.__RightPointer = pRight

class TreeClass():
    # Tree as 1D array of type Node with 20 elements, PRIVATE
    # FirstNode as INTEGER, PRIVATE
    # NumberNodes as INTEGER, PRIVATE
    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNodes = 0
        self.__Tree = [Node(-1) for _ in range(20)]

    def InsertNode(self, pNewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = pNewNode
            self.__NumberNodes = self.__NumberNodes + 1
            self.__FirstNode = 0
        elif self.__NumberNodes >= 20:
            print("tree is full")
        else:
            direction = ""
            self.__Tree[self.__NumberNodes] = pNewNode
            next_pointer = self.__FirstNode
            while next_pointer != -1:
                current_pointer = next_pointer
                if self.__Tree[next_pointer].GetData() > pNewNode.GetData():
                    direction = "left"
                    next_pointer = self.__Tree[next_pointer].GetLeft()

                else:
                    direction = "right"
                    next_pointer = self.__Tree[next_pointer].GetRight()


            if direction == "left":
                self.__Tree[current_pointer].SetLeft(self.__NumberNodes)
                self.__NumberNodes += 1
            else:
                self.__Tree[current_pointer].SetRight(self.__NumberNodes)
                self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for index in range(0, self.__NumberNodes):
                node = self.__Tree[index]
                print(f"left pointer:{node.GetLeft()} data:{node.GetData()} right pointer:{node.GetRight()}")

# main

TheTree = TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()