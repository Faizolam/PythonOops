class Atm:

    #static/class varible
    __counter = 1


    def __init__(self) -> None:
        #atributes
        #instence variable
        self.__pin=""    #Instence veriable are access by using self.variableName.
        self.__balance = 0
        self.sno = Atm.__counter  #Static/class variabel are access by using class name like className.variableName
        Atm.__counter=Atm.__counter + 1 # Increment the counter for the next instance

    #Instence variable: It's a variable for which the value is different for every object eg. pin, balance.
    #Static/class variable: It's a variable for which the value is same for every object
        
        print(id(self))
        # self.__menu()
    
    @staticmethod #@staticmethod: It's a special method which can be accessble without Object, generally it is use when we deal with static variable
    def get_counter():
        return Atm.__counter
    
    @staticmethod 
    def set_counter(new):
        if type(new)==int:
            Atm.__counter=new
        else:
            print("Not Allowed!")

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



# >>> from a5static import Atm
# >>> Atm.get_counter()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Atm.get_counter() missing 1 required positional argument: 'self'

#In this error get_counter() expecting self, means it expecting any object but trying to get counter by className.get_counter, But in the code method get_counter and set_counter we don't require self because we are not using self in side the method we just need class name.
#So When you making such a function which deals with your static variable than we don't pass self, for this use we use keyword @staticmethod and that type of are called static method.




#~ A good explaination of Staticmethod
# The `@staticmethod` decorator in Python is used to define a method in a class that doesn’t require access to the instance (`self`) or class (`cls`) objects. It essentially acts as a standalone function within the class, which can be useful for utility methods that logically belong to the class but don’t operate on instance-specific data.

# Here’s an example of how to use `@staticmethod` within the `Customer` class:


class Customer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"I am {self.name} and I am {self.age}")

    @staticmethod
    def welcome_message():
        print("Welcome to our store! We value every customer.")

# Creating customer instances
c1 = Customer("Nitish", 34)
c2 = Customer("Ankit", 45)
c3 = Customer("Neha", 32)

# Calling the static method without creating an instance
Customer.welcome_message()

# You can also call the static method from an instance, though it’s not required
c1.welcome_message()


###! Explanation
# - **Static Method**: `welcome_message` is a static method because it doesn’t depend on any instance variables. It can be called directly on the class (`Customer.welcome_message()`).
# - **Access**: You can still call it from an instance (`c1.welcome_message()`), but it's generally recommended to call it from the class directly for clarity.

###! When to Use
# Use `@staticmethod` when:
# - The method does not need access to instance attributes or methods.
# - It logically belongs to the class, such as a helper function or a method providing general information (e.g., utility methods or welcome messages).

# This approach keeps your code organized and leverages class-based structuring even for methods that don’t interact with specific instances.




#~ Another example1
# The error you're encountering (`AttributeError: type object 'Atm' has no attribute 'counter'`) occurs because the `counter` attribute is not defined in the `Atm` class. To use a static or class variable like `counter`, you need to define it within the class itself. Here’s how to correct it:

# 1. Define `counter` as a class attribute.
# 2. Access it using `Atm.counter`.

# Here's an example of how to set this up:


class Atm:
    # Class variable (static variable)
    counter = 1

    def __init__(self):
        # Instance variables
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.counter  # Accessing the class variable using the class name
        Atm.counter += 1  # Increment the counter for the next instance

# Creating instances of Atm
idfc = Atm()
hdfc = Atm()

# Accessing the instance variables and class variable
print("IDFC serial number:", idfc.sno)  # Should print 1
print("HDFC serial number:", hdfc.sno)  # Should print 2
print("Next counter:", Atm.counter)     # Should print 3

###! Explanation

# - **Class Variable** (`counter`): This is defined directly in the class scope, not within any method. It’s shared among all instances of `Atm`.
# - **Instance Variable** (`sno`): This is set in the `__init__` method, and each instance of `Atm` gets its own `sno` based on the value of `Atm.counter`.
# - **Incrementing `counter`**: Every time an instance is created, `counter` is incremented by 1, so each instance has a unique serial number.

# This setup allows each `Atm` instance to have a unique `sno`, while `counter` keeps track of the next serial number.



#~ Another Example2

# The issue arises because you are trying to access `counter` instead of `__counter`. Since `__counter` is defined with double underscores (`__`), it’s a private class variable. To access it, you need to use the same name with the double underscores in all references.

# Here’s how to fix it:

# 1. Replace `Atm.counter` with `Atm.__counter` in the `__init__` method.
# 2. Since `__counter` is a private variable, it can only be accessed within the class itself. If you need to access `counter` from outside the class, you can add a class method or a property to retrieve its value.

# Here’s the corrected code:


class Atm:
    # Private static/class variable
    __counter = 1

    def __init__(self) -> None:
        # Instance variables
        self.__pin = ""         # Instance variable accessed by using self.variableName
        self.__balance = 0
        self.sno = Atm.__counter  # Access the private class variable using Atm.__counter
        Atm.__counter += 1       # Increment the counter for the next instance

    @classmethod
    def get_counter(cls):
        return cls.__counter

# Creating an instance of Atm
idfc = Atm()
print("IDFC serial number:", idfc.sno)  # Should print 1
print("Current counter:", Atm.get_counter())  # Accessing counter via a class method

hdfc = Atm()
print("HDFC serial number:", hdfc.sno)  # Should print 2
print("Next counter:", Atm.get_counter())  # Should print 3


###! Explanation
# - **Private Class Variable** (`__counter`): This is prefixed with double underscores, making it private to the class.
# - **Accessing `__counter` in `__init__`**: Since `__counter` is private, use `Atm.__counter` to access it within the class.
# - **Class Method `get_counter`**: This method allows controlled access to the `__counter` variable from outside the class if needed.