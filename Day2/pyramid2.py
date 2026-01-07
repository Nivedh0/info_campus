# n=5
# for i in range(1,n+1):
#     print('A'*i)

n=5
for i in range(n):
    for j in range(i+1):
        print('A',end=' ')
    print()