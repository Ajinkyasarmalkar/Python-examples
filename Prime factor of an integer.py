n = int(input("Enter an integer:"))
f = 0
for i in range(2, n+1):
    if n%i==0:
        for j in range(2, int(i/2)):
            if i%j ==0:
                f = 1
                break
        if f == 0:
            print(i)    
