print("                   Welcome to Calci !!!")
print("Please enters the numbers and specify the operation (+.-.x./)")
print("\n")
while(True):
    n1=int(input("Enter the FIRST Number : "))
    n2=int(input("Enter the SECOND Number : "))
    operation=input("Specify the desired operation : ")
    if operation=='+':
        print("The sum of",n1,"and",n2,"is =",n1+n2,"\n")
    elif operation=='-':
        print("The difference of",n1,"and",n2,"is =",n1-n2,"\n")
    elif operation=='x':
        print("The product of",n1,"and",n2,"is =",n1*n2,"\n")
    elif operation=='/':
        print("The division of",n1,"and",n2,"gives =",n1/n2,"\n")
    else:
        print("Invalid Operation")
        print("Select + - x or / ")

    opera=input("Press 'y' to continue and 'n' for terminate : ")
    print("\n")
    if opera=='n' or opera=='N':
        exit(0)
