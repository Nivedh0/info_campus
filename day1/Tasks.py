#TASK1
name=input("Enter Name:")
age=input("Enter Age:")
email=input("Enter Email:")
print("NAME:",name)
print("\nAGE:",age)
print("\nEMAIL:",email)



#TASK2
username="admin"
password="admin123"

un=input("Enter Username:")
ps=input("Enter Password")

if un==username and ps==password:
    print("Login Successfull")
else:
    print("Invalid")

    

#TASK3
age=int(input("Enter Age:"))
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")

    

#TASK4
num=int(input("Enter a number:"))
if num % 2 ==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

    


#TASK5
num=int(input("Enter the number:"))
if num ==0:
    print("zero")
elif num<1:
    print("negative")
else:
    print("Positive")
    


#TASK6
mark=int(input("Enter the Mark:"))
if mark>=80:
    print("Grade=A")
elif mark>=60:
    print("Grade=B")
elif mark>=40:
    print("Grade=C")
else:
    print("Fail")



#TASK7
a=input("Enter first number:")
b=input("Enter second number:")
print("Greatest of two number is:",max(a,b))




#TASK8
Balance=10000
amount=int(input("Enter Amount:"))
if amount <= Balance:
    newbal=Balance - amount
    print("Transaction Successfull\nCurrent Balance=",newbal)
else:
    print("Insufficient Balance")

