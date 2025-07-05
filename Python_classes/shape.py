import math

class Shape:
    def __init__(self):
        pass
    
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def calculate(self, type_of_calculation):
        if type_of_calculation == "area":
            return self.calculate_area()
        elif "perimeter":
            return self.calculate_perimeter()
        else:
            return "Неизвестный тип вычислений"
            
class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width
    
    def calculate_perimeter(self):
        return 2 * (self._length + self._width)
    
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
    
    def calculate_area(self):
        return math.pi * self._radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self._radius
    
rectangle = Rectangle(10, 5)
rectangle_area = rectangle.calculate("area")
rectangle_perimeter = rectangle.calculate("perimeter")

circle = Circle(10)
circle_area = circle.calculate("area")
circle_perimeter = circle.calculate("perimeter")

print(f"Прямойгольник - площадь: {rectangle_area}, периметр: {rectangle_perimeter}")
print(f"Окружность - площадь: {circle_area}, периметр: {circle_perimeter}")