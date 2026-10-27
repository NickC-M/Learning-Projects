#nicholas chapman-miller
#Grade Report Program

class ReportCard:

    def __init__(self, name: str):
        self.name = name
        self.quiz: list[float] = []
        self.project: float = 0.0
        self.exam: float = 0.0
        self.qavg: float = 0.0
        self.final: float = 0.0

    def averageGrades(self):
        #average of quiz list
        self.qavg = float(sum(self.quiz) / len(self.quiz))
        #calculate weighted grade
        self.final = (self.qavg * 0.5)+(self.project * 0.3)+(self.exam * 0.2)





userC1 = "y"

#count so every text file is dif name
count = 1

while(userC1.lower() == "y"):
    
    print("************************************\n\tReport Card Program\n************************************\n")

    name = input("What is your name?\n")

    reportCard = ReportCard(name)

    print("************************************")

    userC2 = "y"
    qCnt = 1

    while(userC2.lower() == "y"):

        grade = input("Quiz Grade #"+format(qCnt)+": "  )
        
        #check if input is valid
        if(grade.isdecimal() == False or int(grade) < 0 or int(grade) > 100):
            print("Invalid Input :/, whole numbers 0 - 100 only")
            continue

        #add to list of quiz grades
        reportCard.quiz.append(float(grade))

        qCnt = qCnt + 1

        userC2 = input("Do you have another quiz grade? (y / n)\n")

    print("************************************")

    projectGrade = input("Final Project Grade:  ")

    #check if input is valid
    while(projectGrade.isdecimal() == False or int(projectGrade) < 0 or int(projectGrade) > 100):
        print("Invalid Input :/, whole numbers 0 - 100 only")
        projectGrade = input("Final Project Grade:  ")

    #add to report card
    reportCard.project = float(projectGrade)
    
    print("************************************")

    examGrade = input("Final Exam Grade:  ")

    #check if input is valid
    while(examGrade.isdecimal() == False or int(examGrade) < 0 or int(examGrade) > 100):
        print("Invalid Input :/, whole numbers 0 - 100 only")
        examGrade = input("Final Exam Grade:  ")

    #add to report card
    reportCard.exam = float(examGrade)

    #average all the grades
    reportCard.averageGrades()

    #different file name every iteration
    fileName = "ReportCard"+format(count)+".txt"

    #write report card to file
    with open(fileName, "w") as f:
        print("******************************************", file=f)
        print("\tCentral Community College", file=f)
        print("    CPT 227 Advanced Python Programming\n", file=f)
        print("\t   "+reportCard.name+"'s Report Card ", file=f)
        print("  -----------------------------------------", file=f)
        print("\t Quiz Average: "+format(reportCard.qavg, ",.2f"), file=f)
        print("\t Final Project: "+format(reportCard.project, ",.2f"), file=f)
        print("\t Final Exam: "+format(reportCard.exam, ",.2f"), file=f)
        print("\t Final Grade: "+format(reportCard.final, ",.2f"), file=f)

        print("******************************************", file=f)

    print("\tReport Card Printed !!! File Name: "+fileName)
        
    userC1 = input("Would you like another report card? (y / n)")

    count = count +1


print("! ! ! T H A N K  Y O U ! ! !")