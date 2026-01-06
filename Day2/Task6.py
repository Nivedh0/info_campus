print("1.ADD \n2.SUB \n3.MUL \n4.EXIT")
choice=int(input("Enter Choice:"))
if choice==4:
    print("Exiting")
else:
    a=int(input("Enter first numbers:"))
    b=int(input("Enter second numbers:"))

    if choice==1:
        print("Result:",a+b)
    elif choice==2:
            print("Result:",a-b)
    elif choice==3:
        print("Result:",a*b)

    else:
        print("invalid choice")


