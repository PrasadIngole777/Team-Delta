
#### Day 27: Advanced Animation Techniques - 3D Animations and Camera Controls

 
### **2. Exploration of 3D Animations and Scene Management**

Manim supports 3D animations, allowing for the creation of scenes with depth and perspective.

**2.1. Creating 3D Objects**
- **Basic 3D Shapes**:
  - Manim provides several 3D shapes like `Sphere`, `Cube`, `Cone`, etc.

  - **Example**:
    ```python
    class Basic3DShapes(ThreeDScene):
        def construct(self):
            sphere = Sphere()
            cube = Cube()
            cone = Cone()

            self.add(sphere, cube, cone)
            self.play(Create(sphere), Create(cube), Create(cone))
            self.wait(2)
    ```

**2.2. 3D Axes and Graphs**
- **3D Axes**:
  - Use `ThreeDAxes` to create a 3D coordinate system.

  - **Example**:
    ```python
    class ThreeDAxesExample(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            self.add(axes)

            # Function graph
            graph = ParametricFunction(
                lambda t: np.array([t, np.sin(t), np.cos(t)]),
                t_range=[-2 * np.pi, 2 * np.pi],
                color=BLUE,
            )

            self.add(graph)
            self.play(Create(graph))
            self.wait(2)
    ```

**2.3. Animating 3D Objects**
- **Rotation and Transformation**:
  - Use `Rotate`, `Scale`, and `MoveToTarget` to animate transformations.

  - **Example**:
    ```python
    class Rotate3DObject(ThreeDScene):
        def construct(self):
            cube = Cube()
            self.add(cube)
            self.play(Rotate(cube, axis=RIGHT, angle=PI/4))
            self.wait(2)
    ```

### **3. Use of Camera Controls and Varying Perspectives in Animations**

Manim allows you to control the camera to create dynamic perspectives and views.

**3.1. Basic Camera Movements**
- **Rotation**: Rotate the camera around the scene.
- **Panning**: Move the camera along the x, y, or z-axis.
- **Zooming**: Zoom in or out.

- **Example**:
  ```python
  class CameraMovementExample(ThreeDScene):
      def construct(self):
          axes = ThreeDAxes()
          self.add(axes)

          # Rotate the camera
          self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES)
          self.begin_ambient_camera_rotation(rate=0.1)  # Start rotating
          self.wait(2)
          self.stop_ambient_camera_rotation()  # Stop rotating
          self.wait(2)
  ```

**3.2. Advanced Camera Techniques**
- **Focusing on Specific Objects**:
  - You can adjust the camera's focal point to focus on specific parts of the scene.

  - **Example**:
    ```python
    self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
    self.move_camera(focus=cube)
    ```

- **Camera Path Animations**:
  - Create a path for the camera to follow during an animation.

  - **Example**:
    ```python
    class CameraPathAnimation(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            self.add(axes)
            cube = Cube()
            self.add(cube)

            # Define camera path
            self.play(self.camera.frame.animate.move_to(cube).set(width=cube.width*2))
            self.wait(2)
    ```

---

### **Key Takeaways for Days 27**

 
**Day 27**:
1. **3D Animations**: Explore the creation and animation of 3D objects and scenes in Manim.
2. **Camera Controls**: Master the use of camera movements and perspectives to enhance the visual experience of animations.

 
