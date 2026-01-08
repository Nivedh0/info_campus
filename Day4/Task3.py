# Task 3: Customer Phone Directory

# Store customer names and phone numbers in a dictionary.
# Allow searching a phone number by customer name.

cust={
    "rohan": "98756747388",
    "shahidh": "7689453678",
    "sulafa": "6543218769"
}

n=input("Enter Name of the customer:")
if n in cust:
        print("Phone Number:",cust[n])
else:
        print("No such customer")
