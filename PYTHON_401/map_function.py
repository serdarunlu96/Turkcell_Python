liste = [1,2,3,4,5]

for i in liste:
    print(i+10)

map_function=list(map(lambda x: x*10, liste))
print(map_function)
