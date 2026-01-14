from crm.customer import Customer


cid = int(input("Enter ID: "))
name = input("Enter Name: ")
email = input("Enter Email: ")
status = input("Enter Status: ")

c1 = Customer(cid, name, email, status)

if c1.is_valid():
    print("\nCustomer Details")
    c1.display()
else:
    print("\nCustomer data is invalid")
