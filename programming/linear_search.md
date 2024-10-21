# Linear search 

The linear search (sequential search) algorithm is a simple search algorithm that starts at index 0 and moves through the array one item at a time, comparing the value at the index to the item being searched for. Once the item being searched for is found the algorithm tells the user that the item was found and exits the loop. If the algorithm reaches the end of the array without finding the item then it informs the user that the item wasn't found. 

##### flow chart

<img src="https://raw.githubusercontent.com/maycra01/comp-sci-notes/328f590db324d421f45c93b12bfb68ed764ef577/Linear%20Search%20Diagram.drawio.svg" alt="Alt Text" width="1000" height="700">

##### pseudocode

```
DECLARE my_list : ARRAY[1:4] OF CHAR
DECLARE flag : CHAR
DECLARE found : BOOLEAN 

my_list ← [“a”, “b”, “w”, “t”]
found ← FALSE
i ← i
INPUT flag 

WHILE ( i < LENGTH(my_list)) AND (found = FALSE)
	IF my_list[i] = flag THEN
		OUTPUT “Flag found at index: “ i
		found ← TRUE
	END IF
	i ← i + 1

IF found = FALSE:
	OUTPUT “The flag was not found”

```
##### python
###### Note: First uses ***while and if***. Second uses ***while and for***

```
my_list = ["a", "b", "w", "t"]
flag = input("what letter would you like to find?")
found = False
i = 0

# While and If

while (i < len(my_list) - 1) and (found == False):
     if my_list[i] == flag:
         print(f"Flag found at index {i}")
         found = True
     i += 1
     break

 if found == False:
     print("The flag was not found")

# While and For

 found = False
 x = (input("num"))

 while found == False:
     for i in range(len(my_list)):
         if x == my_list[i]:
             print(f"{x} is in the list at position {i + 1}")
             found = True

 print("exit")
