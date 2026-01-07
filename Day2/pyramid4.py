# n = 5

# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + j), end="")
#     print()

    
# for i in range(5):
#     print("ABCDE"[:i+1])

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p+j),end=' ')
    print()
