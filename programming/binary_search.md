Binary Search 

pseudocode

```
DECLARE my_list : ARRAY[1:9] as INTEGER
DECLARE flag :  INTEGER 
DECLARE index : INTEGER 
DECLARE upper_bound : INTEGER
DECLARE lower_bound : INTEGER
DECLARE found : BOOLEAN

OUTPUT “Enter the number you want to find”
INPUT flag

my_list ← [1, 3, 11, 18, 30, 36, 40, 41, 43] 
upper_bound ← LENGTH(my_list) 
lower_bound ← 1
Index ← 1
found ← FALSE

WHILE (lower_bound <> upper_bound)  AND  (found = FALSE)
	index ← (upper_bound + lower_bound) DIV 2
	IF flag = my_list[index] then
		found ← TRUE
	ENDIF
	
	IF flag > my_list[index] THEN
		lower_bound ← index  + 1
`	ENDIF


	IF flag < my_list[index] THEN
		upper_bound ← index - 1
	END IF 

IF found = TRUE
	OUTPUT “The value: ”, flag, “was found at index: “, index
END IF

IF found = FALSE:
	OUTPUT “The value: “, flag, “is not in the list” 

```
python

```
my_list = [1, 2, 5, 8, 11, 14, 18, 46, 58]

upper_bound = len(my_list)-1
lower_bound = 0
flag = int(input("Please enter item to be found"))
found = False
index = 0

while (found == False) and (lower_bound != upper_bound):
    index = (upper_bound + lower_bound) // 2
    if flag == my_list[index]:
        found = True

    elif flag > my_list[index]:
        lower_bound = index + 1

    elif flag < my_list[index]:
        upper_bound = index - 1

if found:
    print(f"Item {flag} found at index: {index}")
else:
    print("Item not found")
```
