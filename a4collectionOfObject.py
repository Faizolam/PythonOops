class Customer:
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age
    
    def intro(self):
        print(f"I am {self.name} and i am {self.age}")

c1 = Customer("Nitish", 34) 
c2 = Customer("Ankit", 45) 
c3 = Customer("Neha", 32) 

print("--------------------------------List of objects-----------------------------------")
#!List of objects
L=[c1,c2,c3] 

#~you can do looping on objects
for obj in L:
    obj.intro()
    # print(i.name,i.age)

#!This same thing we can do also on dictionary and tuple, but not with sets because sets only accept immutable data types but objects are mutable data types 

print("--------------------------------Tuple of objects-----------------------------------")
#! Tuple of objects
T=(c1, c2, c3)

for obj in T:
    obj.intro()


print("--------------------------------dictionary of objects-----------------------------------")
#! Dictionary of objects
# Storing customers in a dictionary
D = {'customer1':c1, 'customer2':c2, 'customer3':c3}

# Looping through the dictionary values to call intro for each customer
for key, custobj in D.items():
    print(f'key: {key}')
    custobj.intro()
    # print(D[obj].intro())