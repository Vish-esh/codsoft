# calculator
ch='y'
def add(a,b):
    print("a+b:",a+b)
def subtract(a,b):
    print("a-b:",a-b)
def multiply(a,b):
    print("a*b:",a*b)
def divide(a,b):
    print("a/b is",a/b)
while (ch=='y'):
    a = float(input("Enter first  number \t"))
    b = float(input("Enter second number \t"))
    print("For addition press 1")
    print("For subtarction press 2")
    print("For multiplication press 3 ")
    print("For division press 4 ")
    x=int(input("Enter your choice"))


    if(x==1):
        add(a,b)

    elif(x==2):
        subtract(a,b)

    elif(x==3):
        multiply(a,b)

    elif(x==4):
        divide(a,b)

    else:
        print("Invalid input")
    ch=input("Do you wish to continue Y/N")


