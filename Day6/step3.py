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
crm.add_customer()
crm.add_customer()
#crm.display()
#crm.search_customer()
#crm.update_customer_status()
#crm.display()
#crm.delete_customer()
#crm.display()
crm.count_by_status()




        
