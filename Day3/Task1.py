def validate_login(username, password):
    if username == "admin" and password == "1234":
        return True
    else:
        return False
# user=input("Enter Username:")
# pswd=input("Enter Password:")

# if validate_login(user,pswd):
#     print("Login Successfull")
# else:
#     print("invalid")

print(validate_login("admin", "1234"))  
print(validate_login("admin", "0000"))