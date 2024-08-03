#  Creating Simple Shapes


# 1) Circle

from manim import *

class CircleScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.add(circle)
        self.wait()


# 2) Square

from manim import *

class SquareScene(Scene):
    def construct(self):
        square = Square(side_length=2, color=RED)
        self.add(square)
        self.wait()

# 3) Rectangle

from manim import *

class RectangleScene(Scene):
    def construct(self):
        rectangle = Rectangle(width=3, height=2, color=GREEN)
        self.add(rectangle)
        self.wait()
      
# 4) Triangle

from manim import *

class TriangleScene(Scene):
    def construct(self):
        triangle = Triangle(color=YELLOW)
        self.add(triangle)
        self.wait()
