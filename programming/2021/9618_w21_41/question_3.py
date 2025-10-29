ArrayNodes = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1],
              [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1],
              [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1],
              [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
            # 20 by 3 elements of type INTEGER

RootPointer = -1  # INTEGER
FreeNode = 0  # INTEGER

def AddNode(array_nodes, root_point, free_node):  # by ref
    global ArrayNodes
    global RootPointer
    global FreeNode
    node_data = int(input("Enter the data"))  # INTEGER
    if free_node <= 19:
        array_nodes[free_node][0] = -1
        array_nodes[free_node][1] = node_data
        array_nodes[free_node][2] = -1

        if root_point == -1:
            root_point = 0
        else:
            placed = False
            current_node = root_point
            while placed == False:
                if node_data < array_nodes[current_node][1]:
                    if array_nodes[current_node][0] == -1:
                        array_nodes[current_node][0] = free_node
                        placed = True
                    else:
                         current_node = array_nodes[current_node][0]
                else:
                    if array_nodes[current_node][2] == -1:
                        array_nodes[current_node][2] = free_node
                        placed = True
                    else:
                        current_node = array_nodes[current_node][2]
        free_node = free_node + 1

        ArrayNodes = array_nodes
        RootPointer = root_point
        FreeNode = free_node

    else:
        print("Tree is full")

def PrintAll():
    global ArrayNodes
    for node in ArrayNodes:
        print(f"{node[0]}  {node[1]}  {node[2]}")

for _ in range(10):
    AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll()

# def InOrder(root):
#     global ArrayNodes
#     if ArrayNodes[root][0] != -1:
#         InOrder(ArrayNodes[root][0])
#     print(ArrayNodes[root][1])
#     if ArrayNodes[root][2] != -1:
#         InOrder(ArrayNodes[root][2])

# def InOrder(root):
#     global ArrayNodes
#     if root != -1:
#         InOrder(ArrayNodes[root][0])
#         print(ArrayNodes[root][1])
#         InOrder(ArrayNodes[root][2])

# def InOrder(root, traversal):
#     global ArrayNodes
#     if root != -1:
#         traversal = InOrder(ArrayNodes[root][0], traversal)
#         traversal.append(ArrayNodes[root][1])
#         traversal = InOrder(ArrayNodes[root][2], traversal)
#     return traversal


# def InOrder(root, traversal):
#     global ArrayNodes
#     if root != -1:
#         traversal = InOrder(ArrayNodes[root][0], traversal)
#         traversal += (str(ArrayNodes[root][1]) + "-")
#         traversal = InOrder(ArrayNodes[root][2], traversal)
#     return traversal
#

def PreOrder(root):
    global ArrayNodes
    print(ArrayNodes[root][1])
    if ArrayNodes[root][0] != -1:
        PreOrder(ArrayNodes[root][0])
    if ArrayNodes[root][2] != -1:
        PreOrder(ArrayNodes[root][2])
print(PreOrder(RootPointer))

def PostOrder(root):
    global ArrayNodes
    print(ArrayNodes[root][1])
    if ArrayNodes[root][0] != -1:
        PostOrder(ArrayNodes[root][0])
    if ArrayNodes[root][2] != -1:
        PostOrder(ArrayNodes[root][2])
print(PreOrder(RootPointer))


