# There are 4 types of inheritance
#! 1. Single level Inheritance        2. multi-level Inheritance       3. Hierarchical Inheritance        4. Multiple Inheritance       5. Hybrid Inheritance(Hybrid Inheritance is a combination of all 4 types.)

#!                                       ______________                ______________           ___________     ___________             ______________    
#!                                       | GrandParent|                |   Parent   |           | Parent  |     | Mother  |             | GrandParent|
#!                                       |____________|                |____________|           |_________|     |_________|             |____________|
#!                                             |                             |                       |               |                        |
#!   ______________                      ______|________              _______|_______                |_______________|                  ______|________ 
#!   |  Parent    |                      |  Parent     |         _____|_____   _____|_____                   |                          |  Parent     |
#!   |____________|                      |_____________|         | Child1  |   | Child2  |             ______|______                    |_____________|
#!          |Inherite from parent              | Is-A car        |_________|   |_________|             |   Child   |                          |
#!   _______|_____                       ______|________                                               |___________|                    ______|________
#!   |  Child    |                       |  Child      |                                                                                |             |
#!   |___________|                       |_____________|                                                                         _______|___        __|________
#!                                                                                                                               | Child1  |        | Child2  |
#!                                                                                                                               |_________|        |_________|
#!                                                                                                                                      |______________|
#!                                                                                                                                              |
#!                                                                                                                                        ______|______       
#!                                                                                                                                        |GrandChild1|      
#!                                                                                                                                        |___________| 
#!                                                                                                                                              |
#!                                                                                                                                        ______|______       
#!                                                                                                                                        |GrandChild |
#!                                                                                                                                        |Of Child   |  
#!                                                                                                                                        |___________|
######################################################## Example of Single level inheritance ######################################################################

# #Perent Class
# class Phone:
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

#     def return_phone(self):
#         print("Returning a phone")

# #Child Class
# class SmartPhone(Phone):
#     pass

# SmartPhone(10000, "Apple", "13px").buy()
# # print(s.brand)


######################################################## Example of Multilevel inheritance #########################################

# class Product:
#     def review(self):
#         print("Product customer review")


# class Phone(Product):
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#         print("here Also")

#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(20000,"Apple",12)
# p=Phone(1000,"Samsung",1)

# s.buy()
# s.review()   
# p.review()         


######################################################## Example of Hierarchical inheritance ########################################

# class Phone():
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     pass

# class FeaturePhone(Phone):
#     pass

# s=SmartPhone(20000,"Apple","13px").buy()


######################################################## Example of Multiple inheritance ############################################

# class Phone():
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
       

#     def buy(self):
#         print("Buying a phone")


# class Product:
#     def review(self):
#         print("Product customer review")

# class SmartPhone(Phone,Product): #*Here smartphone has no constructor so the phone's constructor is being invoked as the phone has a constructor, if the phone has no constructor then the product's constructor will be called, but the product has no constructor.
#     pass

# s=SmartPhone(20000,"Apple",12)
# # p=Phone(1000,"Samsung",1)

# s.buy()   
# s.review()

######################################################## Example of Multiple inheritance with MRO(method resolution order) ####################################
#~Here you are calling s.buy() but you see in the code there are two buy() functions in two classes so which one will be called, it depends on which class called first in the SmartPhone() class.
# class Phone:
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
       

#     def buy(self):
#         print("Buying a phone")


# class Product:
#     def buy(self):
#         print("Product buy method")

# # class SmartPhone(Phone,Product):    
# class SmartPhone(Product,Phone):  #In the same order in which you are inheriting will execute first this is called MRO
#     pass

# s=SmartPhone(20000,"Apple",12)
# # p=Phone(1000,"Samsung",1)

# s.buy()


######################################################## Example 1 on type  #########################################################

# class A:

#     def m1(self):
#         return 20
    
# class B(A):

#     def m1(self):
#         return 30
#     def m2(self):
#         return 40
# class C(B):

#     def m2(self):
#         return 20
    
# obj1=A()
# obj2=B()
# obj3=C()

# print(obj1.m1()+obj3.m1()+obj3.m2())
# print(obj1.m1()+obj2.m1()+obj3.m2())
# #print(obj1.m1()+obj2.m1()+obj1.m2())#Error: Parent can't inherite from child.


## print(obj1.m1()+obj3.m1()+obj3.m2())
## 20+30+20=70
# 20--> get from class A.
# 30--> get from class B because of we can't inherite from grandpaa if we have method present in parent class.
# 20--> get from class C because method overriding.
######################################################## Example 1 on type  #########################################################

# class A:

#     def m1(self):
#         return 20
    
# class B(A):

#     def m1(self):
#         val = super().m1()+30
#         return val 
    
#     # def m2(self):
#     #     return 40
# class C(B):

#     def m1(self):
#         val = self.m1()+20
#         return val
# obj=C()
# print(obj.m1())

# Because it calling it self again and again
# Error:val = self.m1()+20
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

#############################################################################################################################################################
## Python uses a depth-first left-to-right search strategy to determine the MRO. This means that it looks for methods and attributes in the current class before moving to its parent class(es), following a specific order defined by the class hierarchy.

## The MRO can be accessed using the __mro__ attribute or the mro() method. Here's an example to illustrate how MRO works:
# class A:
#     def greet(self):
#         return "Hello from A"

# class B(A):
#     def greet(self):
#         return "Hello from B"

# class C(A):
#     def greet(self):
#         return "Hello from C"

# class D(B, C):
#     pass

# # MRO for class D
# print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# # Call the greet method of class D
# d = D()
# print(d.greet())  # Output: Hello from B
