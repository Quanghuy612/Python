class GeometricObject:
    def __init__(self, color="green", filled=True):
        self._color = color
        self._filled = filled

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def isFilled(self):
        return self._filled

    def setFilled(self, filled):
        self._filled = filled

    def __str__(self):
        return f"GeometricObject[color={self._color}, filled={self._filled}]"


class Circle(GeometricObject):
    def __init__(self, radius=1.0, color="green", filled=True):
        super().__init__(color, filled)
        self._radius = radius

    def getRadius(self):
        return self._radius

    def setRadius(self, radius):
        self._radius = radius

    def getArea(self):
        return 3.1416 * self._radius * self._radius

    def getPerimeter(self):
        return 2 * 3.1416 * self._radius

    def getDiameter(self):
        return 2 * self._radius

    def printCircle(self):
        print(f"Circle: radius={self._radius}, {self.__str__()}")


class Rectangle(GeometricObject):
    def __init__(self, width=1.0, height=1.0, color="green", filled=True):
        super().__init__(color, filled)
        self._width = width
        self._height = height

    def getWidth(self):
        return self._width

    def setWidth(self, width):
        self._width = width

    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height

    def getArea(self):
        return self._width * self._height

    def getPerimeter(self):
        return 2 * (self._width + self._height)


# Testing the classes
circle = Circle(5, "red", True)
circle.printCircle()
print(f"Area: {circle.getArea()}, Perimeter: {circle.getPerimeter()}, Diameter: {circle.getDiameter()}")

rectangle = Rectangle(4, 6, "blue", False)
print(rectangle)
print(f"Area: {rectangle.getArea()}, Perimeter: {rectangle.getPerimeter()}")
