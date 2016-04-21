###### WHILE LOOPS #####

i = 0
while i !=10:
	i = i + 1
	print i

## forever loop ##

#i = 1
#while i !=10:
	#i = i + 2
	#print i 

## loop with a counting variable 

i = 0
while i < 10:
	print i
	i = i + 1

#while loops that removes all spaces 

def remove_spaces(text):
	text_without_spaces = '' # empty string for now
	while text != '':
		next_character = text[0]
		if next_character != ' ': # single sapce
			text_without_spaces = text_without_spaces + next_character
		text = text[1:]
	return text_without_spaces
print remove_spaces("hello my name is Olessia")

###
def print_numbers(n):
	i = 1
	while i <= n:
   		print i
   		i = i + 1

print_numbers(3)