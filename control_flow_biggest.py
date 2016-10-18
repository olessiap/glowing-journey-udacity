# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    if b > c:
        return b
    else:
        return c

print biggest(101,2782,3)

### another solution to above

def bigger (a, b):
    if a > b:
        return a
    else:
        return b

def biggest (a, b, c):
    return bigger (bigger (a, b), c )

print biggest (1343,43335,5)

##### WHILE LOOPS #####

i = 0
while i < 10:
    print i
    i = i + 1
#>>> 0-9

i = 0
while i != 10:
    i = i + 1
    print i
#>>> 1-10
