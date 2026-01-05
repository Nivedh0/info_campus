Balance=10000
amount=int(input("Enter Amount:"))
if amount <= Balance:
    newbal=Balance - amount
    print("Transaction Successfull\nCurrent Balance=",newbal)
else:
    print("Insufficient Balance")
