### Week 4: Introduction to Manim Animation Engine

#### Day 21: Getting Started with Manim

Manim (Mathematical Animation Engine) is a powerful library used for creating precise and 
high-quality mathematical animations.It is widely used in educational content to explain concepts visually. 
This guide will provide a comprehensive introduction, starting from installation to crafting basic scenes and animations.

---

### 1. **Installation and Configuration of the Manim Engine**

**1.1. Overview of Manim Versions**
- **Manim Community**: The community-maintained version of Manim, actively developed and
                      supported by a wide range of contributors. It offers more features and
                        better documentation compared to the original version.
- **ManimGL**: The original version of Manim created by 3Blue1Brown (Grant Sanderson).
                        It uses OpenGL for rendering and is optimized for high-quality animations.

In this guide, we'll focus on the Manim Community version due to its extensive features and active development.

**1.2. Prerequisites**
- **Python**: Ensure Python 3.7 or later is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **FFmpeg**: Required for rendering videos. You can download it from [ffmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

**1.3. Installation Steps**
- **Windows**:
  1. Install Python and FFmpeg.
  2. Install Manim Community via pip:
     ```sh
     pip install manim
     ```

- **macOS**:
  1. Use Homebrew to install FFmpeg:
     ```sh
     brew install ffmpeg
     ```
  2. Install Manim Community:
     ```sh
     pip install manim
     ```

- **Linux**:
  1. Use your package manager to install FFmpeg. For example, on Ubuntu:
     ```sh
     sudo apt update
     sudo apt install ffmpeg
     ```
  2. Install Manim Community:
     ```sh
     pip install manim
     ```

**1.4. Verifying the Installation**
- To verify the installation, run the following command:
  ```sh
  manim -v
  ```
  This should display the version of Manim installed and confirm that it's set up correctly.

**1.5. Basic Configuration**
- **Manim Config File**: Manim uses a configuration file (`manim.cfg`) to store rendering settings such as resolution and output directories.
                       This file can be customized according to your preferences.
- **Default Configuration Settings**:
  ```sh
  [CLI]
  frame_rate = 30
  pixel_height = 1080
  pixel_width = 1920
  output_file = output.mp4
  ```

### 2. **Structural Overview of a Manim Script**

A Manim script is a Python script that defines animations using Manim's API. It typically consists of the following components:

**2.1. Import Statements**
- Begin with importing necessary modules from Manim:
  ```python
  from manim import *
  ```

**2.2. Scene Class**
- The core of a Manim script is a class that inherits from `Scene` or its variants. This class defines the animations and scenes.

**2.3. Construct Method**
- The `construct` method is where the main logic of the scene resides. It contains the sequence of animations and visual elements to be rendered.

**2.4. Basic Structure of a Manim Script**
- Example:
  ```python
  from manim import *

  class MyFirstScene(Scene):
      def construct(self):
          circle = Circle()  # Create a circle
          self.play(Create(circle))  # Animate the creation of the circle
          self.wait(2)  # Pause for 2 seconds
  ```

### 3. **Crafting Basic Scenes and Animations**

**3.1. Creating Basic Shapes**
- **Circles, Squares, Triangles**:
  ```python
  circle = Circle()
  square = Square()
  triangle = Triangle()
  ```

**3.2. Adding Shapes to the Scene**
- Use the `add` method to add shapes to the scene:
  ```python
  self.add(circle)
  ```

**3.3. Animating Shapes**
- **Basic Animations**:
  - **Creating**: `Create(circle)`
  - **Moving**: `circle.animate.shift(UP)`
  - **Rotating**: `Rotate(circle, angle=PI/4)`

- **Example**:
  ```python
  from manim import *

  class MyFirstAnimation(Scene):
      def construct(self):
          circle = Circle()  # Create a circle
          self.play(Create(circle))  # Animate the creation
          self.play(circle.animate.shift(UP))  # Move the circle up
          self.play(Rotate(circle, angle=PI/4))  # Rotate the circle
          self.wait(2)  # Pause for 2 seconds
  ```

**3.4. Running a Manim Script**
- To render the animation, navigate to the script's directory in the terminal and use the following command:
  ```sh
  manim -pql my_script.py MyFirstAnimation
  ```
  - `-p`: Automatically play the video after rendering.
  - `-ql`: Render at a lower quality (quick).

 
