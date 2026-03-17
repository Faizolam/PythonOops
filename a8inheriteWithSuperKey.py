########################################################Example of Super Keyword ####################################################
##~ The super() function is used to give access to methods and properties (not attributes) of a parent or sibling class from a child or sibling class.
##~ --> super() key shuold be first statment inside cunstructor otherwise super() will not work.


class Phone:
    def __init__(self, price, brand, camera) -> None:
        print("Inside Phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")
    
class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s=SmartPhone(20000,"Apple",13)
s.buy()

## s.super().buy() ##*NOTE:You can't use super() keyword out side of class, it will give error.
##* By using super key you can access only two things method of parent class and constructor of parent class, even you can not access the attributes.

# BISMALLAH>>PythonOop python .\a8inheriteWithSuperKey.py
# Inside Phone constructor
# Traceback (most recent call last):
#   File "F:\Python\PythonPractice\PythonOop\a8inheriteWithSuperKey.py", line 25, in <module>
#     s.super().buy()
# AttributeError: 'SmartPhone' object has no attribute 'super'

# ###################################################*The Super vs. Self Rule*##################################################
#! "super() accesses the parent's constructor (to set things up), but it cannot access the attributes created inside that constructor. To access those attributes, you must use self.attributeName."
#~ Why?
    #* super() is a "Manual Finder": It looks at the Parent Class to find instructions (methods like __init__). It doesn't know about specific data.
    #* self is the "Data Container": Once the parent's constructor runs, the attributes are stored directly inside the current object (self).

# # Cheat Sheet Example:
# class Parent:
#     def __init__(self):
#         self.money = 100  # Attribute created here

# class Child(Parent):
#     def __init__(self):
#         super().__init__()   # ✅ WORKS: Calls the instructions
        
#         # print(super().money) # ❌ FAILS: super() doesn't hold data
#         print(self.money)      # ✅ WORKS: self holds the data now
# kid = Child()




######################################################## *Super Example with constructor* #############################################
# class Phone:
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside Phone constructor")
#         self.__price=price
#         self.brand=brand
#         self.camera=camera
    
# class SmartPhone(Phone):

#     def __init__(self, price, brand, camera, os, ram) -> None:
#         print("Pehle Yahan")
#         super().__init__(price, brand, camera)
#         self.os=os
#         self.ram=ram
#         print("Inside smartphone constructor")

# s=SmartPhone(20000,"Samsung", 12, "Android", 2)

# print(s.os)
# print(s.brand)


######################################################## Super Example 1 with constructor ###########################################
# class Parent:
#     def __init__(self, num) -> None:
#         self.__num=num
    
#     print("second")

#     def get_num(self):
#         return self.__num

# class Child(Parent):
#     print("First")
#     def __init__(self, num, val) -> None:
#         print("super() key shuold be first statment inside custructor")
#         super().__init__(num)
#         self.__val=val
    
#     def get_val(self):
#         return self.__val

# son=Child(100,200)
# print(son.get_num())
# print(son.get_val())

######################################################## Super Example 2 with constructor ###########################################

# class Parent:

#     def __init__(self) -> None:
#         self.num=100


# class Child(Parent):

#     def __init__(self) -> None:
#         super().__init__()
#         self.var=200

#     def show(self):
#         print(self.num) #~accessing parent class attribute from child class via son object, because self it self son object.
#         print(self.var)


# son=Child()
# son.show()


######################################################## Super Example 3 with constructor ###########################################


# class Parent:

#     def __init__(self) -> None:
#         self.__num=100

#     def show(self):
#         print("Parent:", self.__num)

# class Child(Parent):

#     def __init__(self) -> None:
#         super().__init__()
#         self.__var=10

#     def show(self): #This one execute becz of method override
#         print("Child:", self.__var)


# dad=Parent()
# dad.show()
# son=Child()
# son.show()

# ************************************Optional Read for more clearity*******************************************************************

#! In Python, the reason you can access the constructor but not instance attributes using super() comes down to where that information is stored:
#~ 1. Methods (The Constructor) are in the Class 
    # The constructor (__init__) and other methods are functions stored in the Class definition.
    # super() is a proxy object designed specifically to look through the Class Hierarchy (Method Resolution Order) to find these functions.
    # Because the parent class "owns" the __init__ function, super() can find it and run it. 
#
#~ 2. Instance Attributes are in the Object 
    # Attributes like self.wealth are Instance Attributes. They are not part of the class "blueprint"; they are created only after you make a specific object.
    # Python stores these in a private dictionary called __dict__ that belongs to the individual object (self), not the class.
    # super() does not look inside the object's personal __dict__. It only looks at the classes themselves. 

#~ Why this is helpful to you
#* You don't need super() to get attributes. In Python, there is only one "bag" of data for your object: self. 
    # To initialize them: Use super().__init__() to tell the parent class to add its variables to the "bag".
    # To use them: Once they are in the bag, just use self.attribute_name. 

#~ Simple Summary
    # super() = "Go look at my parent's instructions (methods) to see how to do something."
    # self = "Look at my own data (attributes) that I currently have." 



#! Would you like to see what happens to the internal __dict__ (the "bag" of data) before and after you call super().__init__()?
#* To understand why super() acts this way, think of your object as a single backpack (self). The classes (Parent and Child) are just instruction manuals. 

#~ The Code: Watching the "Backpack" (__dict__)
    # You can use self.__dict__ to see exactly what is inside your object at any moment.

# class Parent:
#     def __init__(self):
#         # 2. This instruction manual says: "Put 'money' in the backpack"
#         self.money = 100

# class Child(Parent):
#     def __init__(self):
#         # 1. Right now, the backpack is empty
#         print(f"Before super: {self.__dict__}") 
        
#         # Accessing the CONSTRUCTOR (instruction manual)
#         super().__init__() 
        
#         # 3. Now the backpack has 'money' in it!
#         print(f"After super:  {self.__dict__}")

#         # ❌ super().money fails because 'money' is in the backpack (self), 
#         # not inside the instruction manual (the Parent class).
#         try:
#             print(super().money)
#         except AttributeError:
#             print("Error: super() can't find 'money' in the manual!")

# c = Child()

#~ Summary
    # Use super().__init__() to run the parent's setup instructions.
    # Use self.attribute to grab the data once it has been set up.
    # super() is for actions (methods); self is for data (attributes).