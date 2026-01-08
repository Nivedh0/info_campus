# Create a list to store customer names.
# Allow the user to:

# Add a customer

# Remove a customer

# Display all customers

list=[]
while True:
    print("\n1.ADD\n2.REMOVE\n3.DISPALY\n4.EXIT")
    ch=int(input("Enter choice:"))
    if ch==1:
        list.append(input("Add a customer:"))
        print("Customer added")
    elif ch==2:
        a=input("Enter the name of customer to be removed:")
        if a in list:
            list.remove(a)
            print(a," removed")
        else:
            print("No such customer")
    elif ch==3:
        print(list)
    elif ch==4:
        break
        


