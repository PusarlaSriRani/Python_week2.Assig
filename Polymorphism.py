class Circle:
    def area(self, r):
        return 3.14 * r * r

class Rectangle:
    def area(self, l, b):
        return l * b

circle = Circle()
rectangle = Rectangle()

radius = int(input("Enter radius: "))
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

print("Circle Area:", circle.area(radius))
print("Rectangle Area:", rectangle.area(length, breadth))