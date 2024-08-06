from manim import *

class AnimationScene(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # Break down complex animation into smaller parts
        self.play(Create(square))
        self.wait(1)
        self.play(square.scale(2))
        self.wait(1)
        self.play(square.rotate(PI/2))
        self.wait(1)

        # Use transition states
        self.play(square.set_opacity(0.5))
        self.wait(1)
        self.play(square.set_opacity(1))

        # Utilize animation methods
        self.play(FadeOut(square))
        self.wait(1)
        self.play(FadeIn(square))
