# class Customer:

#     def __init__(self, name, gender) -> None:
#         self.name=name
#         self.gender=gender 
#  #function   
# def greet(customer):
#     if customer.gender=="Male":
#         print("Hello", customer.name, "Sir!")
#     else:
#         print("Hello", customer.name, "Ma'am!")

#     cust2=Customer("Faiz","Male")
#     return cust2

# cust= Customer("Heena", "Female")
# # print(cust.name)
# # greet(cust)
# new_cust=greet(cust)
# print(new_cust.name)
# ----------------------------------------------------------------------
#~ cust is a refernce variable that storing reference address of actual object.
# pass by reference work like this
# >>> a = 3
# >>> b = a
# >>> id(a)
# 1646715339056
# >>> id(b)
# 1646715339056
# >>> 

#~ conclusion: if you can give to your function a list, int, tuple, dict than you can also pass a object of class inside the function b/c everything is object in python. 
# ---------------------------------------------------------------------

class Customer:

    def __init__(self, name) -> None:
        self.name=name

 #function 
 # if you pass a object in a function and if function edited the object then changes will reflect in the original object  
def greet(customer):
    print(id(customer))
    customer.name="Faiz" 
    print(customer.name)
    print(id(customer))
    
cust= Customer("Heena") #original object
print(id(cust))

greet(cust)
print(cust.name)
print('---------------------------------------------------------------------------')

#class ke objects are also mutable like lists, dict and sets.
#edit krne ke bad v addr wahi hota jo pahle tha it's shows the data type is mutable








def change(L):
    print(id(L))
    L.append(5)
    print(L)
    print(id(L))

L1=[1,2,3,4]
print(id(L1))
print(L1)

# change(L1)
change(L1[:]) #cloning([:]): do cloning if you don't want to get changes in you original list.
print(L1)
print("----------------------------------------------------------------------")


def change(T):
    print(id(T))
    T=T+(5,6)
    print(T)
    print(id(T))

T1=(1,2,3,4)
print(id(T1))
print(T1)

change(T1)
print(T1)

# pass by reference jo hota hai uske through mutable data type, including objects ko bhejo ge to original wale me changes ho jayege agr immutable wale ko bhej ge to original me changes nhi hogi, see above eg: List mutable and Tuple immutable.
