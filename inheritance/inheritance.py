class Parent():
    def __init__(self, last_name, eye_color): #5 init method for class parent is called
        print("parent constructor called") #6 Parent print statement executed
        self.last_name = last_name #7 instance variables last_name of class parent initialized
        self.eye_color = eye_color #7 instance variables of class parent initialized
                                   #8 init method for class parent successfully run
    def show_info(self): #this is an instance method named show_info that Class Child inherits
        print ("Last name - " +self.last_name)
        print ("Eye color - " +self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys): #2 init method inside class child is called
        print ("Child Constructer Called") #3 Child print method gets executed (bc first line)
        Parent.__init__(self, last_name, eye_color) #4 constructor for class parent is called
        self.number_of_toys = number_of_toys #9 instance variable for number_of_toys get inititalized
                                             #10 init method for class Child is done
    #14 #METHOD OVERIDING##
    def show_info(self):
        print("Last Name - " +self.last_name)
        print("Eye Color - " +self.eye_color)
        print("Number of toys - " +str(self.number_of_toys)) #wrap around a string function to print number correctly

billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info() #calling show_info method using the Parents instance billy_cyrus
#print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5) #1 creates an instance of Class child called miley_cyrus #11 RUNS
#print(miley_cyrus.last_name) #12 print statement gets executed
#print(miley_cyrus.number_of_toys) #13 print statement gets executed
miley_cyrus.show_info() # using instance miley_cyrus to call the method show_info
    #14 ^method overwriting if instance miley_cyrus has her own show_info method 
    #if not Parent class method is used (no toys)


##STEPS FOR #12 AND #13 PRINT STATEMENTS
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
