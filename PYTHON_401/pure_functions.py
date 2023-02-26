# impure pure bagımsız bagımlı fonksiyonlar

A=9 # global variable 

def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b

print(impure_sum(6))
print(pure_sum(3,4))