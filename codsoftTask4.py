import random

user_score=0
comp_score=0
def RPS():
    global user_score, comp_score
    user_choice=input("Enter Rock/Paper/Scissors: ").capitalize()
    choices=['Rock','Paper','Scissors']
    comp_choice=random.choice(choices)

    if user_choice==comp_choice:
        status="Tie"

    elif (user_choice=='Rock' and comp_choice=='Scissors') or (user_choice=='Paper' and comp_choice=='Rock') or (user_choice=='Scissors' and comp_choice=='Paper'):
        status="User"

    elif (user_choice=='Paper' and comp_choice=='Scissors') or (user_choice=='Rock' and comp_choice=='Paper') or (user_choice=='Scissors' and comp_choice=='Rock'):
        status="Computer"

    elif user_choice not in choices:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        return

    print("Computer: "+comp_choice+"\n"+"User: "+user_choice+"\n"+"Winner: "+status)

    if status=="User":
        user_score+=1
    elif status=="Computer":
        comp_score+=1

    print("Scores:-" +"\n"+  "User: " + str(user_score) + "\n"+ "Computer: " + str(comp_score))   

RPS()
while True:
    ask=input("Play Again? (Yes/No)").capitalize()
    if ask=='Yes':
        RPS()
    else:
        print("Thank You, come again soon!")
        break