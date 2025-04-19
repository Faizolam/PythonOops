# # 1.
# class Vehicle:
#     def __init__(self) -> None:
#         self.max_speed=0
#         self.mileage=0
#         print("done")
# s=Vehicle()

##2.
# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# schoolBus=Bus("MyBus",180,100)
# # print(schoolBus.name)
# print(f"Vehicle Name: {schoolBus.name} Speed: {schoolBus.max_speed} Mileage: {schoolBus.mileage}")

# #3, 4
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    
# schoolBus=Bus('MyBus',180,100)
# print(schoolBus.seating_capacity())


# # 5.
# class Vehicle:
#     #Class attribute
#     color = "White"

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
        

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# schoolBus=Bus("MyBus",180,12)
# myCar=Car("Audi Q5",240,18)
# # print(schoolBus.name)
# print(f"Color: {schoolBus.color} Vehicle Name: {schoolBus.name} Speed: {schoolBus.max_speed} Mileage: {schoolBus.mileage}")
# print(f"Color: {myCar.color} Vehicle Name: {myCar.name} Speed: {myCar.max_speed} Mileage: {myCar.mileage}")

##6.
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         totalFare=super().fare()+(self.capacity*100*0.1)
#         return totalFare

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

##7.##############################Write a program to determine which class a given Bus object belongs to.#####################################
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(type(School_bus))

##8.##############################Determine if School_bus is also an instance of the Vehicle class#####################################

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(isinstance(School_bus, Vehicle))


##################################################################################################################################
# class Staff:
#     def __init__(self, role, dept, __salary): 
#         self.role = role
#         self.dept = dept
#         self.__salary = __salary

#     def show_details(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Role:", self.role)
#         print("Department:", self.dept)
#         print("__salary:", self.__salary)

# #inherit from the Staff class
# class Teacher(Staff):
#     def __init__(self, name, age, role, dept, __salary):
#         self.name = name
#         self.age = age
#         # initialize the Parent  class
#         super().__init__(role, dept, __salary)


# teacher = Teacher("Raj", 28, "Teacher", "Maths", 200000)

# #access the Staff Method
# teacher.show_details()
# #display all namespace
# print(teacher.__dict__)


class Orders:
    def __init__(self, items):
        self.items = items

    # overload the + operator
    def __add__(self, other):
        return self.items + other.items

    # overload the > operator
    def __gt__(self, other):
        return len(self.items) > len(other.items)

order1 = Orders([5])

order2 = Orders([50])

# order1 = Orders([1, 2, 3, 4, 5, 6])

# order2 = Orders([10, 20, 30])

print("order1 + order2=", order1 + order2)
print("order1 > order2=", order1 > order2)
print(Orders.__add__)