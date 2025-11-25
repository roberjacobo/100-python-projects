class Point:
    """Represents a point in 2D space with x and y coordinates."""

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def show_point(self) -> None:
        """Prints the current value of X and Y"""

        print(f"The point is {self.X}, {self.Y}")


p1 = Point(4, 6)
p1.X = 6
p1.show_point()

p2 = Point(2, 2)
p2.show_point()

p3 = Point(6, 1)
p3.show_point()

p4 = Point(9, 2)
p4.show_point()

p1 = p4
p1.show_point()
