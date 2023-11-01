#example for abstraction

class Employee:
    
    __firstName: str = "Aravind"
    __lastName: str = "Swami"

 def fullName(self):
        return self.__firstName+" "+self.__lastName
     
emp = Employee()
emp.firstName = "cda"

print(emp.fullName())
