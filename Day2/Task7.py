pswd=input("Enter Password:")
leng=len(pswd)
if leng >= 8:
    print("Strong Password")
elif leng >=5 and leng <=7:
    print("Medium Password")
else:
    print("Weak Password")
