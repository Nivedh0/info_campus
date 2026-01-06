pswd=input("Enter Password:")
leng=len(pswd)
if leng >= 8:
    print("Strong")
elif leng >=5 and leng <=7:
    print("medium")
else:
    print("weak")
