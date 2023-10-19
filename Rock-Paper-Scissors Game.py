import random

print("Enter 1 for rock \n 2 for paper \n 3 for scissor")
ch='y'
round=0
win=0
loss=0
draw=0

while(ch=='y'):
    choice=int(input("Enter your choice"))
    round+=1
    if(choice>3 and choice<1):
        print("Invalid Input")
    else:


        comp_choice = random.randint(1, 3)
        if (choice == 1):
            print("User's choice is rock")
        elif (choice == 2):
            print("User's choice is paper")
        else:
            print("User's choice is scissor")
        if (comp_choice == 1):
            print("Computer's  choice is rock")
        elif (comp_choice == 2):
            print("Computer's choice is paper")
        else:
            print("Computer's choice is scissor")
        if (choice == comp_choice):

            print("Draw game")
            draw+=1
        elif (choice == 1 and comp_choice == 2):
            print("Rock vs paper: \n")
            print("You loose")
            loss += 1
        elif (choice == 1 and comp_choice == 3):
            print("Rock vs scissor: \n")
            print("You win")
            win+=1
        elif (choice == 2 and comp_choice == 1):
            print("Paper vs Rock: \n")
            print("You win ")
            win += 1

        elif (choice == 2 and comp_choice == 3):
            print("Paper vs Scissor : \n")
            print("You loose ")
            loss += 1
        elif (choice == 3 and comp_choice == 1):
            print("Scissor vs Rock: \n")
            print("You loose")
            loss+=1
        elif (choice == 3 and comp_choice == 2):
            print("Scissor vs Paper: \n")
            print("You win")
            win+=1



    print("Do you wish to continue Y/N")
    ch=input()
print("\n\nUser played",round,"times and won ",win,"times,lost",loss,"times and drew",draw,"times")

#record
