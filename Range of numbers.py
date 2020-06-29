num1 = int(input("Enter a lower number: "))
num2 = int(input("Enter a upper number2: "))

for i in range(num1, num2+1):
    if(i%7==0 and i%5==0):
        print(i)