########################################################Example of Super Keyword ####################################################
##~ The super() function is used to give access to methods and properties (not attributes) of a parent or sibling class from a child or sibling class.
##~ --> super() key shuold be first statment inside custructor otherwise super() will not work.


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

## s.super().buy() ##*NOTE:You can't use super() key word out side of class, it will give error.
##* By using super key you can access only two things method of parent class and constructor of parent class, even you can not access the attributes.

# BISMALLAH>>PythonOop python .\a8inheriteWithSuperKey.py
# Inside Phone constructor
# Traceback (most recent call last):
#   File "F:\Python\PythonPractice\PythonOop\a8inheriteWithSuperKey.py", line 25, in <module>
#     s.super().buy()
# AttributeError: 'SmartPhone' object has no attribute 'super'


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