attempts=3
while attempts>0:
    user=input("Enter Username:")
    pswd=input("Enter password:")


    if user=="admin" and pswd=="123":
            print("Login Successfull")
            break

    else:
            attempts-=1
            print("invalid\nAttempts left=",attempts)
             
if attempts==0:
    print("No attempts left")

