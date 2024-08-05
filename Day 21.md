### Install Manim
You can install Manim from PyPI using pip. Run the following command:
```
pip install manim
```
Then, in the terminal or command prompt, navigate to the directory containing filename and run:
```
manim -pql ClassName
```
### Basic Structure of a Manim Script
1.Importing Manim
```
from manim import *
```
2.Defining a Scene
```py
class MyScene(Scene):
    def construct(self):
        # Define your mobjects and animations here
        pass
```
Creating and Displaying Text:
```py
from manim import *

class HelloWorld(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hello, Manim!")
        
        # Display the text on the screen
        self.play(Write(text))
        self.wait(2)  # Wait for 2 seconds
```
