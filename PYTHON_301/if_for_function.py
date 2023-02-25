salary=[1000,2000,3000,4000,5000]

def maas_ust(x):
    print("Ust maaas: ", x*10/100+x)

def maas_alt(x):
    print("Alt maaas: ", x*20/100+x)

for i in salary:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)