#syntax
#class classA:

# logic

#class classB(calssA):


# logic


#class classC(calssA):

# logic

class Address:
    _address: str = ""
    def addAddress(self, address):
        self._address = address
    def getAddress(self):

        return self._address

class Employee(Address):
    _firstName: str = ""
    _lastName: str = ""
    _sunName: str = ""
    def setName(self, fName: str, lName: str, sName: str = ""):
        self._firstName = fName
        self._sunName = sName
        self._lastName = lName

    def _nameFormat(self):
        return f'{self._sunName} {self._firstName} {self._lastName}'

    def getFullName(self):
        return self._nameFormat()

class perminentEmployee(Employee):
    _sal : int = 30000
    def salcal(self) -> str:
         return f'sal cal per year: {12 * self._sal}'

class contactEmployee(Employee):
       _hr_pay:int = 500
       def salcal(self, hrs: int) -> str:
           return f'sal cal for {hrs} hrs: {self._hr_pay * hrs}'
pemp =perminentEmployee()
pemp.setName(fName="Aravind", sName="P", lName="swami")
pemp.addAddress("Guntur")
print(pemp.getFullName())
print(pemp.getAddress())
print(pemp.salcal())


cemp = contactEmployee()
cemp.setName(fName="praveen", sName="k", lName="pavan")
cemp.addAddress("Guntur")
print(cemp.getFullName())
print(cemp.getAddress())
print(cemp.salcal(20))

