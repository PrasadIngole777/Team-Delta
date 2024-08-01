
#### Day 11-12: Object-Oriented Programming (OOP)

**Object-Oriented Programming (OOP)** is a programming paradigm that uses "objects" – data structures consisting of fields and methods
– to design and organize software. It is based on several key principles: classes, objects, inheritance, polymorphism, and encapsulation.

#### Day 11: Foundations of Classes and Objects

**1. Classes and Objects**

- **Classes**: 
  - Definition: Blueprints for creating objects. They encapsulate data (attributes) and functions (methods) that operate on that data.
  - Syntax:
    ```python
    class ClassName:
        # Class attribute
        class_attribute = value

        # Initializer method (constructor)
        def __init__(self, attribute1, attribute2):
            self.attribute1 = attribute1  # Instance attribute
            self.attribute2 = attribute2  # Instance attribute

        # Method
        def method(self):
            # Method implementation
            pass
    ```

- **Objects**: 
  - Definition: Instances of a class. Each object can have unique values for its attributes.
  - Syntax:
    ```python
    object_name = ClassName(attribute1_value, attribute2_value)
    ```

- **Example**:
  ```python
  class Dog:
      # Class attribute
      species = "Canis familiaris"

      def __init__(self, name, age):
          self.name = name  # Instance attribute
          self.age = age    # Instance attribute

      def description(self):
          return f"{self.name} is {self.age} years old."

      def speak(self, sound):
          return f"{self.name} says {sound}"

  # Creating an object
  my_dog = Dog("Buddy", 5)
  print(my_dog.description())  # Output: Buddy is 5 years old.
  print(my_dog.speak("Woof"))  # Output: Buddy says Woof
  ```

**2. Special Methods (Magic Methods)**

- **Definition**: Special methods in Python are prefixed and suffixed with double underscores (`__`). They allow customization of certain behaviors in classes.
- **Common Special Methods**:
  - `__init__(self)`: Initializes a new object (constructor).
  - `__str__(self)`: Returns a human-readable string representation of an object.
  - `__repr__(self)`: Returns an unambiguous string representation of an object, useful for debugging.
  - `__len__(self)`: Returns the length of the object.
  - `__eq__(self, other)`: Compares two objects for equality.
  
- **Example**:
  ```python
  class Book:
      def __init__(self, title, author, pages):
          self.title = title
          self.author = author
          self.pages = pages

      def __str__(self):
          return f"{self.title} by {self.author}"

      def __len__(self):
          return self.pages

  my_book = Book("1984", "George Orwell", 328)
  print(my_book)             # Output: 1984 by George Orwell
  print(len(my_book))        # Output: 328
  ```

#### Day 12: Inheritance, Polymorphism, Encapsulation, Abstract Base Classes, and Interfaces

**1. Inheritance**

- **Definition**: A mechanism by which a new class (child class) inherits attributes and methods from an existing class (parent class). This promotes code reuse.
- **Syntax**:
  ```python
  class ParentClass:
      pass

  class ChildClass(ParentClass):
      pass
  ```

- **Types of Inheritance**:
  - **Single Inheritance**: Child class inherits from one parent class.
  - **Multiple Inheritance**: Child class inherits from multiple parent classes.
  - **Multilevel Inheritance**: A child class becomes a parent class for another child class.

- **Example**:
  ```python
  class Animal:
      def __init__(self, name):
          self.name = name

      def speak(self):
          raise NotImplementedError("Subclass must implement abstract method")

  class Cat(Animal):
      def speak(self):
          return "Meow"

  class Dog(Animal):
      def speak(self):
          return "Woof"

  my_cat = Cat("Kitty")
  my_dog = Dog("Buddy")
  print(my_cat.speak())  # Output: Meow
  print(my_dog.speak())  # Output: Woof
  ```

**2. Polymorphism**

- **Definition**: The ability of different objects to respond to the same method call in different ways.
-  It allows methods to be used interchangeably between objects of different classes.
- **Example**:
  ```python
  def animal_sound(animal):
      print(animal.speak())

  animal_sound(Cat("Kitty"))  # Output: Meow
  animal_sound(Dog("Buddy"))  # Output: Woof
  ```

**3. Encapsulation**

- **Definition**: The concept of wrapping data (attributes) and methods (functions) together into a single unit (class).
-  It restricts access to certain components, protecting object integrity.
- **Access Modifiers**:
  - **Public**: Accessible from anywhere (`self.attribute`).
  - **Protected**: Accessible within the class and its subclasses (`self._attribute`).
  - **Private**: Accessible only within the class (`self.__attribute`).

- **Example**:
  ```python
  class Person:
      def __init__(self, name, age):
          self.__name = name  # Private attribute
          self._age = age     # Protected attribute

      def get_name(self):
          return self.__name

      def set_name(self, name):
          self.__name = name

  person = Person("Alice", 30)
  print(person.get_name())    # Output: Alice
  person.set_name("Bob")
  print(person.get_name())    # Output: Bob
  ```

**4. Abstract Base Classes (ABCs) and Interfaces**

- **Abstract Base Classes (ABCs)**:
  - Definition: Classes that cannot be instantiated and are designed to be subclassed.
  - They can define a set of methods that must be created within any child class.
  - Use Case: To define a common interface for a group of subclasses.

- **Implementation in Python**:
  - ABCs are implemented using the `abc` module.
  - Syntax:
    ```python
    from abc import ABC, abstractmethod

    class AbstractClassName(ABC):
        @abstractmethod
        def abstract_method(self):
            pass
    ```

- **Example**:
  ```python
  from abc import ABC, abstractmethod

  class Shape(ABC):
      @abstractmethod
      def area(self):
          pass

      @abstractmethod
      def perimeter(self):
          pass

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height

      def perimeter(self):
          return 2 * (self.width + self.height)

  rect = Rectangle(5, 10)
  print(rect.area())       # Output: 50
  print(rect.perimeter())  # Output: 30
  ```

