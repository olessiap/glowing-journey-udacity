e_p = "__1__ & __2__"

e_a = ["ea1", "ea2" ]

bq = ["__1__", "__2__"]

def play_game():
    user_choice = raw_input("pick level from easy or medium: ")
    if user_choice == 'easy':
        process(e_p, e_a, bq)
    else:
        play_game()

def process(paragraph, answers, questions):
    print paragraph #//__1__ & __2__
    replaced = []
    paragraph = paragraph.split() #waswrong after index
    index = 0 #was wrong
    for word in paragraph:
        if index < len(answers):
            if questions[index] in word:
                user_input = raw_input("what are you answering? " + str(index + 1) + ":") #waswrong
                if user_input == answers[index]:
                    paragraph = " ".join(paragraph) #makes paragraph string again
                    paragraph = paragraph.replace(word, user_input) #replaces word for user_input
                    index += 1 #waswrong
                    print paragraph
                    paragraph = paragraph.split() #splits it again for round2 and on
                else:
                    print "Incorrect, try again"
            else:
                replaced.append(word) #waswrongly indented outside of l21 // adds word to replaced list
    replaced = " ".join(replaced) # makes list into a string
    return replaced #SOMETHING WRONG HERE! http://www.pythontutor.com/live.html#mode=edit

play_game()


            #replaced.append(word)

#user_input = ea1
#printed: __1__ & two --> ae1 --> ae1 & two
#paragraph = ["__1__" "&" "two"]
#answer = 0:ea1
#bq = 0:__1__
#index = 0
#replaced = ae1 & 2
#word = 0:__1__


#set up easy paragraph
#set up easy answers
#set up bq
#set up level rules(play_game)
#ask user which level
#if user picks easy, go through easy level
#based on level go through process
##print chosen paragraph
#set up empty list to hold developing paragraphs
#set index to 0 to keep track of the items in the answer list
#break up the paragraph into a list
#identify 1st word in paragraph
#while index is <= to # of answers -> run through list of words in paragraph
# if 1st word in paragraph = 1st question
# ask user to answer q1
# if user_input1 = answer1(index)
# make paragraph a string again
# replace 1st word in paragraph with user_input1
# add 1 to index
# print paragraph with user_input instead of word
# make paragraph a list again
#if user_input1 is wrong
#print "wrong, try again" (need to add tries)


#if 1st word in paragraph not in 1st question:
# add 1st word to replaced list
## print "now move on to 2nd word in paragraph"

# move on to 2nd word in paragraph
# if 2nd word in paragraph does NOT = 2nd question
# add 2nd word in paragraph to replaced list
