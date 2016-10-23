### STRINGS AND FIND ***
text = "this is my text"
print text.find('my')

###find second occurance of zip

text = "all zip files are zipped"
firstZip = text.find("zip")
print text.find("zip", firstZip + 1)


### STRING.REPLACE ###

## replace the NOUN with duck and VERB with waddle ##
sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace('NOUN', 'duck')
sentence = sentence.replace('VERB', 'waddle')
print sentence

###
s = 'jol'
print s.find(s+ '!!!') + 1


print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

#STRINGS#

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[:1] + t[2:]
print s[:5] + t[6:]
print s[:-2] + t [-3:]

## given any string S, the following always equal to S

###
s = 'hi'
('a' + s) [1:]
print s

###
s + ''
print s

###
s[0:]
print s

##STRING SLICING##

# Insert the proper slicing indices for the substring variable
# so that the slice is a string that contains everything after "A NOUN".
# For example, if we wanted to store everything after "went", the returned
# string would be equal to sentence[11:].

sentence = "A NOUN went on a walk."
substring = sentence[6:]
print substring

###
# Set noun_replacement and verb_replacement to your own noun and verb strings.
# Then, concatenate the variables substring1-3, noun_replacement, and
# verb_replacement and assign the result to the variable new_sentence so that
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "cat" # your noun here
verb_replacement = "tickle" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement +substring3
print new_sentence

##STRINGS AND VARIABLES##

##strings and quotes
div_with_class = '<div class="concept-description">'
just_the_class = div_with_class[5:-1]
print just_the_class

## printing multiple lines

print """I am a string
that takes up
multiple lines."""

##


print '''
<div class="concept">
    <div class="concept-title">
        Multi-line strings
    </div>
'''

##print the div_element variable on 3 different lines
div_element = "<div>I am learning to code!</div>"

opening_tag = div_element[:5]
indent      = '    ' # this is just a string with 4 spaces.
inner_text  = div_element[5:-6]
closing_tag = div_element[-6:]

print opening_tag
print indent + inner_text
print closing_tag


####################### FUNCTIONS #######################

def say_hello(name):
	greeting = "Hello " + name + "!"
	return greeting

print say_hello("Mariam")
print say_hello("Andy")

###print udacity###

def rest_of_string(s):
	return s[1:]

print rest_of_string('Dudacity')


#### sum does nothing ###

def sum(a,b):
	print "enter sum!"
	print "a is", a
	a = a + b
	print "a is", a
	#return a // returns 3

print sum (1,2)


### function that prints Hello World ###

def some_function():
	print "Hello World!"

some_function() ## 'calling' the function

### function 'square' that takes a number and outputs its square  ###

def square(n):
	return n * n

print square(5)
#>>>25

### take 3 inputs and return their sum ###

def sum3(a, b, c):
	return a + b + c

print sum3(1,2,3)
#>>>6

### procedure, ABBAIZE that takes 2 strings as inputs
### and outputs a string
### that is the first input,
### followed by 2 repititions of the second input
### followed by first input

def abbaize (a, b):
    return a + b * 2 + a

print abbaize ('a', 'b')

#>>> abba

#### def udacify
### takes string input
### outpus string with uppercase "U" followed by the input string

def udacify (s):
    return 'U' + s

print udacify('dacity')
#>>> Udacity

#### IF STATEMENTS ######

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger (a, b):
    if a > b:
        return a

print bigger (4, 2)
#>>>4

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Only D names

def is_friend (name):
    if name [0] == 'D':
        return True
    else:
        return False

print is_friend ('Diane')
#>>>True

## same as above but with D or N

def is_friend (name):
    if name[0] == 'D' or name[0] == 'N':
        return True
    else:
        return False

print is_friend('Diane')
print is_friend('Nancy')
#>>>abba

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
#>>>>>>>> 0-9

i = 0
while i != 10:
    i = i + 1
    print i
#>>> 1-10

#i = 1
#while i !=10:
#    i = i + 2
    #print i
#>>>> INFINITE LOOP

i = 0
while i < 10:
    print i
    i = i + 1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces

print remove_spaces("hello my name is andy how are you?")

# Define a procedure that takes as input a positive whole number
# & prints out all the whole numbers from 1 to the input number

def print_numbers(n):
    i = 1
    while i <= n:
        print i
        i = i + 1

