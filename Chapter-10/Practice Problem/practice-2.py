class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num**2}")

    def squareRoot(self):
        print(f"The square root of {self.num} is {self.num**0.5}")

    def cube(self):
       print(f"The cube of {self.num} is {self.num**3}")


x = Calculator(9)
x.square()
x.squareRoot()
x.cube()