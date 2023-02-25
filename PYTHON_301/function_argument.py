def kare_al(x): # function
    print(x**2)

def carpma_yap(x,y): # 2 argument function
    print(x*y)

carpma_yap(2,3)

def carpma_yap(x,y = 1): # Pre defined argument function ( ön tanımlı argüman )
    print(x*y)

carpma_yap(2)
carpma_yap(y=2,x=3)