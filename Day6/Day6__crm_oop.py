class CRMsystem:
    def __init__(self):
        self.customers=[]
    
    def add_customer(self):
        cid=int(input("Enter ID:"))
        name=input("Enter Name:")
        email=input("Enter Email:")
        status=input("Enter Status:")
        customer={
            "cid":cid,
            "name":name,
            "email":email,
            "status":status
        }
        self.customers.append(customer)

    def display(self):
        for c in self.customers:
            print("CID:",c['cid'],
                "\nNAME:",c['name'],
                "\nEMAIL:",c['email'],
                "\nSTATUS:",c['status']
              )
            
    def search_customer(self):
        key=input("Enter id or Email:")
        for c in self.customers:
            if str(c['cid']) == key or c['email'] == key:
                print(c)
                return
        else:
                print("No such Customer")

    def update_customer_status(self):
        key=int(input("Enter ID of the customer to be updated:"))
        for c in self.customers:
            if c['cid'] == key:
                if c['status'] == 'lead':
                    c['status'] = 'customer'
                elif c['status'] == 'customer':
                    c['status'] = 'client'
                elif c['status'] == 'client':
                    print("cannot downgrade")
                break
        else:
            print("No such customer")

    
    def delete_customer(self):
        key=int(input("Enter ID of customer to be removed:"))
        for c in self.customers:
            if c['cid'] == key:
                if c['status'] == 'lead':
                    self.customers.remove(c)
                    print(c['name'],"Removed")
                else:
                    print("Cannot remove active customer")
            else:
                print("No such customer")

    def count_by_status(self):
        lead=0
        cust=0
        cl=0
        for c in self.customers:
            if c['status'] == 'lead':
                lead+=1
            elif c['status'] == 'customer':
                cust+=1
            elif c['status'] == 'client':
                cl+=1

        print("Lead:",lead,
                "\nCustomer:",cust,
                "\nClient",cl)
            
        
crm=CRMsystem()
while True:
    print("-----MENU-----\n1.Add customer\n2.Display\n3.search\n4.update\n5.delete\n6.count_by_status\n7.Exit")
    ch=int(input("Enter choice:"))
    if ch == 1:
        crm.add_customer()
    elif ch == 2:
        crm.display()
    elif ch == 3:
        crm.search_customer()
    elif ch == 4:
        crm.update_customer_status()
    elif ch == 5:
        crm.delete_customer()
    elif ch == 6:
        crm.count_by_status()
    elif ch == 7:
        print("Exiting....")
        break
    else:
        print("invalid choice")
        break





        
