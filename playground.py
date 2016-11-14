e_p = "__1__ & two"

e_a = ["ea1", "ea2" ]

bq = ["__1__", "__2__"]

def play_game():
    user_input = raw_input("pick level from easy or medium: ")
    if user_input == 'easy':
        return process(e_p, e_a, bq)
    else:
        play_game()

def process(paragraphs, answers, questions):
    print paragraph #//__1__, & __2__
    replaced = []##2
    paragraph = paragraph.split() ##2
    index = 0 ##1
    for word in paragraph:
        while index <= len(answers):
            if word == index:
                user_input = raw_input("what is 1st answer?" + str(index) + ":")
                paragraph = paragraph.replace(word, user_input)
                replaced = " ".join(paragraph)
                print replaced
        if word != index:
            print "move on to 2nd word in paragraph"
    return replaced

play_game


            #replaced.append(word)
#PLAY_GAME
#user_choice = 'easy'

#PROCESS
#paragraph = ["__1__" "&" "two"]
#answers = 0:ea1
#questions = 0:__1__
#replaced = empty list
#index = 0
#word = __1__

#user_input = ea1
#printed: __1__ & two --> ae1 --> ae1 & two


#replaced = ae1 & 2
#word = 0:__1__