print_numbers(3)
#>> 1,2,3

# ^ another solution

def print_numbers(n):
    i = 0
    while i < n:
        i = i + 1
        print i

print_numbers(4)

##### BREAK #####

def print_numbers(n):
    while True:
        if i > n:
            BREAK
        print i
        i = i + 1

### from WORK SESSION 4 ###

#Define a procedure weekend which takes a string as its input, and
#returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False

print weekend('Monday')
print weekend('Sunday')

## define procdedure, countdown that
## takes a positive whole nubmer as input
## and prints out a countdown from that number to 1
## followed by Blastofff!

def countdown(n):
    while n >= 1:
        print n
        n = n - 1
    print 'Blastoff!'

print countdown(3)

## define a procedure, median that
## takes 3 numbers as its inputs
## and outputs the median of the 3 numbers

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger (b,c)
    if big == b:
        return bigger (a,c)
    else:
        return bigger (a,b)

print(median(1,2,3))

# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes return
# the string "sofa" if the number is 0, else return "llama".

#from random import randit
#
#def random_noun():
#    random_num = randit(0,1)
#    if random_num == 0:
#        return 'sofa'
#    else:
#        return 'llama'
#
##random verb madlib
#from random import randit
#def random_verb():
#    random_num = randit(0,1)
#    if random_num == 0:
#        return 'run'
#    else:
#        return 'kayak'
#
### MADLIB PROBLEM ALL TOGETHER
#
#(def random_noun():
#    random_num = randit(0,1)
#    if random_num == 0:
#        return 'sofa'
#    else:
#        return 'llama'

#def random_verb():
#    random_num = randit(0,1)
#    if random_num == 0:
#        return 'run'
#    else:
#        return 'kayak'
#
#def word_transformer(word):
#    if word == 'NOUN':
#        return random_noun()
#    if word == 'VERB':
#        return random_verb()
#    else:
#        return word[0]
#
#def process_madlib(mad_lib):
#    processed = ""
#    index = 0
#    box_length = 4
#    while index < len(madlib):
#        frame = madlib[index:index + box_length]
#        to_add = word_transformer(frame)
#        processed += to_add
#        if len(tp_add)==1:
#            index +=1
#        else:
#            index +=4
#        return processed
#
#test_string_1 = "this is a good NOUN to use when you VERB your food"
#
#print process_madlib(test_string_1)

###### LISTS: STRUCTURED DATA #######

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list
#>>>[3.14159, 2.71828, 1.61803]

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like strings"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi
#>>>3.14159
#>>>[2.71828, 1.61803]

## given the variable, days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##define procedure, how_many_days that
## takes input a number representing a month
## outputs the number of days in that month

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def how_many_days(month_number):
    return days_in_month[month_number - 1]

###looking for specific value in 4th list###

print how_many_days(10)

beatles = [['John', 1940], ['Paul', 1942],
            ['George', 1943], ['Ringo', 1940]]

print beatles[3][1]
#>>> 1940

### LISTS: MUTATION = change the value of a list after its creation #####

p = ['H', 'e', 'l', 'l', 'o']
print p
#>>> ['H', 'e', 'l', 'l', 'o']
p[0] = 'Y'
print p
#>>> ['Y', 'e', 'l', 'l', 'o']
p[4] = '!'
print p

###ALIASING = when 2 variables refer to the same list  ####

## whats the value of agent[2] after the following code:###

#spy = [0, 0, 7]
#agent = spy
#spy[2] = agent[2] + 1
#>>>8

spy = [0,0,7]

def replace_spy(p):
    p[2] = p[2] + 1

replace_spy(spy)
print spy

### 1. LIST OPERATOR "APPEND" = adds a new element to the end of the list ###

stooges = ['Moe', 'Larry', 'Curly']
stooges.append('Shemp')
print stooges
#>>>['Moe', 'Larry', 'Curly', 'Shemp']

### 2.LIST OPERATOR "+" = like cocatination in Strings. makes NEW LIST

### 3.LIST OPERATOR "LEN(<list>)" outputs NUMBER of elements in the input

## Whats the value of len(p) after this code

p = [1,2]
p.append(3)
p = p + [4, 5]
print len(p)
#>>> 5

p = [1, 2]
q = [3, 4]
p.append(q)
print p
#>>>[1, 2, [3, 4]]
print len(p)
#>>>3
