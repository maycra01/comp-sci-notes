# Linear search 
##### flow chart



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
