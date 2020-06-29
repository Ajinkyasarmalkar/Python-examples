# string = input("Enter a name: ")
# length = len(string)
# for row in range(length):
#     for col in range(row+1):
#         print(string[col], end="")
#     print(" ")    

print()

number = int(input("Enter a number: "))
for row in range(1, number+1):
    for col in range(1, number-row+1):
        print(end=" ")
    for col in range(row, 0, -1):
        print(col, end="")   
    for col in range(2, row+1):
        print(col, end="")    
    print("")    
