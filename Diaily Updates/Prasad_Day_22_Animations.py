# Creating Simple Animations


# 1) Fade In

from manim import *

class FadeInScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.play(FadeIn(circle))
        self.wait()

# 2) Fade Out

from manim import *

class FadeOutScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.add(circle)
        self.play(FadeOut(circle))
        self.wait()

# 3) Shift

from manim import *

class ShiftScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.add(circle)
        self.play(circle.animate.shift(RIGHT * 3))
        self.wait()

# 4) Scale

from manim import *

class ScaleScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.add(circle)
        self.play(circle.animate.scale(2))
        self.wait()

# 5) Rotate

from manim import *

class RotateScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.add(circle)
        self.play(circle.animate.rotate(PI / 2))
        self.wait()
