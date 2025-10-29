def Unknown(X , Y):  # Returns integer, X passed by val, Y:INTEGER and passed by val
    if X < Y:
        print(X+Y)
        return (Unknown(X + 1,Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print(X+Y)
            return (Unknown(X-1, Y)//2)


print(f"X = 10 and Y = 15")
return_value = Unknown(10, 15)
print(f"This is the return value: {return_value}")

print(f"X = 10 and Y = 10")
return_value = Unknown(10, 10)
print(f"This is the return value: {return_value}")

print(f"X = 15 and Y = 10")
return_value = Unknown(15, 10)
print(f"This is the return value: {return_value}")

def IterativeUnknown(X, Y):  # Returns integer
    if X == Y:
        return 1
    elif X > Y:
        return 0
    else:
        return (2**(Y-X))

print(f"X = 10 and Y = 15")
return_value = IterativeUnknown(10, 15)
print(f"This is the return value: {return_value}")

print(f"X = 10 and Y = 10")
return_value = IterativeUnknown(10, 10)
print(f"This is the return value: {return_value}")

print(f"X = 15 and Y = 10")
return_value = IterativeUnknown(15, 10)
print(f"This is the return value: {return_value}")