
#parameter less:
def add():
    a = 10
    b = 20
    print(a + b)
add()
def sub():
    a = 10
    b = 20
    print(a - b)
sub()

#parameterized function:
def add(literal1: int, literal2: int):
    print(literal1 + literal2)
add(10, 20)

def sub(literal1: int, literal2: int):
    print(literal1 - literal2)
add(10, 20)
a = 10
b = 20
sub(literal1=a, literal2=b)
sub(literal2=b, literal1=a)

#String Transform Functions-capitalize
#Syntax:variable.capitalize()
def capitalize():
    a = "aravind"
    print(a.capitalize())
capitalize()

#Title
#syntax:variable.title()
def title():
    a = "aravind"
    print(a.title())
title()

#upper
#syntax:variable.upper()
def upper():
    a ="aravind"
    print(a.upper())
upper()

#lower
#syntax:variable.lower()
def lower():
    a = "PRAVEEN"
    print(a.lower())
lower()

#casefold
#syntax:variable.casefold()
def casefold():
    a = "SUESH"
    print(a.casefold())
casefold()

#swapcase
#syn tax:variable.swapcase()
def swapcase():
    a = "AraVind"
    print(a.swapcase())
swapcase()

#String Check Functions
#isnumeric
#syntax:variable.isnumeric()
def isnumeric():
    a = "234"
    print(a.isnumeric())
isnumeric()

#isalphanumeric
#syntax:variable.ialnum()
def isalnum():
    a = "Aravind143"
    print(a.isalnum())
isalnum()

#isdecimal
#syntax:variable.isdecimal()
def isdecimal():
    a ="520520"
    print(a.isdecimal())
isdecimal()

#isdigit
#syntax:variable.isdigit()
def isdigit():
    a = "Aravind"
    print(a.isdigit())
isdigit()

#isascii
#syntax:variable.isascii()
def isascii():
    a = "aravind"
    print(a.isascii())
isascii()

#isupper
#syntax:variable.isupper()
def isupper():
    a = "aravind"
    print(a.isupper())
isupper()

#islower
#syntax:variable.islower()
def islower():
    a = "ARAVIND"
    print(a.islower())
islower()

#isspace
#syntax:variable.isspace()
def isspace():
    a =" "
    print(a.isspace())
isspace()

#isidentifier
#syntax:variable.isidentifier()
def isidentifier():
    a ="1234@"
    print(a.isidentifier())
isidentifier()

#isprintable
#syntax:variable.isprintable()
def isprintable():
    a = "Aravind"
    print(a.isprintable())
isprintable()

#istitle
#syntax:variable.istitle()
def istitle():
    a = "Aravind"
    print(a.istitle())
istitle()

#String Search Functions
#index
#syntax:variableName.index(string/char)
def index():
    email = "aravind@gmail.com"
    print(email.index("@"))
index()

#rindex
#syntax:variableName.rindex(string/char)
def rindex():
    email = "aravind@gmail.com"
    print(email.rindex("@"))
rindex()

#rfind
#syntax:variableName.rfind(string/char)
def rfind():
    email = "aravind@gmail.com"
    print(email.rindex("@"))
rfind()

#startswith
#syntax:variableName.startswith(string/char)
def startswidth():
    email = "aravind@gmail.com"
    print(email.startswith("navya"))
startswidth()

#endswith
#syntax:variableName.endswith(string/char)
def endswith():
    email = "aravind@gmail.com"
    print(email.endswith(".com"))
endswith()

#list methods
#Append
#syntax:lst.append()
def append():
    lst=[]
    print(lst.append("aravind"))
    print(lst)
append()

#insert
#syntax:lst.insert(index,item)
def insert():
    lst = ["kumar","swami"]
    print(lst.insert(1,"aravind"))
    print(lst)
insert()

#Extend
#syntax:lst.extend(lst1)
def extend():
    name = ["sai","vinod","raju"]
    name1 = ["surendra","abral"]
    name.extend(name1)
    print(name)
extend()

#count
#syntax:lst.count(item)
def count():
    name=["praveen","sai","ravi","raju"]
    print(name.count("aravind"))
count()

#pop with index
#syntax:lst.pop(index)
def pop():
    name=["aravind","raju","sai"]
    name.pop(1)
    print(name)
pop()

#pop without index
#syntax:lst.pop()
def pop():
    attendees=["sai","raju","pavan"]
    attendees.pop()
    print(attendees)
pop()

#remove
#syntax:lst.remove()
def remove():
    a=["sai","mahesh","kumar"]
    print(a.remove("sai"))
    print(a)
remove()

#clear
#syntax:lst.clear()
def clear():
    a=["raju","praveen","kumar"]
    print(a.clear())
    print(a)
