def eligibility(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"
    
ag=int(input("Enter your Age:"))
print(eligibility(ag))
