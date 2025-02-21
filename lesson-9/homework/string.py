##Puzzle 1: Create a Simple Class
 Problem: Define a class Car with attributes brand and year. Create an object and print its attributes.
class Car:
    def __init__(self, brand, year):
        self.brand=brand
        self.year=year
    def object(self):
        print(f' Car brand: {self.brand}\n Car year is: {self.year}')
car1=Car('Tayota',2023)
car1.object()
car2=Car('Cybertrack', 2024)
car2.object()
##Puzzle 2: Default Constructor
 Problem: Create a class Person with a default constructor that sets name = "John" and age = 30.
class Person:
    def __init__(self, name='John', age=37):
        self.name=name
        self.age=age
person1=Person()

print(f' Name: {person1.name}, Age: {person1.age}')
##print(f' Name: {person.name}, Age: {person.age}')
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        pi=3.14
        print(f'Area of the circle where radius {self.radius} is {self.radius**2*pi};') 
area1=Circle(5)
area1.area()
## Puzzle 4: Class with Multiple Methods
 Problem: Define a class Rectangle with methods area() and perimeter().
class Rectangle:
    def __init__(self, heighth, width):
        self.heighth=heighth
        self.width=width
    def area(self):
        print(f' Rectangle Area of {self.width} and {self.heighth}  is {self.width*self.heighth}')    
    def perimeter(self):
        print(f"Rectangle Perimeter of {self.width} and {self.heighth}  is {self.width*2+self.heighth*2}'")   
rectangle1=Rectangle(3,4)
rectangle1.area()
rectangle1.perimeter()
## Puzzle 5: Encapsulation Problem: Create a class BankAccount with a private attribute _balance. Provide methods to deposit and withdraw money.

class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute to store balance
        self._balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. Current balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self._balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Get the current balance of the account."""
        return self._balance
     account = BankAccount(100)  # Initialize with a balance of 100
account.deposit(50)  # Deposit 50
account.withdraw(30)  # Withdraw 30
account.withdraw(200)  # Try to withdraw more than available
print("Final balance:", account.get_balance())
## Puzzle 6. Addition
Problem: Create a class method that will add x to y. Show the output
class Addition1:
    def __init__(self, num_x,num_y):
        self.num_x=num_x
        self.num_y=num_y
    def addi(self):
        print(f'Addition of {self.num_x} and {self.num_y} is {self.num_x+self.num_y}')   
value1=Addition1(3,4)
value1.addi()
## Puzzle 7. Multiple Inheritance
Problem: Create classes A and B. Create a class C that inherits from both.
class A:
    def method_a(self):
        print("Method from class A")

# Defining class B
class B:
    def method_b(self):
        print("Method from class B")

# Defining class C that inherits from both A and B
class C(A, B):
    def method_c(self):
        print("Method from class C")


obj_c = C()

# Calling methods from all classes
obj_c.method_a()  # Inherited from class A
obj_c.method_b()  # Inherited from class B
obj_c.method_c()  # Defined in cla
## Puzzle 8: Private Methods
Problem: Create a class Secret with a private method _hidden_message() that prints "This is private".
class Secret:
    def __hidden_massage__(self):
        print("This is private")
      

secret=Secret()     
secret.__hidden_massage__()
## Puzzle 9: Class with a Counter
Problem: Create a class Student that keeps track of the total number of students created.
class Student:
    total_students=0
 

    def __init__(self, name):
        self.name=name
        Student.total_students +=1
    @classmethod 
    def get_total_students(cls):
        return cls.total_students
    
    
student1=Student('Denzel')
student2=Student('Bob')
student3=Student('Lola')

print("Total number of students: ", Student.get_total_students())    
## Puzzle 10: Class with a Generator Method
Problem: Create a class EvenNumbers that generates even numbers up to a given limit using a method generate_even().
    class EvenNumbers:
    def __init__(self, limit):
        self.limit=limit

    def generate_even(self):

        even_numbers= []
        for num in range (2, self.limit + 1, 2):
            even_numbers.append(num)
        return even_numbers
      even_gen=EvenNumbers(20)
print ("Even numbers up to 20:", even_gen.generate_even())
