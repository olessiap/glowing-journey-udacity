#1 read text
#2 check text for curse words
import urllib

def read_text():
    quotes = open("/Users/olessiapotapova/Desktop/paragraph/quotes.txt")
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)# for pirate - http://isithackday.com/arrpi.php?text=
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print "Profanity Alert!!!"
    elif "false" in output:
        print "No curse words here!"
    else:
        print "couldn't scan the document"

read_text()
