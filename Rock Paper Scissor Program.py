import random
print("          ====================================")
print("            Welcome to \"Rock-Paper-Scissors\" ")
print("          ====================================")
print("\n")
print("r/R for choosing Rock")
print("p/P for choosing Paper")
print("s/S for choosing Scissor")
print('''
Basic Rules :
R>S : Rock beats Scissor
P>R : Paper beats Rock
S>P : Scissor beats Paper
''')
AI=0
you=0
while(True):
    u=input("Enter you choice : ")
    ai=random.randint(1,3)
    if(ai==1):
        ai='r'
    elif(ai==2):
        ai='p'
    else:
        ai='s'

    if(((u=='r' or u=='R') and ai=='r') or ((u=='s' or u=='S') and ai=='s') or ((u=='p' or u=='P') and ai=='p')):
        print("Computer's choice :",ai)
        print("Your choice :",u)
        print("Therefore; it is a TIE!!!")
        AI+=1
        you+=1
        print("Your score :",you," Computer score :",AI)
        print("\n")
    elif(((u=='r' or u=='R') and ai=='p') or ((u=='s' or u=='S') and ai=='r') or ((u=='p' or u=='P') and ai=='s')):
        print("Computer's choice :",ai)
        print("Your choice :",u)
        print("Therefore; COMPUTER wins !!!")
        AI+=1
        print("Your score :",you," Computer score :",AI)
        print("\n")
    else:
        print("Computer's choice :",ai)
        print("Your choice :",u)
        print("Therefore; YOU win !!!")
        you+=1
        print("Your score :",you," Computer score :",AI)
        print("\n")

    yn=input("Press 'y' to continue and 'n' to stop : ")
    if yn=='n' or yn=='N':
        print("Thank You !!!")
        exit(0)
