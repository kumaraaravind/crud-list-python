#Set data type
#1.implicit
a = {'a', 'b', 'd'}
print(a)

#2.explicit
a = set(('a', 'b', 'e'))
print(type(a))

#3.data type /varabail annotation
a:set = {'a', 'b', 'f'}
print(type(a))

#.*Create
#1.add:
a:set = {'a', 'b', 'c'}
a.add('e')
print(a)

#.*Update
a:set = {'a', 'e', 'f'}
b:set = {'e', 'f', 'd'}
a.update(b)
print(a)

#.*Delete
#1.Remove
a:set = {'a', 'b', 'c'}
a.remove('c')
print(a)

#2.Discard
a:set = {'a', 'b', 'e'}
a.discard('d')
print(a)

#3.pop
a:set = {'a', 'b', 'g'}
a.pop()
print(a)

#Some other methods of set
#Union
a:set = {'x', 'y', 'z'}
b:set = {'y', 'z', 'd'}
print(a.union(b))

#intersection
a:set = {1, 2, 3}
b:set = {1, 2, 4}
print(a.intersection(b))