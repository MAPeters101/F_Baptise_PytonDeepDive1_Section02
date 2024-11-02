class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)



r1 = Rectangle(10, 20)
print(r1.width)
r1.width = 100
print(r1.width)
print(r1.height)

r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())

print(str(r1))

print(r1.to_string())






