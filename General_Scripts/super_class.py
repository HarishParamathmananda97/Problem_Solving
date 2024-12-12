class Rectangle:
    def __init__(self, *args):
        # Example: Assigning first two arguments as length and width
        self.length = args[0]
        self.width = args[1]

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Cube(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Cubic(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


# Example usage:
rectangle = Rectangle(4, 6)
print("Rectangle dimensions:", rectangle.length, "x", rectangle.width)

square = Square(5)
print("Square dimensions:", square.length, "x", square.width)

cube = Cubic(5)
print("Cube dimension: ", square.length, 'X', square.length, 'X', square.length)
