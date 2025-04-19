# When you constructing a large-scale application, it involves the creation of numerous classes, each with distinct relationships to one another.

        #!                      Relationship
        #!       ____________________|___________________             
        #!  ______|_________________       _____________|________
        #!  |   Aggregation        |       |      Inheritance   | 
        #!  |   Has-A Relationship |       |  Is-A Relationship |
        #!  |______________________|       |____________________| 


#Let's we have two class Product and Smartphone with their details, So What will be Inheritance relationship? 
# The relationship between them is Product Is-A Smartphone

        #!   _______________            _______________
        #!   |  Procuct    |            |  vehicle    |   
        #!   |_____________|            |_____________|  
        #!          |Is-A Smartphone           | Is-A car
        #!   _______|_______             ______|________      
        #!   |  Smartphone |             |  Car        | 
        #!   |_____________|             |_____________| 

#Let's we have two class Customer and Address with their details, So What will be aggregarion relationship? 
# The relationship between them is customer has-a address
        #!   _______________            _______________
        #!   |  Customer   |            |  Person     |   
        #!   |_____________|            |_____________|  
        #!          | |Has-A address           | |Has-A car
        #!   _______|_|_____             ______|_|______      
        #!   |  Address    |             |  Car        | 
        #!   |_____________|             |_____________| 

#Aggregation: When an object A contains a reference to another object B or we can say Object A has a HAS-A relationship with Object B, then it is termed as Aggregation. Aggregation helps in reusing the code. Object B can have utility methods and which can be utilized by multiple objects

#?Dynamic Representation of Aggregation Class
#!             _______________________                _______________________                                               
#!class------->|________Atm__________|                |_____AtmSBranch______|     
#!             | -pin                |                | -pin                |                
#!             | -balance            |                | -balance            |                                                                  
#!attributes-->|                     |                |                     |                                                                                      #!             |                     |                |                     |                                                                               
#!             |_____________________|                |_____________________|                            (-)-->Private                                            
#!             | - __init__()        |<>--------------| - __init__()        |                            (+)-->Public
#!             | - menu()            |                | - menu()            |                                                             
#!methods----->| + change_pin()      |                | + change_pin()      |                               
#!             | + deposit()         |                | + deposit()         |                       
#!             | + withdraw()        |                | + withdraw()        |                                                                                    
#!             | + check_balance()   |                | + check_balance()   |                                                                     
#!             |                     |                |                     |                                                                                    
#!             |_____________________|                |_____________________|                                                                                      
#~ eg: Customer --> has A --> Address(Customer<>-----Address)

class Customer:
    def __init__(self,name,gender,address) -> None:
        self.name=name
        self.gender=gender
        self.address=address
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)

class Address:

    def __init__(self,city,pincode,state) -> None:
        self.city=city
        self.pincode=pincode
        self.state=state
    
    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state=new_state

#Aggregation: Passing an object inside another object
#*Here add object passing inside cust object
add=Address("Kolkata",700156,"WB")
cust=Customer("Faiz","Male",add)

cust.edit_profile("Masnoon","Gurgaon",122011,"Haryana")

print(cust.name,cust.address.pincode)