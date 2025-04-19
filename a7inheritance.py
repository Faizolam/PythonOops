
## @Inheritance : code reusability

##~Inheritance: Inheritance in Python is a fundamental feature of object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. This promotes code reusability and the creation of a hierarchy of classes. Inheritance is implemented using the syntax class DerivedClassName(BaseClassName):, where DerivedClassName is the name of the new class being created and BaseClassName is the name of the class from which it inherits.
##~Inheritance in Python supports single inheritance, meaning a class can inherit from only one base class. However, Python also supports multiple inheritance, where a class can inherit from more than one base class.

                #                   User                                                                   User
                #     ________________|_______________                                                       |                             ^
                #     |                              |     ------Dry principle,code reusability---->         |-->login                     |
                # Student                        Instructor                                                  |-->Regs                      |
                #?    |-->login                      |-->login                                 ______________|_______________              | 
                #?    |-->Regs                       |-->Regs                                  |                            |              |
                #     |                              |                                       Student                  Instructor           |
                #     |-->Enroll                     |-->Create                                |                            |              |
                #     |-->Renew                      |-->Answer                                |-->Enroll                   |-->Create     |
                #     |                              |                                         |-->Renew                    |-->Answer     |

#Inheritance always happen in upper direction means you can inherite from User to Student and Instructor but you can't inheriate from Student and Instructor to User.


#? What we can inherite form parent to child class?
# We inherite things from parent to child calss.
# -->All Data members
# -->All Member functions or method.
# -->And constructor
# --> Private members can't inherite(__private)

#?Dynamic Representation of Inheritance Class
#!             _______________________                _______________________                                               
#!class------->|________User_________|                |________Student______|     
#!             | user's              |                | student's           |                
#!             | attributes          |                | attributes          |                                                                  
#!attributes-->|                     |                |                     |                                                                                      #!             |                     |                |                     |                                                                               
#!             |_____________________|                |_____________________|                            (-)-->Private                                           
#!             |                     |                |                     |                            (+)-->Public
#!             |  user's             |<|------------- | Student's           |                                                             
#!methods----->|   methods           |                | methods             |                               
#!             |                     |                |                     |                       
#!             | +login()            |                | + enroll()          |                                                                                    
#!             | + register()        |                | + review()          |                                                                     
#!             |                     |                |                     |                                                                                    
#!             |_____________________|                |_____________________|   

#~ Eg: Student Class inheriting from User Class(User<|-----Student)
# class User:

#     def login(self):
#         print("Login")

#     def register(self):
#         print("Register")

# class Student(User):

#     def enroll(self):
#         print("Enroll")

#     def review(self):
#         print("Review")

# # stu1=Student()

# # stu1.enroll()
# # stu1.review()
# # stu1.login()
# # stu1.register() 

# #* output: see you inherited from parent class to child class
# # BISMALLAH>>PythonOop python .\a7inheritance.py
# # Enroll
# # Review  
# # Login   
# # Register

# user1=User()

# user1.enroll()
# user1.review()
# user1.login()
# user1.register() 

# #* output: see you can not inherite from child class into parent class.
# # BISMALLAH>>PythonOop python .\a7inheritance.py
# # Traceback (most recent call last):
# #   File "F:\Python\PythonPractice\PythonOop\a7inheritance.py", line 56, in <module>
# #     u.enroll()
# # AttributeError: 'User' object has no attribute 'enroll'


################################################################Inheriting Constructor #################################################
# #NOTE: If you are creating an object of child class and if child class does not have a constructor then the constructor of parent class will be called.
# #Perent Class
# class Phone:
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
# #Child Class
# class SmartPhone(Phone):
#     pass

# s=SmartPhone(200, "Apple", 13)
# print(s.brand)

#########################################################Eg2-Inheriting Private members #############################################

# class Phone:
#     def __init__(self, price, brand, camera) -> None:
#         print("Inside phone constructor")
#         self.price = price
#         self.__brand = brand #Private attribute or hiden members can not inheritable by child class object
#         self.camera = camera

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(200, "Apple", 13)

# print(s.__brand) #* It will return error (AttributeError: 'SmartPhone' object has no attribute '__brand') Because child's class object can not access prents's class hidden member/attribute.

#########################################################Eg3-Polymorphism --> Method Overriding #####################################

##~ Method Overriding: method overriding occurs when a subclass (child class) has the same method as the parent class.
# class Phone:
#     def __init__(self, price, brand, camera) -> None:

#         print("Inside phone constructor")
#         self.price = price
#         self.__brand = brand 
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):          # It will execute becz of method overriding.
#         print("Buying a smartphone") 

# s=SmartPhone(200, "Apple", 13)
# # print(s.__brand)
# s.buy()


# #* In Polymorphism Their are three things. 
# #Method Overriding
# #Method Overloading
# #Operator Overriding


######################################################## Test-1 #####################################################################

##~ If the child has no its own constructor then the parent constructor automatically invoked.

# class Parent:
    
#     def __init__(self, num) -> None:
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def show(self):
#         print("This is in child class")


# son=Child(100)
# print(son.get_num())
# son.show()


######################################################## Test-2 #####################################################################

##~ If the child has its own constructor then the parent constructor will not invoked.

# class Parent:
#     def __init__(self, num) -> None:
#         self.__num=num
    
#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self,val, num) -> None:
#         self.__val=val
    
#     def get_val(self):
#         return self.__val

# son=Child(100,10)
# print("Parent: Num:",son.get_num())  #!It will return AttributeError: 'Child' object has no attribute '_Parent__num'becasue child have it own cunstructer that's why Parent cunstructer did not invoked and did not store self.__num value.
# # print("Child: Val:", son.get_val())


######################################################## Test-3 #####################################################################

# class A:
#     def __init__(self) -> None:
#         self.var1=100
    
#     def display1(self,var1):   #var1=200
#         print("class A :", self.var1) #~self.var1=100 The (output is 100 because you have sent 200 in var1 but we are printing self.var1 which is set as 100) 
##        print("class A :", self.var1, var1)          

# class B(A):

#     def display2(self, var1):
#         print("class B:", self.var1)

# obj=B()
# obj.display1(200)


