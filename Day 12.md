# Concept 1: Inheritance

### What is Inheritance?
```
Inheritance is a way to create a new class based on an existing class. The new class inherits all the properties and behavior of the existing class and can also add new properties and  behavior or override the ones inherited.
```
### Why Use Inheritance?
```
Inheritance helps to:

Reuse code
Create a hierarchy of classes
Simplify code maintenance
```
### Example:
```py
// Animal class (parent)
class Animal {
  void sound() {
    print("The animal makes a sound");
  }
}

// Dog class (child) inherits from Animal
class Dog extends Animal {
  void sound() {
    print("The dog barks");
  }
}
```
In this example, the Dog class inherits from the Animal class and overrides the sound() method to provide its own implementation.

# Concept 2: Polymorphism

### What is Polymorphism?
```
Polymorphism is the ability of an object to take on multiple forms. This can be achieved through method overriding or method overloading.

Method Overriding: When a child class provides a specific implementation for a method that is already defined in its parent class.

Method Overloading: When multiple methods with the same name can be defined, but with different parameter lists.
```
### Why Use Polymorphism?
```
Polymorphism helps to:

Increase flexibility
Improve code reusability
Simplify code maintenance
```
Example:
```py
// Shape class (parent)
class Shape {
  void draw() {
    print("Drawing a shape");
  }
}

// Circle class (child) inherits from Shape
class Circle extends Shape {
  void draw() {
    print("Drawing a circle");
  }
}

// Rectangle class (child) inherits from Shape
class Rectangle extends Shape {
  void draw() {
    print("Drawing a rectangle");
  }
}

// Polymorphic method
void drawShape(Shape shape) {
  shape.draw();
}

drawShape(new Circle()); // Output: Drawing a circle
drawShape(new Rectangle()); // Output: Drawing a rectangle
```
In this example, the drawShape() method takes a Shape object as a parameter, but it can work with objects of different classes (Circle and Rectangle) because of polymorphism.

# Concept 3: Encapsulation

### What is Encapsulation?

```
Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, called a class. The data is hidden from the outside world, and access to it is restricted through public methods.
```
### Why Use Encapsulation?
```
Encapsulation helps to:

Hide implementation details
Protect data from external interference
Improve code organization and readability
```
Example:
```py
class BankAccount {
  private double balance;

  public BankAccount(double initialBalance) {
    balance = initialBalance;
  }

  public void deposit(double amount) {
    balance += amount;
  }

  public void withdraw(double amount) {
    if (balance >= amount) {
      balance -= amount;
    } else {
      print("Insufficient balance");
    }
  }

  public double getBalance() {
    return balance;
  }
}
```
In this example, the BankAccount class encapsulates the balance data and provides public methods (deposit(), withdraw(), and getBalance()) to interact with it, while hiding the implementation details.

Abstract Base Classes (ABCs)
```
An abstract base class is a class that cannot be instantiated on its own and exists to be inherited by other classes.
```
Use:
```
Create a common base class for related classes

Force the class to implement some of its methods

Anonymous method (Provide default implementation for methods)
```
Interfaces
```
Interface is an abstract class in C# which contains only the declaration of methods.
```
Use:
```
A simple Interface, so defining contract that need to be implemented by classes

Separate class dependencies

Provide a way to test classes
```
