salary=[8000,5000,2000,1000,3000,7000,1000]

# dir(salary)

# print(salary.sort())

for i in salary:
    if i == 3000:
        print("Kesildi")
        break # find 3000 and stop the printing loop without 3000
    print(i)

print()

for i in salary:
    if i == 3000:
        continue # find 3000 and continue the printing loop skip 3000
    print(i)