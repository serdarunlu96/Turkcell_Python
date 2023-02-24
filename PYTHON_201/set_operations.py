set1=set([1,3,5])
set2=set([1,2,3])

print(set1.difference(set2)) # set1 have, set2 not
print(set2.difference(set1)) # set2 have, set1 not

print(set1.symmetric_difference(set2)) # return two sets not having each other

print(set1-set2) # - and difference same thing

print(set1.intersection(set2)) # intersection
print(set1&set2) # & and intersection same thing

birlesim= set1.union(set2) #set1 and set2 union elements one birlesim set
print(birlesim)

set1.intersection_update(set2) # set1 and set2 intersection defined into set1
print(set1)
print(set1.intersection(set2)) # intersection