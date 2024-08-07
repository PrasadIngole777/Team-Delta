# 1) VGroup
# VGroup is a vertical group that arranges its elements vertically. You can use it to group objects that need to be aligned vertically.

from manim import *

class VGroupScene(Scene):
    def construct(self):
        square1 = Square()
        square2 = Square()
        square3 = Square()
        group = VGroup(square1, square2, square3)
        self.add(group)
        self.play(group.scale(2))

# 2) HGroup
# HGroup is a horizontal group that arranges its elements horizontally. You can use it to group objects that need to be aligned horizontally.

from manim import *

class HGroupScene(Scene):
    def construct(self):
        square1 = Square()
        square2 = Square()
        square3 = Square()
        group = HGroup(square1, square2, square3)
        self.add(group)
        self.play(group.scale(2))


# 3) Group
# Group is a generic group that can be used to group objects in any arrangement.

from manim import *

class GroupScene(Scene):
    def construct(self):
        square1 = Square()
        square2 = Square()
        square3 = Square()
        group = Group(square1, square2, square3)
        group.arrange(RIGHT)
        self.add(group)
        self.play(group.scale(2))
