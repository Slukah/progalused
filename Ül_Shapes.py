"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.__color = color
        pass

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.__color = color
        pass

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.__color
        pass

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.__radius = radius
        pass

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.__radius}, color: {self.get_color()})"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * self.__radius * self.__radius
        pass


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.__side = side
        pass

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.__side}, color: {self.get_color()})"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.__side * self.__side
        pass


#class Rectangle(Shape):


   class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        pass

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        pass

    def get_shapes(self) -> list:
        """Return all the shapes."""
        pass

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        pass

    def get_circles(self) -> list:
        """Return only circles."""
        pass

    def get_squares(self) -> list:
        """Return only squares."""
        pass

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        pass


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    print(circle)
    print(circle.get_area())
    square = Square("red", 11)
    print(square)
    print(square.get_area())
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
