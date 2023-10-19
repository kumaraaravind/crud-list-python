#union
#syntax:variable.union(variable)

a = {10, 22, 30, 40}
b = {55, 22, 70, 88}
print(a.union(b))

#intersection
#Syntax:variable.intersection(variable)
a = {15, 25, 39, 45}
b = {50, 25, 75, 80}
print(a.intersection(b))

#intersection update
#Syntax:set1.intersection.update(set2)
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)

a = {'a'}
b = {'d'}
print(a.isdisjoint(b))

a = {'a'}
b = {'a'}
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)
a = {'Navya', 'Rajesh', 'Mahalya', 'Aravind'}
b = {'Navya', 'Aravind'}
print(a.difference(b))

#symmetric
#syntax:set1.symmetric difference(set2)

a = {'Aravind', 'Rajesh', 'ravi', 'kumar'}
b = {'Rajesh', 'ravi'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)
a = {'Navya', 'rajesh', 'Mahalya', 'Aravind'}
b = {'Aravind', 'Mahalya'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)

a = {'Navya','Rajesh','Mahalya','Aravind'}
b = {'Rajesh','Mahalya'}
print(a.issubset(b))

a = {'Navya','Rajesh','Mahalya','Aravind'}
b = {'Rajesh','Mahalya','Navya','Aravind'}
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)
a = {'praveen','sai','kumar','Aravind'}
b = {'praveen'}
print(a.issuperset(b))