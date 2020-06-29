print("How many row you want to print?")
row = int(input())
print("Enter 0 or 1")
x = int(input())
new = bool(x)
if new == True:
    for i in range (1,row+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()    
elif new == False:
    for i in range (row,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()                