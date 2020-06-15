n = int(input("enter a number of elements to be inserted: "))
list =[]
for i in range(0, n):
    number = int(input('Enter a number: '))
    list.append(number)
avg = sum(list)/n
print("avg: ", avg)   
