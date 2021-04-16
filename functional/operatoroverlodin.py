class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return Book(self.pages+other.pages)

    def __sub__(self, other):
        return 'substraction overload'

    def __mul__(self, other):
        return 'multiplicaton overloading'

    def __truediv__(self, other):
        return 'overloading true div'

    def __str__(self):
        return str(self.pages)
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1+b2+b3)

#+ operator can be used with integer type only
# here b1 and b2 rae of type book