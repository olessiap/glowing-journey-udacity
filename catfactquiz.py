fun_facts = "Cats are the most popular __1__ in the US. There are __2__ million pet cats. A group of cats is called a __3__. The largest litter of kittens produced __4__ kittens."
random_facts = "Cats can move their __1__ 180 degrees. When a family cat died in ancient __2__, family members would shave off their __3__ as they mourned. Cats cant taste __4__."
serious_facts = "Cats and humans have nearly identical sections of the brain that control __1__ . A cats nose is ridged with a unique pattern, just like a human __2__. Cats have free-floating __3__ bones that attach their __4__ to their __5__, which allows them to squeeze through very small spaces. Cats are really cool."

fun_answers = [ "pet", "88", "clowder", "19"]
random_answers = ["ears", "Egypt", "eyebrows", "sweetness"]
serious_answers = ["emotion", "fingerprint", "clavicle", "shoulders", "forelimbs"]

blank_questions = ["__1__", "__2__", "__3__", "__4__", "__5__"]

def take_quiz(): #sets up the different game levels that gets processed depending on user choice
    user_choice = raw_input("Which cat facts do you want to answer? Pick either fun, random, or serious: ")
    if user_choice == "fun":
        process(fun_facts, fun_answers, blank_questions)
    elif user_choice == "random":
        process(random_facts, random_answers, blank_questions)
    elif user_choice == "serious":
        process(serious_facts, serious_answers, blank_questions)
    else:
        take_quiz()

def process(fact, answers, questions): #sets up the steps of the program
    print fact #prints fact with all the blanks
    replaced = [] #create a list to re-build the fact with
    fact = fact.split() #split fact into a list
    index = 0 # keeps track of items in the answer list and blank list
    for word in fact: #goes through each word in the fact starting at index 0
        if index < len(answers): #limits index to the number of answers in the answer list
            if questions[index] in word: #finds the question number in the current word
                tries = 3 #sets limit to number of guesses
                while tries >= 0: #allows user to try until runs out of tries
                    user_input = raw_input("Type in the answer to number " + str(index + 1) + ": ") # asks user to answer question number
                    if user_input == answers[index]: #if the user response equals the correct answer in the answer list
                        fact = " ".join(fact) #joins the list fact together
                        fact = fact.replace(word, user_input) #replaces word with user_input in fact
                        replaced.append(user_input) #adds user_input to the replaced list
                        index += 1 #adds 1 to index to move to the next answer/question
                        tries = -1 # resets number of tries to set up for next question
                        print fact #prints fact / replaces blank question with user answer
                        fact = fact.split() # splits the fact to set up for next question
                    else:
                        print "WRONG, Try again"
                        print "You have " + str(tries) + " tries left."
                        tries = tries - 1 #subracts number of tries by 1
            else:
                replaced.append(word) #adds word to replaced list
    replaced = " ".join(replaced) #joins the replaced list together
    return replaced

take_quiz()




#set up easy fact
#set up easy answers
#set up fill in the blanks
#set up level rules(take_quiz)
#ask user which level
#if user picks easy, go through easy level
#based on level go through process
##print chosen fact
#set up empty list to hold developing facts
#set index to 0 to keep track of the items in the answer list
#break up the fact into a list
#identify 1st word in fact
#while index is <= to # of answers -> run through list of words in fact
# if 1st word in fact = 1st question
# ask user to answer q1
# if user_input1 = answer1(index)
# make fact a string again
# replace 1st word in fact with user_input1
# add 1 to index to move on to next word
# print fact with user_input instead of word
# make fact a list again
# add word to replaced string
#if user_input1 is wrong
#print "wrong, try again" (need to add tries)



#TODOLIST
#add tries
#add possible format answers to take_quiz_game
#add else statement that says "didn't get that try again" and asks the question again
