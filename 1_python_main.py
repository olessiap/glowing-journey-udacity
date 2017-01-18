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

###FOR LOOPS ON LISTS = looping through the elements of a list ###

def print_all_elements(p):
    i = 0
    while i < len(p):
        print p[1]
        i = i + 1
#>>> prints out only the length of p

def print_all_elements(p):
    for e in p:
        print e

mylist = [1, 2, [3, 4]]
print_all_elements(mylist)

## for loops in lists practice

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing
#>>> abcd

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country
#>>>Beiking is the capital of China and etc

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result

print sum_list([1, 2, 3])
#>>> 6

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
    return count

print measure_udacity(['Dave', 'Ulia', 'Ugi', 'Uasss'])
#>>> 3

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

####while loop answer ###
def find_element(p,t):
    i = 0
    while i < len(p):
        if p[i] == t:
            return i
        i = i + 1
    return -1

### FOR loop answer

def find_element(p,t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1

###INDEX answer ###

def find_element (p, t):
    if t in p:
        return p.index(t)
    else:
        return -1

### IN/NOT IN answer

def find_element(p, t):
    if t not in p:
        return -1
    return p.index(t)

# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

##breaking down the problem ##


#PSEUDOCODE for daysBetweenDates (3)#
#
# days = 0
# while date1 is before date2: #<--dateIsBefore (2)
#     date1 = day after date1 #<-- nextDay (1)
#     days = days + 1
# return days


## 1. nextDay - find next day assuming month has 30 days##


#BIG HOW OLD ARE YOU IN DAYS PROBLEM BROKEN DOWN#

#def daysBetweenDates
#def nextDay(year, month, day);
#def isLeapYear(year);
# idef daysInMonth(month);

### Define a simple nextDay procedure, that assumes
### every month has 30 days.

def nextDay(year, month, day):
    """Warning: this version incorrectly
        assumes all months have 30 days!"""
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


print nextDay(2016, 10, 06) #>>2016, 10, 07
print nextDay(2016, 12, 30)
print nextDay(2017, 12, 30)
print nextDay(2017, 11, 29)

## 2.  helper procedure##
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """returns True if year1-month1-day1 is before
        year2-month2-day2. otherwise, returns False"""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

print dateIsBefore(2016, 10, 06, 2016, 10, 07) # True
print dateIsBefore(2016, 10, 06, 2016, 11, 06) # True
print dateIsBefore(2018, 10, 06, 2017, 10, 06) # False

## 3. daysBetweenDates - approximate answers using the above nextDay procedure ###

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print daysBetweenDates(2016, 10, 06, 2016, 10, 07) #>>1
print daysBetweenDates(2016, 10, 06, 2016, 11, 06) #>>30
print daysBetweenDates(2016, 10, 06, 2017, 10, 06) #>>360
print daysBetweenDates(2013, 1, 24, 2013, 6, 29) #>>155
print daysBetweenDates(2015, 1, 24, 2013, 6, 29) #>> 0

#to finish with LEAP year requirement

#1. write stub daysInMonth(year, month) #always returns 30
#2. modify nextDay(year, month, day) to use daysInMonth(year, month)
#3. test nextDay(year, month, day) using stub daysInMonth
#4. modify daysInMonth(year, month) to be correct EXCEPT for leap years
#5. test nextDay again
#6. write isLeapYear(year) helper procedure
#7. test leapYear
#8. test all test cases
def isleapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 11):
        return 31
    else:
        if month == 2:
            if isleapYear(year):
                return 29
            else:
                return 28
    return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """returns True if year1-month1-day1 is before
        year2-month2-day2. otherwise, returns False"""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

#testing#

def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay (2013, 2, 28) == (2013, 3, 1)
    assert nextDay (2013, 9, 30) == (2013, 10, 1)
    assert nextDay (2012, 2, 28) == (2012, 2, 29)
    assert daysBetweenDates(2012, 2, 28, 2012, 2, 29) == 1
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366


    print "test finished"
test()

print daysBetweenDates(1990, 10, 6, 2016, 11, 5)


# STAGE 2: WORK SESSION 5##

# list practice

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6] #> [1,2,3,4,5,6]
list2.append([5, 6]) #>[1,2,3,4[5,6]]

#use a while loop to populate a list of 20 random integers.# //changed to 3 with print statements

