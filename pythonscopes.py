#Global scope or publicscope

class Employee:
    firstName: str = "Aravind"
    lastName: str = "swami"

emp = Employee()
print(emp.firstName)


#partially private or protected

class Employee:
    _firstName: str = "swami"
    _lastName: str = "Aravind"
emp = Employee()

print(emp._firstName)

#Strictly private

class Employee:
    __firstName: str = "swami"
    __lastName: str = "Aravind"
emp = Employee()

print(emp.__firstName)

