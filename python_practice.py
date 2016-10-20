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
#            indes +=1
#        else:
#            index +=4
#        return processed
#
#test_string_1 = "this is a good NOUN to use when you VERB your food"
#
#print process_madlib(test_string_1)