# Generate a random integer between 0 and 10
# Add this random integer to our list
# Do we have a list of length 20 yet?
# If not, we loop back up and go through steps 1 to 3 again while length of the list is less than 20

import random

random_list = []
list_length = 3

while len(random_list) < list_length:
    print "searching for " + str(random_list) + " in " + str(list_length)
    print "looping for the number " + str(random_list)
    random_list.append(random.randint(0,3))

print random_list
#>>[2, 4, 0, 5, 10, 6, 2, 5, 1, 10, 10, 5, 1, 0, 1, 3, 9, 1, 1, 4]

# #alternative solution #
# import random
#
# random_list = []
# list_length = 20
# count = 0
#
# while count < list_length:
#     random_list.append(random.randint(0,10))
#     count += 1
#
# print random_list
# #[3, 7, 8, 10, 8, 3, 4, 10, 6, 6, 7, 2, 5, 6, 9, 10, 9, 2, 4, 3]
#
#
# # count how many times the number 9 is in a list of 20 random numbers #

#1. Loop through each element in the list
#2. If the element is 9, we increase our count by 1
#3. Are we at the end of the list yet?
#4. If not, we loop back up and go through steps 1 to 3 again while we are still going through the list

import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

index = 0
count = 0

while index < len(random_list):
    if random_list[index] == 9:
        count = count + 1
    index = index + 1

#list that contains the counts of all occurrances of every number
#seen in the randomly generated list.

# store the list of length 11 with 0s filled in
#use this list to store count of numbers 0-10.
#Target number is the index of the list
#1. loop through each element in the list
#2. get current number in the list
#3. increment curent count for this number by 1
count_list = [1,2,3,2,2,1,1,2,3,1,2]
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0
count = 0

while index < len(random_list): #1
    number = random_list[index] #2
    count_list[number] = count_list[number] + 1 #3
    index = index +1


print count_list
#print sum(count_list) #20

## now print it like a table with header "Number | Occurance"

import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1

##

def product_list(p):
    total = 1
    for i in p:
        total = total * i
    return total

print product_list([1,2])
#> 1

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    big = 0
    for i in list_of_numbers:
        #print "searching for " + str(big) + " in " + str(list_of_numbers)
        #print "looping for the number " + str(big)
        if big < i:
            big = i
    return big

print greatest([1,2])
#>2

##SPLIT - turns words in a string into a list of those words ###
## string1.split()

#Write code for the
# function word_in_pos (meaning word in parts_of_speech), which takes in a string
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech,
# else return None.

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        print "searching for " + str(pos) + " in " + str(word)
        print "looping for this word " + str(word)
        if pos in word:
            return pos
        return None

test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

print word_in_pos(test_cases[0], parts_of_speech) #>None
print word_in_pos(test_cases[1], parts_of_speech) #>None
print word_in_pos(test_cases[2], parts_of_speech) #>PERSON
print word_in_pos(test_cases[3], parts_of_speech) #>None

# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            #user_input = raw_input("Type in a " + replacement + " ")
            word = word.replace(replacement, "Corgi") # or user_input
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)

################################################################################
###################   STAGE 3: CREATE A MOVIE SITE    ##########################
################################################################################

###take a break###

# import time
# import webbrowser
#
# total_breaks = 3
# break_count = 0
#
# print "break started at " + time.ctime()
# while break_count < total_breaks:
#     time.sleep(3)
#     webbrowser.open("https://www.youtube.com/watch?v=Ly7uj0JwgKg")
#     break_count += 1


## Renaming files in your computer ###
# 1. access the files
# 2. for each file, rename the files
import os
def rename_files():
    file_list = os.listdir("/Users/olessiapotapova/Desktop/prank")#1. get file names from a folder
    print file_list
    #2. for each file, rename filename
    saved_path = os.getcwd() #see what the current working directory is
    print("current working directory is " + saved_path)
    os.chdir("/Users/olessiapotapova/Desktop/prank")#change directory to point to the folder with images
    for file_name in file_list:#go throught each file in the list
        print("old name - " + file_name)
        os.rename(file_name, file_name.translate(None, "0123456789")) #rename each file & take out the numbers
        print ("new name - " + file_name.translate(None, "0123456789"))
    os.chdir(saved_path) #change path back to how it was
print rename_files()


#####TURTLE GAME#######

###SEND A TEXT MESSAGE###

###Class -user-defined prototype of an object that defines a set of attributes
### that characterize any object of the class (a blueprint of an object)
