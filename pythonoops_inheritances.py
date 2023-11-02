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
        return f'{self._firstName} {self._lastName} {self._sunName}'

    def getFullName(self):
        return self._nameFormat()

emp = Employee()
emp.setName(fName="Aravind", sName="P", lName="swami")
emp.addAddress("Guntur")
print(emp.getFullName())
print(emp.addAddress())
