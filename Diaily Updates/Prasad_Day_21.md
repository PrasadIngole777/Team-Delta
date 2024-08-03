# MAMIM introduction : 

Installation and Configuration of Manim Engine : 

  * To install Manim, you'll need to have Python 3.7 or later installed
  
  * Try this commmand
      
        pip install manim

  * Once installed, you can verify the installation by running:

        manim --help

  Structural Overview of a Manim Script :

        from manim import *

        class MyScene(Scene):
          def construct(self):
            # Your code here
            pass

  * from manim import * : Imports the Manim library.
  * class MyScene(Scene) : Defines a new scene class that inherits from Manim's Scene class.
  * def construct(self) : Defines the construct method, which is where you'll write your animation code.

You can render this scene by running :

    manim -p -ql ClassName
