def add():
    num1=int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    res=num1+num2

    print("Addition value:",res)
    print("")

def sub():
    num1=int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    res=num1-num2

    print("Subtraction value:",res)
    print("")

def multi():
    num1=int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    res=num1*num2

    print("Multiplition value:",res)
    print("")
def div():

    num1=int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    res=num1/num2

    print("Divition value:",res)
    print("")

operation=["1.Addition","2.Subtraction","3.Multiplication","4.Divition","5.Exit"]
choice=0
while choice!=5:

    print("_________________")
    for i in range(len(operation)):
        print(operation[i])

    print("_________________")
    choice = int(input("WHAT WOULD YOU LIKE TO DO (1-5) ?"))

    if choice == 1:
        add()

    elif choice == 2:
        sub()

    elif choice == 3:
        multi()
        
    elif choice == 4:
        div()