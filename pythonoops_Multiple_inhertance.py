#syntax
#class classB:

# logic

#class classC:


# logic


#class classA(calssB, classC):

# logic


#multiple inheritance


class classB:
    def printdata(self):
        print(10)
class classc:
    def printdata(self):
        print(3)
class ClassA(classB,classc):
    pass
a = ClassA()
a.printdata()

