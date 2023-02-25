x=10 # global variable
y=20 # global variable

def carpma_yap(x = 2,y = 1): # x and y local variables
    return x*y

cikti = carpma_yap(2,3)
print(cikti)