import math
lst = []
for i in range(0, 4):
    list_item = int(input("Enter a number: "))
    lst.append(list_item)
x = int(input("Enter a Value of x: "))
sum1=0
j=3
for i in range(0,3):
    while(j>0):
        sum1=sum1+(lst[i]*math.pow(x,j))
        break
    j=j-1
sum1=sum1+lst[3]
print("The value of the polynomial is:",sum1)    

