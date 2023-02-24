list=["ali","veli","berkcan","ayse"]
print(list)

list[1]="velinin_babasi"
print(list)

list[1]="veli"
list[0:3]="alinin_babasi","velinin_babasi","berkcanin_babasi"
print(list)

list=["ali","veli","berkcan","ayse"]
list=list+["kemal"]
print(list)

del list[2]
print(list)