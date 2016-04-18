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


#### FUNCTIONS #####

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

### function abbaize that takes 3 strings as inputs and outputs a string that is the first input,
###followed by 2 repetitions of the second input, followed by the first input

def abbaize(a,b):
	return a + b + b + a

print abbaize('a', 'b')
#>>>abba

### define function that takes a string input and outputs a string with uppercase 'U'
###followed by the input stirng

def udacity(s):
	return 'U' + s

print udacity('daman')


########### IF STATEMENTS #############

## function that takes 2 numbers as inputs & outputs the greater of the 2 inputs

def bigger(a, b):
	if a > b:
		return a

	else:
		return b

print bigger(2,7)
#>>>7

### define a procedure that takes a string and returns a Boolean
### indicating if the input string is a friend.
### Only friends with names that start with D

def is_friend(name):
	if name[0] == 'D':    ## return name [0] == 'D' /// instead of is/else is the same thing
		return True
	else:
		return False

print is_friend('Diane')
#>>>True

## ### define a procedure that takes a string and returns a Boolean
### indicating if the input string is a friend.
### Only friends with names that start with D or N

def is_friend(name):
	if name[0] == 'D' or name[0] == 'N':
		return True
	else:
		return False

print is_friend('Nora')
print is_friend('Zoe')

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(number1, number2, number3):
	if number1 > number2:
		return number1
	else:
		return number3
	if number2 > number3:
		return number2
	if number3 > number1:
		return number3

print biggest(3, 6, 9)
#>>> 9
print biggest(9, 3, 6)
#>>> 9
