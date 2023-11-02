
class Employee:
    __firstName: str = "Aravind"
    __lastName: str = "swami"
    def fullName(self):
        return self.__nameFormat(self.__firstName, self.__lastName)

    def __nameFormat(self, fName: str, lName: str, ):
        return f" = {fName} {lName} "
emp = Employee()
emp.__firstName = "Abc"
print(emp.fullName())
print(emp.__nameFormat('Aravind', 'swami'))