clear()

#sort
#syntax:lst.sort()
def sort():
    a=[1,2, 4,5]
    a.sort()
    print(a)
sort()

#reverse
#syntax:lst.reverse()
def reverse():
    a=[1,2, 3,5]
    a.reverse()
    print(a)
reverse()

#Tuple Methods
#count
#syntax:tpl.count(item)
def count():
    tpl=tuple(("sai","prakesh","sai"))
    print(tpl.count("sai"))
count()

#index
#syntax:tpl.index(item)
def index():
    tpl=tuple((1,2,3,4,5))
    print(tpl.index(3))
index()

#set methods
#add
#syntax:variable.add()
def add():
    a={'a','b','c'}
    a.add('d')
    print(a)
add()

#update
#syntax:variable.update(setvariable)
def update():
    a={'a','b','c'}
    b={'b','c','d'}
    a.update(b)
    print(a)
update()

#remove
#syntax:variableName.remove(item)
def remove():
    a={'a','b','c'}
    a.remove('b')
    print(a)
remove()

#discard
#syntax:variableName.discard(item)
def discard():
    a={'a','b','c'}
    a.discard('c')
    print(a)
discard()

def discard():
    a={'a','b','c'}
    a.discard('d')
    print(a)
discard()

#pop
#syntax:variableName.pop()
def pop():
    a={'a','b','c'}
    a.pop()
    print(a)
pop()

#other methods of sets
#union
#syntax:variableName.union(variable)
def union():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.union(b))
union()

#intersection
#syntax:variableName.intersection(variable)
def intersection():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.intersection(b))
intersection()

#intersection update
#syntax:set1.intersection_update(set2)
def intersection_update():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.intersection_update(b))
    print(a)
    print(b)
intersection_update()

#isdisjoint
#syntax:set1.isdisjoint(set2)
def isdisjoint():
    a={'a'}
    b={'b'}
    print(a.isdisjoint(b))
isdisjoint()

#difference
#syntax:set1.difference(set2)
def difference():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.difference(b))
difference()

#symmetric difference
#syntax:set1.symmetric difference(set2)
def symmetric_difference():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.symmetric_difference(b))
symmetric_difference()

#symmetric difference update
#syntax:set1.symmetric difference update(set2)
def symmetric_difference_update():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.symmetric_difference_update(b))
    print(a)
    print(b)
symmetric_difference_update()

#issubset
#syntax:set1.issubset(set2)
def issubset():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.issubset(b))
issubset()

#issuperset
#syntax:set1.issuperset(set2)
def issuperset():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.issuperset(b))
issuperset()

#frozenset-union
#syntax:variableName.union(variable)
def union():
    a=frozenset(["aravind","sai"])
    b=frozenset(["aravind","sai","kumar"])
    print(a.union(b))
union()

#intersection
#syntax:variableName.intersection(variable)
def intersection():
    a=frozenset(["sai","ravi","kumar"])
    b=frozenset(["sai","ravi","kumar"])
    print(a.intersection(b))
intersection()

#isdisjoint
#syntax:set1.isdisjoint(set2)
def isdisjoint():
    a=frozenset(["lg","sony","tcl"])
    b=frozenset(["sony","tcl","samsung"])
    print(a.isdisjoint(b))
isdisjoint()

def isdisjoint():
    a=frozenset(["sai"])
    b=frozenset(["naveen"])
    print(a.isdisjoint(b))
isdisjoint()

#issubset
#syntax:set1.issubset(set2)
def issubset():
    a=frozenset(["sai","ravi","pavan"])
    b=frozenset(["sai","ravi","pavan"])
    print(a.issubset(b))
issubset()

def issubset():
    a=frozenset(["Mahesh"])
    b=frozenset(["sai","Mahesh","pavan"])
    print(a.issubset(b))
issubset()

#issuperset
#syntax:set1.issuperset(set2)
def issuperset():
    a=frozenset(["sai","mahesh","pavan"])
    b=frozenset(["sai","mahesh","pavan"])
    print(a.issuperset(b))
issuperset()

def issuperset():
    a=frozenset(["sai","mahesh","pavan"])
    b=frozenset(["sai"])
    print(a.issuperset(b))
issuperset()

#diffrence
#syntax:set1.difference(set2)
def difference():
    a=frozenset(["sai","mahesh","pavan"])
    b=frozenset(["sai","mahesh","pavan"])
    print(a.difference(b))
    print(b.difference(a))
difference()

#symmetric_difference
#syntax:set1.symmetric difference(set2)

def symmetric_difference():
    a=frozenset(["sai","mahesh","pavan"])
    b=frozenset(["sai","mahesh","pavan"])
    print(a.symmetric_difference(b))
symmetric_difference()

