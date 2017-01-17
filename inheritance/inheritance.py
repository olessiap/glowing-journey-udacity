class Parent():
    def __init__(self, last_name, eye_color): #5 init method for class parent is called
        print("parent constructor called") #6 Parent print statement executed
        self.last_name = last_name #7 instance variables last_name of class parent initialized
        self.eye_color = eye_color #7 instance variables of class parent initialized
                                   #8 init method for class parent successfully run

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys): #2 init method inside class child is called
        print ("Child Constructer Called") #3 Child print method gets executed (bc first line)
        Parent.__init__(self, last_name, eye_color) #4 constructor for class parent is called
        self.number_of_toys = number_of_toys #9 instance variable for number_of_toys get inititalized
                                             #10 init method for class Child is done

#billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5) #1 creates an instance of Class child called miley_cyrus AND #11 instance created successfully
print(miley_cyrus.last_name) #12 print statement gets executed
print(miley_cyrus.number_of_toys) #13 print statement gets executed

#1 creates an instance of Class child called miley_cyrus
#2 init method inside class child is called
#3 Child print method gets executed (bc first line)
#4 constructer for class parent is called
#5 init method for class parent is called
#6 Parent print statement executed
#7 instance variable last_name of class parent inititalized
#7 instance variable eye_color of class parent inititalized
#8 init method for class parent successfully run
#9 instance variable for number_of_toys gets inititalized
#10 init method for class Child is done
#11 instance of class Child created successfully
#12 last_name print statement gets executed
#13 number_of_toys print statement get executed
