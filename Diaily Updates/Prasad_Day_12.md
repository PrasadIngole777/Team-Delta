Inheritance in OOP :

        Inheritance is a fundamental concept in object-oriented programming that allows programmers to reuse code 
        and create class hierarchies. It is a way to form  new classes using classes that have already been defined. 
        The new classes, known as derived classes, inherit attributes and behavior of the pre-existing 
        classes, which are referred to as base classes.

Example : 
      
      class Human:
          species = "Homo sapiens"

      class Man(Human):
          def gender():
            return "Male"


      man = Man()
      print(man.species)  # Inherited from Human
      print(Man.gender()) # Male

Encapsulation and Abstraction : 

        Encapsulation is the mechanism of hiding data and functions within an object and making them inaccessible 
        from the outside world. Abstraction is the process of exposing only the necessary information and hiding 
        the implementation details. Together, encapsulation and abstraction help to create well-designed, modular,
        and secure code.

Polymorphism :

        Polymorphism is the ability for objects of different types to be treated as if they are of the same type. 
        In the context of inheritance, polymorphism allows objects of derived classes to be used in place of objects 
        of base classes, enabling more flexible and reusable code.

        Types :
        --> Compile-time
        --> Runtime 

Abstract Base Classes (ABCs) : 

    Abstract Base Classes in Python define a blueprint for other classes. They cannot be instantiated directly and 
    usually contain one or more abstract methods that must be implemented by subclasses.

