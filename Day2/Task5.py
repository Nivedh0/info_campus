even=0
odd=0
n=int(input("Enter limit:"))
for i in range(1,n+1):
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)

