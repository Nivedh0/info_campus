<<<<<<< HEAD
#  Step 1 – Create Customer Class

# class Customer:
#     def _init_(self, cid, name, email, status):
#         self.cid = cid
#         self.name = name
#         self.email = email
#         self.status = status

# 🔹 Step 2 – Add Methods
# Add the following methods:
# 1. display() Displays customer details. 
# 2. update_status(new_status) Updates customer status with these rules: 
# * Lead → Customer 
# * Customer → Client 
# * Client → Client (cannot downgrade) 
# 3. is_deletable() Return True if status is Lead Else return False


class Customer:
    def __init__(self,cid,name,email,status):
        self.cid=cid
        self.name=name
        self.email=email
        self.status=status

    def display(self):
        print("CID:",self.cid,
              "\nname:",self.name,
              "\nemail:",self.email,
              "\nstatus:",self.status,
              "\n------------")

    def update_status(self):
        if self.status.lower() == "lead":
            self.status="Customer"
        elif self.status.lower() == "customer":
            self.status="Client"
        elif self.status.lower() == "client":
            print("Cannot downgrade")

    def is_deletable(self):
        if self.status == "lead":
            return True
        else:
            return False
        
cid=int(input("Enter ID:"))
name=input("Enter Name:")
email=input("Enter Email:")
status=input("Enter Status:")


c1=Customer(cid,name,email,status)
c1.display()
c1.update_status()
c1.display()
print(c1.is_deletable())
=======
#  Step 1 – Create Customer Class

# class Customer:
#     def _init_(self, cid, name, email, status):
#         self.cid = cid
#         self.name = name
#         self.email = email
#         self.status = status

# 🔹 Step 2 – Add Methods
# Add the following methods:
# 1. display() Displays customer details. 
# 2. update_status(new_status) Updates customer status with these rules: 
# * Lead → Customer 
# * Customer → Client 
# * Client → Client (cannot downgrade) 
# 3. is_deletable() Return True if status is Lead Else return False


class Customer:
    def __init__(self,cid,name,email,status):
        self.cid=cid
        self.name=name
        self.email=email
        self.status=status

    def display(self):
        print("CID:",self.cid,
              "\nname:",self.name,
              "\nemail:",self.email,
              "\nstatus:",self.status,
              "\n------------")

    def update_status(self):
        if self.status.lower() == "lead":
            self.status="Customer"
        elif self.status.lower() == "customer":
            self.status="Client"
        elif self.status.lower() == "client":
            print("Cannot downgrade")

    def is_deletable(self):
        if self.status == "lead":
            return True
        else:
            return False
        
cid=int(input("Enter ID:"))
name=input("Enter Name:")
email=input("Enter Email:")
status=input("Enter Status:")


c1=Customer(cid,name,email,status)
c1.display()
c1.update_status()
c1.display()
print(c1.is_deletable())
>>>>>>> a40b258a31065e8dedde132928672de512e98615
