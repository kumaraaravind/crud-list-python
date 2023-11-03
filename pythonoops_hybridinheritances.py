
#syntax
#class classA:

# logic

#classclassB (classA):


# logic

#class classC(classA)

#class classD(calssB, classC):

# logic




# hydrid inheritances
class ClassA:
    def printdata(self):
        print("10")
class ClassB(ClassA):
     def printdata(self):
        print("20")
class ClassC(ClassA):
    def printdata(self):
        print("40")
class ClassD(ClassB,ClassC):
    pass
a = ClassD()
a.printdata()

