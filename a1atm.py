class Atm:
    #48:00min
    # __init__ :The constructor is a method that is called when an object is created. constructor run the code automatically when object create. 
    #? What is an Instance Variable in Python? 
    # If the value of a variable varies from object to object, then such variables are called instance variables. For every object, a separate copy of the instance variable will be created. Instance variables are not shared by objects.
    def __init__(self) -> None:
        #atributes
        self.__pin=""  #encapsulation (__variable)
        self.__balance = 0  

        print(id(self))
        self.__menu()

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin Changed!")
        else:
            
            print("Not Allowed")    

#method(function)
    def __menu(self):
        user_input=input(""" 
                    Hello, how would you like to proceed?
                    1.Enter 1 to create pin.
                    2.Enter 2 to deposit.
                    3.Enter 3 to withdraw.
                    4.Enter 4 to check balance.
                    5.Enter 5 to exit.
""")

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
           self.withdraw()
        elif user_input=='4':
            self.check_balance()
        else:
            print("Bye!")
        
    def create_pin(self):
        self.__pin=input("Enter you pin ")
        print("Pin set successfully!")
    
    def deposit(self):
        temp = input("Enter your pin ")
        if self.__pin ==temp:
           amount=int(input("Enter the amount "))
           self.__balance=self.__balance+amount
           print("Deposit successful!")
        else:
            print("Invalid pin ")
    def withdraw(self):
        temp = input("Enter your pin ")
        if self.__pin ==temp:
            amount=int(input("Enter your amount "))
            if amount< self.__balance:
                self.__balance=self.__balance-amount
                print("Operation Successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")
    def check_balance(self):
        temp = input("Enter your pin ")
        if self.__pin ==temp:
            print(self.__balance)
        else:
            print("Invalid pin ")

## @Self
#56:00min Self

# from a1atm import Atm 
# >>> sbi = Atm()
# 2753261143040

# >>> id(sbi)
# 2753261143040


# >>> hdfc=Atm()
# 2753261148512
# >>> id(hdfc)
# 2753261148512

# if i remove self from create_pin(self) method then it gives an error see below. 

# File "F:\PythonPractice\PythonOop\a1atm.py", line 33, in __menu
#     self.create_pin()
# TypeError: Atm.create_pin() takes 0 positional arguments but 1 was given

# jab object name with dot(sbi.create_pin()) krke call hota hai to us method me by default 1 argument pass hota hai aor wahi hai wo object.
# yani jab sbi object create_pin() method ko call kr rha hai to is method ko by default 1 input sbi mil rah hai aor wahi create_pin() method ke self me recive ho rha hai. 
# It means sbi hi self hai
            



# In Python, an instance variable is a variable that is bound to an instance of a class. These variables are specific to an instance of the class and are used to store data that belongs to that particular instance. Each instance of a class can have different values for its instance variables.

# Here's an example to illustrate the concept of instance variables:

# python code
            
# class Dog:
#     def __init__(self, name, age):
#         # These are instance variables
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name} says Woof!")

# # Creating instances of the Dog class
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)

# # Accessing instance variables
# print(f"{dog1.name} is {dog1.age} years old.")
# print(f"{dog2.name} is {dog2.age} years old.")

# # Calling a method that uses instance variables
# dog1.bark()
# dog2.bark()

# In this example, the `Dog` class has two instance variables, `name` and `age`, which are defined in the `__init__` method. When you create instances of the `Dog` class (like `dog1` and `dog2`), you provide values for these instance variables.

# Instance variables are accessed using the dot notation (`object.variable`). In the example, `dog1.name` and `dog2.name` access the `name` instance variable for each respective instance.

# Instance variables are useful for storing and managing the state of individual objects created from a class.

# ? Need for encapsulation
# But you can't leave your data member publiclly you have to hide. using (__)
# For eg.  
# self.__pin=""  #encapsulation (__variable)
# self.__balance = 0 

# You can also hide your method if needed like
# def __menu(self):

#What happen after puting (__)
# Python internally convert it
# __pin --> __Atm__pin

#If you write
# sbi.__balance="asljfla" # Here it become new veriable __balance
# Although you have created a new variable in this class but this new variable is not creating any problem because it is not used by any method, all the methods are using this __Atm__pin variable.

#But if some do like this sbi.__Atm__pin='lsfjs' then your variable edit and it maybe create problem.
#Although I hide the variable by using (__) I can give access by making two functions for eg. get_pin and set_pin   
#NOTE: In python there is nothing private But i can hide my data and give access of data on my condtions by making function like geter and seter.

#?Dynamic Representation of Class

#              _______________________
# class------->|________Atm__________|     (-)-->Private
#              | -pin                |
#              | -balance            |
# attributes-->|                     |
#              |                     |
#              |_____________________|
#              | - __init__()        |     (+)-->Public
#              | - menu()              |
# methods----->| + change_pin()      |
#              | + deposit()         |
#              | + withdraw()        |
#              | + check_balance()   |
#              |                     |
#              |_____________________|


#? reference variable
# >>> Atm()
# 1395876823104

#                     Hello, how would you like to proceed?
#                     1.Enter 1 to create pin.
#                     2.Enter 2 to deposit.
#                     3.Enter 3 to withdraw.
#                     4.Enter 4 to check balance.
#                     5.Enter 5 to exit.
# 1
# Enter you pin 123
# Pin set successfully!
# <a1atm.Atm object at 0x0000014500BE0040>

# Above o/p showing a object is created at this memory location <a1atm.Atm object at 0x0000014500BE0040>, but you can't use this object because at that point you created this object you did not store in any variable and because of that this object lost you can't find this in memory.
# Whenever you create a object you write this 
# sbi = Atm() --> So here object will be Atm() and we stores object reference in the sbi variable
 




# In Python's Object-Oriented Programming (OOP), a reference variable is a variable that points to an object, allowing operations to be performed on that object. This concept is crucial for understanding how objects interact within a class and how data is accessed and manipulated.

# A reference variable can be explicitly defined when creating an instance of a class, as shown in the example where `e` is a reference variable pointing to an `Employee` object. This allows external access to the object's variables and methods. Additionally, the `self` keyword is an implicit reference variable used within the class to refer to the current object instance. It enables the class's methods to access and modify the object's attributes.

# Class variables, which are variables declared within a class but outside any instance method, can be accessed and modified using either the class name or an instance of the class. However, modifying a class variable through an instance creates an instance variable that shadows the class variable, leading to different values for the variable across different instances. To ensure that all instances share the same value, it's recommended to modify class variables using the class name.

# Here's an example demonstrating the use of reference variables and class variables in a Python class:


class Employee:
    # Class variable
    company = 'ABC Corp'

    def __init__(self, emp_id, emp_name, emp_address):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_address = emp_address

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Address: {self.emp_address}, Company: {self.company}")

# Creating an instance of Employee
e = Employee(1, 'John Doe', '123 Main St')

# Accessing class variable using the instance
print(e.company)

# Modifying class variable using the class name
Employee.company = 'XYZ Corp'

# Accessing the modified class variable using the instance
print(e.company)


# In this example, `e` is a reference variable pointing to an instance of the `Employee` class. The `company` variable is a class variable that can be accessed and modified using either the class name `Employee.company` or the instance `e.company`. However, modifying it through an instance creates an instance variable, which is why it's recommended to use the class name for modifications to ensure all instances share the same value.
