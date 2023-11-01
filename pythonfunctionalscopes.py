


#functinoal Scope or local scope
def fullName():
    global fName
    fName = "swami"
    lName = "Aravind"
fullName()
print(fName)
print(lName)


#global varable

def fullName():
    global fName
    fName = "Aravind"
    lName = "swami"
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
            c=10
            lst.append(b)
            a=a+b
            b=a-b
            i+=1
        print(lst)
fib=fibseries()
fib.fibex()


