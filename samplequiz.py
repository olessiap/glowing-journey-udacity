e_p = "EP: what is #1 __1__, & #2? __2__."
m_p = "MP:ma1 __1__. ma1__1__ ma2 __2__."
h_p = "HP:ha1 __1__, ha2 __2__, ha3__3__"

e_a = ["ea1", "ea2"]
m_a = ["ma1", "ma2"]
h_a = ["ha1", "ha2", "ha3"]

bq = ["__1__", "__2__", "__3__"]


def play():
    user_choice = raw_input("Choose a level: easy, medium, or hard:")
    if user_choice == "easy":
        process(e_p, e_a, bq)
    elif user_choice == "medium":
        process(m_p, m_a, bq)
    elif user_choice == "hard":
        process(h_p, h_a, bq)
    else:
        play()


def process(paragraph, answers, questions):
    print paragraph #display the paragraph with the blank spaces
    replaced = [] #create a list to re-build the paragraph with the filled-in answers
    paragraph = paragraph.split() #split paragraph into a list
    index = 0 #set index value to keep track of the items in teh answer list and blank list
    for word in paragraph: #goes through each word in the paragraph and checks whether it is a blank space
        if index < len(answers): #limits index to the number of answers in the answer list
            if questions[index] in word: #finds the question number in the paragraph
                tries = 2 #sets number of guesses
                while tries >= 0: #restricts the amount of guesses that can be made
                    user_input = raw_input("what are you answering? " + str(index + 1) + ":") #gets response to the current number question
                    if user_input == answers[index]: #if the user response equals the correct answer in the answer list
                        paragraph = " ".join(paragraph)
                        paragraph = paragraph.replace(word, user_input)
                        index += 1
                        tries = -1
                        print paragraph
                        paragraph = paragraph.split()
                    else:
                        print "Incorrect! Try again!"
                        print "You have " + str(tries) + " tries left."
                        tries = tries - 1
            else:
                replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

play()
