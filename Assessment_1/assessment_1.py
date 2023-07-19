question={}
score=0

def addque():
    global question
    n=int(input("Enter no. of questions :"))
    for i in range(n):
          question={'que':input("Enter question : "),'opt 1':input("Enter option 1 : "),'opt 2':input("Enter option 2 : "),'answer':input("Enter answer : ")}
          print("Added successfully...")
          master()
          

''' question['que']=input("Enter a question : ")
options['opt 1']=input("Enter option 1 : ")
options['opt 2']=input("Enter option 2 : ")
answer['ans']=input("Enter the answer : ")   '''
                 
def viewque():
        print("Question : ",question["que"])
        print("Option 1 : ",question["opt 1"])
        print("Option 2 : ",question["opt 2"])
        print("Answer : ",question["answer"])
        quiz()

          
def deleteque():
        question.clear()
        print("Question deleted...")
        quiz()

def playquiz():
     global question,score
     print("Welcome to the quiz...")
     for i in question.keys():
          print(f"Question : {question['que']} \n Opt 1 : {question['opt 1']} \n Opt 2 : {question['opt 2']}")
          ans=input("Enter answer : ")
          if ans==question["answer"]:
               print("Correct answer...")
               score=score+1

          else:
               print("Wrong answer !")
               score=score-1
          
     print("Your final score is :",score)


     return
   
def master():
    print(str("Welcome master\n").upper().center(65))
    print(str("shake your brain and add some challenging questions..\n").upper())
    print(str("Menu").center(55).upper())

    print(str("Press 1 to add questions").center(55))
    print(str("Press 2 to view questions").center(57))
    print(str("Press 3 to delete questions").center(59))
    print(str("Press 4 to exit").center(47))
    print(2*'\n')


    operation=int(input("Which operation do you want to perform ? :"))
    while(operation!=0):
            if operation==1:
                addque()
            elif operation==2:
                viewque()
            elif operation==3:
                deleteque()
            elif operation==4:
                #exit....
                quiz()
                
            else:
                print("Invalid number...")

        
def cracker():
   
    print("Welcome cracker \n Press 1 to play quiz \n Press 2 to return to main menu \n Press 3 to exit ")
    choice=input("Enter your choice :")
    if choice==1:
        playquiz()
    elif choice==2:
         quiz()
    else:
         exit()


def quiz():
    print(str("Welcome to tops gaming challenge\n").center(65).upper())
    print(str("Select your role :\n").center(49))

    print(str("-> Quiz master     (press 1)").title().center(65))
    print(str("-> Quiz cracker    (press 2)").title().center(66))

    print(1*'\n')
    n=int(input("Enter your role :"))

    if n==1:
        master()
    elif n==2:
        cracker()
    else:
        print("Invalid choice ! Press either 1 or 2")

quiz()