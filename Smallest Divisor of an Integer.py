N = int(input("Enter a number: "))
A = []
for i in range(2, N + 1):
    if(N%i==0):
        A.append(i)
A.sort()
print()        
        
