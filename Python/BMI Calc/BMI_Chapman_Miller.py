#BMI program that takes in weight/height and gives bmi/status
#nicholas chapman-miller

#class that holds information about a person and calculates bmi and status
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = (weight / (height*height)) * 703
        
        

        #if statments to determine status
        if(self.bmi < 18.5):
            self.bmiStatus = "Underweight"
        elif(self.bmi < 25):
            self.bmiStatus = "Normal"
        elif(self.bmi < 30):
            self.bmiStatus = "Overweight"
        else:
            self.bmiStatus = "Obese"

 
#function that takes in user input and creates/returns a person object        
def userInputInfo():

    pName = input("Please enter your name: ")    

    pHeight = float(input("Please enter your height (inches): ")  )

    pWeight = float(input("Please enter your weight (pounds): "))

    person = Person(pName, pHeight, pWeight)
    
    return person


userChoice = "Y"

#list to hold the bmi results/people entered
people = []

peopleListSize = 0

#keeps track of what bmi result the user is viewing
listSelection = 0


#loop continues program until user presses Q to quit
while(userChoice.upper() != "Q"):

    #user press y to input a person's info (starts here)
    while(userChoice.upper() == "Y"):


        #prompt user for info to create person variable
        tempP = userInputInfo()

        #add bmi result/person to list
        people.append(tempP)

        #print results
        print("*******************************************************")

        print(people[peopleListSize].name +"'s BMI is "+format(people[peopleListSize].bmi, ".2f")+ ". "+people[peopleListSize].name+" BMI status is "+people[peopleListSize].bmiStatus)

        print("*******************************************************")

        #increase list size after adding and calculating info
        peopleListSize = peopleListSize + 1


        #prompt user for next step
        userChoice = input("Press: Q to quit || Y to calculate another bmi || B to view the previous calculation\n")


        #user inputs b to view previous result
    while(userChoice.upper() == "B"):

        #selects the previous person or loops if list is back at start
        if(listSelection == 0):
            listSelection = peopleListSize-1
        else: 
             listSelection = listSelection-1


        print("*******************************************************")

        print(people[listSelection].name +"'s BMI is "+format(people[listSelection].bmi, ".2f")+ ". "+people[listSelection].name+" BMI status is "+people[listSelection].bmiStatus)

        print("*******************************************************")

        userChoice = input("Press: Q to quit || Y to calculate another bmi || B to view the previous calculation\n")

