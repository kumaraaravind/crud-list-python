#String Transform Functions
#capitalize
#Syntax:variable.capitalize()
name = "Aravind"
print(name.capitalize())

#Title
#syntax:variable.title()
name ="Aravind"
print(name.title())

#upper
#syntax:variable.upper()
name = "Aravind"
print(name.upper())

#lower
#syntax:variable.lower()
name = "Aravind"
print(name.lower())

#casefold
#syntax:variable.casefold()
name = "KUMAR"
print(name.casefold())

#swapcase
#syntax:variable.swapcase()
name = "Aravind"
print(name.swapcase())


#String Check Functions
#isnumeric
#syntax:variable.isnumeric()
number = "1245"
print(number.isnumeric())

#isalphanumeric
#syntax:variable.ialnum()
num = "Swami12345"
print(num.isalnum())

#isdecimal
#syntax:variable.isdecimal()
number = "Aravind"
print(number.isdecimal())

#isdigit
#syntax:variable.isdigit()
num = "123456"
print(num.isdigit())

#isascii
#syntax:variable.isascii()
num = "abc"
print(num.isascii())

#isupper
#syntax:variable.isupper()
num = "Aravind"
print(num.isupper())

#islower
#syntax:variable.islower()
num = "Aravind"
print(num.islower())

#isspace
#syntax:variable.isspace()
num = " "
print(num.isspace())

#isidentifier
#syntax:variable.isidentifier()
num = "@"
print(num.isidentifier())

#isprintable
#syntax:variable.isprintable()
num = "Aravind"
print(num.isprintable())

#istitle
#syntax:variable.istitle()
num = "Aravind"
print(num.istitle())


#String Search Functions
#index
#syntax:variableName.index(string/char)
email = "aravind@gmail.com"
print(email.index("@"))

#rindex
#syntax:variableName.rindex(string/char)
email = "aravind@gmail@.com"
print(email.rindex("@"))

#rfind
#syntax:variableName.rfind(string/char)
email = "aravind@gmail@.com"
print(email.rindex("@"))

#startswith
#syntax:variableName.startswith(string/char)
name = "Aravind"
print(name.startswith("Aravind"))

#endswith
#syntax:variableName.endswith(string/char)
name = "Aravind"
print(name.endswith("Aravind"))


#list methods
#Append
#syntax:lst.append()
l = []
print(l.append("Aravind"))
print(l)

#insert
#syntax:lst.insert(index,item)
l = ["Aravind", "kumar"]
print(l.insert(1,"swami"))
print(l)
#Extend
#syntax:lst.extend(lst1)
name = ["Aravind", "kumar"]
name1 = ["swami ", "pavan"]
name.extend(name1)
print(name)

#count
#syntax:lst.count(item)
name = ["Aravind", "praveen"]
print(name.count("Aravind"))

#index
#syntax:lst.index(item)
name = ["Aravind", "kumar"]
print(name.count("Aravind"))

#pop
#syntax:lst.pop()
name = ["Aravind", "kumar"]
print(name.pop())

#remove
#syntax:lst.remove()
name = ["Aravind", "kumar"]
print(name.remove("kumar"))
print(name)

#clear
#syntax:lst.clear(item)
name = ["Aravind", "praveen", "raju"]
print(name.clear())
print(name)

#sort
#syntax:lst.sort()
a = [1, 2, 8, 7, 5, 10]
a.sort()
print(a)

#reverse
#syntax:lst.reverse()
a = [1, 2, ]
a.reverse()
print(a)


#Tuple Methods
#count
#syntax:tpl.count(item)
tpl = tuple((1, 6, 3, 5, 6))
print(tpl.count(4))

#index
#syntax:tpl.index(item)
tpl = tuple((1, 2, 3,))
print(tpl.index(2))

#set methods
#add
#syntax:variable.add()
a = {'a', 'b', 'c'}
a.add('d')
print(a)

#update
#syntax:variable.update(setvariable)
a = {'a', 'b', 'c'}
b = {'b','c','d'}
a.update(b)
print(a)

#remove
#syntax:variableName.remove(item)
a = {'a', 'b', 'c', 'd'}
a.remove('b')
print(a)

#discard
#syntax:variableName.discard(item)
a = {'a', 'b', 'c'}
a.discard('c')
print(a)

#pop
#syntax:variableName.pop()
a = {'a', 'b', 'c', 'd'}
a.pop()
print(a)

#frozenset methods
#union function
#syntax:variableName.union(variable)
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.intersection(b))

#intersection update
#yntax:set1.intersection_update
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)
a = {'a'}
b = {'b'}
print(a.isdisjoint(b))
#difference
#syntax:set1.difference(set2)
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)

a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)

a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.issuperset(b))
