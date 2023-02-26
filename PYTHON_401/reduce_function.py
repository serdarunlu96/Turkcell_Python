from functools import reduce

liste = [1,2,3,4]
reduce_function=reduce(lambda a,b: a+b, liste)
print(reduce_function)