list=[1,"a","b",123]
s=set(list)

s.add("ile")
print(s)

s.remove(123)
print(s)

s.discard("c") # delete element into list but not print error message
print(s)