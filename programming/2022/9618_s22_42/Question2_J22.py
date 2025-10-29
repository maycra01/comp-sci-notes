from random import randint

def OutputData(array):
    array_length = 10

    for Y in range(0, array_length):
        for X in range(0, array_length):
            if array[Y][X] < 10:
                print(f"{array[Y][X]}   ", end="")
            elif array[Y][X] == 100:
                print(f"{array[Y][X]} ", end="")
            else:
                print(f"{array[Y][X]}  ", end="")
        print()

def BinarySearch(search_array, lower, upper, search_value):  # returns INTEGER
   if upper >= lower:
       mid = (lower + (upper)) // 2
       if search_array[0][mid] == search_value :
           return mid
       else:
           if search_array[0][mid] > search_value:
               return BinarySearch(search_array, lower, mid - 1, search_value)
           else:
               return BinarySearch(search_array, mid + 1, upper, search_value)
   return -1

array_data = [[randint(1,100) for _ in range(10)] for _ in range(10)]
# 2D array of type Integer, with 10 by 10 elements

OutputData(array_data)
array_length = 10
for X in range(0, array_length):
    for Y in range(0, array_length - 1):
        for Z in range (0, array_length - Y - 1):
            if array_data[X][Z] > array_data[X][Z+1]:
                temp_value = array_data[X][Z]
                array_data[X][Z] = array_data[X][Z+1]
                array_data[X][Z+1] = temp_value
print("")
OutputData(array_data)

search_value = int(input("Enter a seach value"))
print(f"Binary search output is {BinarySearch(array_data, 0, 9, search_value)}")
search_value = int(input("Enter a search value"))
print(f"Binary search output is {BinarySearch(array_data, 0, 9, search_value)}")