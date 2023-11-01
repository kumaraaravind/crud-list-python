



#global variable

def fullName():
    global fName
    lName="sena"
    fName="Sudheer"
fullName()
print(fName)
print(lName)

#functional scope

def fullName():
    global fName
    lName="sena"
    fName="Sudheer"
fullName()
print(fName)
print(lName)


#block scope

class fibseries:
    def fibex(selfself):
        n=10
        a=1
        b=0
        i=1
        lst=[]
        while i<=n:
            c=10     #block scope
            lst.append(b)
            a=a+b
            b=a-b
            i+=1
        print(lst)
fib=fibseries()
fib.fibex()
