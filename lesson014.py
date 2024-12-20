from multiprocessing.managers import Value


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            #return self.width == other.width and self.height == other.height
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())

print(str(r1))

print(r1.to_string())
print(r1.__repr__())

r2 = Rectangle(10, 20)

print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)
print('='*10)
r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)

print(r1<r2)
print(r2<r1)
print(r2>r1)
print('-'*10)
r1 = Rectangle(10,20)
print(r1.width)
#r1.width = -100
r1.width = 100
print(r1.width)




