customers = {
    1: {"name": "Arun", "email": "arun@gmail.com", "status": "Lead"},
    2: {"name": "Meera", "email": "meera@gmail.com", "status": "Customer"},
    3: {"name": "john", "email": "john@gmail.com", "status": "Lead"}
}

while True:
    print("---MENU---\n1. Display All Customers\n2. Add New Customer\n3. Update Customer Status\n4. Search Customer\n5. Delete Customer\n6. Display Customers by Status\n7. Count Customers by Status\n8. Exit")
    ch=int(input("Enter choice:"))
    if ch == 1:
        for key,cust in customers.items():
            print("ID:",key,"\n",
                  "NAME:",cust['name'],"\n",
                  "EMAIL:",cust['email'],"\n",
                  "STATUS:",cust['status'],"\n------------------")
            
    elif ch == 2:
        key=int(input("Enter ID:"))
        if key in customers:
            print("Customer ID already exists")
        else:
            name=input("Enter Name:")
            email=input("Enter Email:")
            status=input("Enter Status(Lead/Customer):")

            existing_email=set()
            for cust in customers.values():
                existing_email.add(cust["email"])
            if email in existing_email:
                    print("Email already exists")
            else:
                customers[key]={
                        'name':name,'email':email,'status':status
                    }
                print("Customer added Successfully!")

    elif ch == 3:
        key=int(input("Enter Customer ID:"))
        if key in customers:
            current_status=customers[key]['status']
            if current_status=='lead':
                customers[key]['status']='Customer'
            elif current_status == 'Customer':
                customers[key]['status']='Client'
            else:
                print("Status cannot be downgraded")
            print("Status updated:"+current_status+"->"+customers[key]['status'])
        else:
            print("No such Customer")  
        
    elif ch == 4:
        key = input("Enter Customer ID or Email: ")

        for cid in customers:
            if str(cid) == key or customers[cid]["email"] == key:
                print(customers[cid])
                break
        else:
            print("Customer not found!")

    elif ch == 5:
        key=int(input("enter custommer ID:"))
        if key in customers:
            if customers[key]['status']=='Lead':
                del customers[key]
                print("Customer Deleted")
            else:
                print("Cannot delete active customers")
        else:
            print("No such customer")

    elif ch == 6:
        sta = input("Enter Status: ")
        found = False

        for key, s in customers.items():
            if s['status']== sta:
                print(key, s['name'], s['email'], s['status'])
                found = True

        if not found:
            print("No customer with this status")


    elif ch == 7:
        leads = 0
        customers_count = 0
        clients = 0

        for s in customers.values():
            status = s["status"]

            if status == "Lead":
                leads += 1
            elif status == "Customer":
                customers_count += 1
            elif status == "Client":
                clients += 1

        print("Leads:", leads)
        print("Customers:", customers_count)
        print("Clients:", clients)

    elif ch == 8:
        print("Exiting CRM System...")
        break

    else:
        print("Invalid choice!")

   



       

    
    

        
