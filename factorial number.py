def factorial_iteratative(n):
    fac = 1 
    for i in range(n):
        fac = fac * (i+1)
    return fac   

fac1 = int(input("Enter a Number: "))

print(factorial_iteratative(fac1))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)    
fac2 = int(input("Enter a Number: "))

print(factorial_recursive(fac2))

