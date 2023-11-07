#Method overriding

class Employee:
    __amt = 25000
    def sal(self):
        return self.__amt*12

class contractEmployee(Employee):
    __hrpay = 1000
    __hrs = 10
    def sal(self):
        return self.__hrpay*self.__hrs
emp1=contractEmployee()
print(emp1.sal())

emp=Employee()
print(emp.sal())

