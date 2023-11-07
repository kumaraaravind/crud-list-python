# Method OverLoading
#In python methokd overloadding achived by using OPTIONAL PARAMETRS:

class calculation:
    def __add__(self, a: int, b: int):
        print(a+b)
    def __add__(self, a:int, b:int, c:int):
        print(a + b + c)

    def __add__(self, a: int, b: int, c: int = 0):
        print(a+b+c)
    def __name__(self, a: str, b: str):
        print(a + "" +b)

cal = calculation()
cal.__add__(1, 2, 3)
cal.__add__(6, 6, 6)
cal.__name__("Aravind", "Swami")