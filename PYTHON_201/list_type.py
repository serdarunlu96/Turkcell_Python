notes=[90,80,70,50]
print(type(notes))

list=["a",19.3,90] # different types datas , ordered , changable 
list_large=["a",19.3,90,list]
print(type(list_large[0]))
print(type(list_large[3]))

all_list=[list,list_large] # concat 2 list all in one list
print(all_list)

# del all_list