# BAsic Circle Usign Manim

from manim import *

class CircleScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        circle.shift(LEFT * 3)

        self.play(circle.animate.shift(RIGHT * 6), run_time=3)
        self.wait()
