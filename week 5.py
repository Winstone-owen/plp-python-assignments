#Question 1
#Designing My Own Class!
#Create a class representing anything you like 
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
        
class scientific_calculator (calculator):
    def power(self):
        return self.num1 ** self.num2
    
    def square_root(self):
        if self.num1 >= 0:
            return self.num1 ** 0.5
        else:
            return "Cannot calculate square root of a negative number"
        
    def logarithm(self):
            import math
            if self.num1 > 0:
                return math.log(self.num1)
            else:
                return "Cannot calculate logarithm of a non-positive number"
            
            
basic_calc = calculator(10, 5)
print("Basic Calculator:")
print("Addition:", basic_calc.add())
print("Division:", basic_calc.divide())
print("Subtraction:", basic_calc.subtract())
print("Multiplication:", basic_calc.multiply())

sci_calc = scientific_calculator(16, 2)
print("\nScientific Calculator:")
print("Addition:", sci_calc.add())
print("Power:", sci_calc.power())
print("Square Root:", sci_calc.square_root())
print("Logarithm:", sci_calc.logarithm())


#Question 2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def move(self):
        print(f"{self.name} is moving.")

class Student(Person):
    def move(self):
        print(f"{self.name} is walking to school.")


class Teacher(Person):
    def move(self):
        print(f"{self.name} is driving to school.")


Person = Person("Alex", 30)
Student = Student("John", 15)
Teacher = Teacher("Mr. Smith", 40)

Person.display()
Person.move()

Student.display()
Student.move()

Teacher.display()
Teacher.move()