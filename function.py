from functools import reduce

# def add(n):
#     return n+10
# print(add(5))



# g = lambda x: x * x * x
# print(g(5))

# lambda with filter
l1 = [4,2,5,10,45,78,56,70,75,105,1015,45,78,110]
finale_list=list(filter(lambda x: (x%5==0),l1))
print(finale_list)

# lambda wirth map
finale_list2 = list(map(lambda x: (x+x),l1))
print(finale_list2)

# lambda with reduce
l2 = [1,2,3,4,5,6,7,8,9,10]
finale_list3 = reduce(lambda x,y: x+y,l2)
print(finale_list3)