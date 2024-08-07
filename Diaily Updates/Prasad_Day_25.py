# Custom Animation Techniques and Use of Updaters

# Updater: Updaters are functions that are called repeatedly during an animation to update the animation's state.

from manim import *

class UpdaterExample(Scene):
    def construct(self):
        circle = Circle()

        def update_circle(obj, alpha):
            obj.set_color(interpolate_color(WHITE, RED, alpha))

        self.play(UpdateFromAlphaFunc(circle, update_circle), run_time=2)


# Custom Animation: Custom animations can be created by defining a custom animation class that inherits from Animation.

from manim import *

class CustomAnimation(Animation):
    def __init__(self, obj, **kwargs):
        super().__init__(obj, **kwargs)

    def interpolate_mobject(self, alpha):
        self.mobject.set_color(interpolate_color(WHITE, RED, alpha))

class CustomAnimationExample(Scene):
    def construct(self):
        circle = Circle()

        animation = CustomAnimation(circle)
        self.play(animation, run_time=2)
