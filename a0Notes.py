 ## @A data type is a class and a variable created using that data type is an object of that class.
                #!               class
                #!        _________|__________ 
                #!    ____|________    ______|________
                #!    | Data or   |    | Function or |
                #!    | property  |    | Behavior    |
                #!    |___________|    |_____________|


## @Object: Object is an instance of the class
#? class         Object           Create objects in python
# Car     ----> WagorR//         wagonr=Car()
# Sports  ----> Gilli Danda//    gillidanda=Sports()
# Animals ----> Langoor//        langoor=Animals()

#Object Literal
L=list()

L.append(1) #--> append is a method, it's mean there is function defined in side the list() class

len(L) #--> len is a function 

#?Dynamic Representation of Class

#!              _______________________
#! class------->|________Car__________|     (-)-->Private
#!              | -Color              |
#!              | -Milage             |
#! attributes-->| -Engine             |
#!              |                     |
#!              |_____________________|
#!              | +cal_avg_speed      |     (+)-->Public
#!              | +open_airbeg        |
#! methods----->| +show_gps           |
#!              |                     |
#!              |                     |
#!              |_____________________|

# Public Members
# Public members are accessible from anywhere in the code, including from outside the class. In Python, public members are those that do not have any special prefix. For example:
class Geek:
    def __init__(self, name, age):
        self.geekName = name
        self.geekAge = age

    def displayAge(self):
        print("Age: ", self.geekAge)
# In this example, geekName and geekAge are public attributes, and displayAge is a public method. They can be accessed and used from anywhere in the code 2.

# Private Members
# Private members are intended to be hidden from outside access. In Python, private members are denoted by a double underscore prefix (__). For example:
class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    def __displayDetails(self):
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()
# In this example, __name, __roll, and __branch are private attributes, and __displayDetails is a private method. They can only be accessed within the class itself. The accessPrivateFunction method is a public method that can access the private members of the class.

## @Function

#* Function: A function is a block of reusable code that performs a specific task. Functions are defined independently and can be called by their name. They can operate on data passed to them as arguments and can return data. Functions are not associated with any class or object. They are defined using the def keyword.
def sum(num1, num2):
    return num1 + num2

## @Method

#* Method: A method is a function that is associated with an object or a class. Methods are defined within a class and are called on instances of that class. They are implicitly passed the instance of the class (the object) on which they are invoked, which is typically referred to as self. Methods can access and modify the data contained within the class instance.
class Dog:
    def my_method(self):
        print("I am a Dog")

dog = Dog()
dog.my_method() # Prints "I am a Dog"


#? The primary differences between a function and a method in Python are:

# Association: Functions are not associated with any class or object, whereas methods are defined within a class and are associated with an object of that class.
# Invocation: Functions are called by their name, while methods are called on an object of the class they are defined in.
# Access to Data: Methods can access and modify the data (instance variables) contained within the class instance, while functions operate on data passed to them as arguments.

# In summary, while functions and methods in Python may appear similar, the key difference lies in their association with objects and classes. Functions are standalone, whereas methods are tied to a class and operate on the data of an instance of that class

