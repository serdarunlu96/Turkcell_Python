def old_sum(a,b):
    return a+b

print(old_sum(4,5))

new_sum= lambda a,b : a+b
print(new_sum(4,5))

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
print(sirasiz_liste)

sirali=sorted(sirasiz_liste, key=lambda x: x[1])
print(sirali)