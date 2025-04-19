
##@ Method Overloading
# #  Method overloading is a concept of Java in which we can create multiple methods of the same name in the same class, and all methods work in different ways. When more than one method of the same name is created in a Class, this type of method is called the Overloaded Method. But in the python class dose not support multiple method with the same name.

# class Geometry:

#     def area(self, radius):
#         return 3.14*radius*radius
    
#     def area(self,l,b):
#         return l*b
    
# obj = Geometry()
# print(obj.area(4)) # error becz same name method

## But below is a trick for overloading in python.

# class Geometry:

#     def area(self,a,b=0):
#         if b==0:
#             print("Circle", 3.14*a*a)
#         else:
#             print("Rectangle",a*b)


# obj=Geometry()
# obj.area(4)
# obj.area(4,5)


##@ Operator Overloading
##~ Operator overloading in Python allows you to define custom behavior for operators (+, -, *, /, etc.) when they are used with instances of your own classes. This feature enables you to define how operators should work with your objects, making your code more expressive and intuitive.

# # Here's a basic example of operator overloading in Python:

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     # Overloading the addition operator (+)
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     # Overloading the string representation for printing
#     def __str__(self):
#         return f"({self.x}, {self.y})"

# # Creating two Point objects
# point1 = Point(1, 2)
# point2 = Point(3, 4)

# # Using the overloaded addition operator
# result = point1 + point2
# print(result)  # Output: (4, 6)


# # In the above example:

# # We define a class Point representing a point in 2D space.
# # We overload the addition operator __add__() to define how two Point objects should be added together. In this case, it returns a new Point object with the coordinates summed.
# # We also overload the __str__() method to provide a custom string representation of the Point objects.
# # Operator overloading in Python is achieved by implementing special methods (also called magic methods or dunder methods) with predefined names such as __add__, __sub__, __mul__, __div__, etc., for each operator you want to overload.

# # Here are some common operators and their corresponding special methods for overloading:

# # + (addition): __add__
# # - (subtraction): __sub__
# # * (multiplication): __mul__
# # / (division): __truediv__
# # % (modulus): __mod__
# # == (equality): __eq__
# # != (inequality): __ne__
# # < (less than): __lt__
# # > (greater than): __gt__
# # <= (less than or equal to): __le__
# # >= (greater than or equal to): __ge__