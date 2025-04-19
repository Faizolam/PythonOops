class Vehicle:
    def __init__(self,vehicle_id, brand, model):
        self.vehicle_id=vehicle_id
        self.brand=brand
        self.model=model
        self.is_available=True

    def rent(self):
        self.is_available = False
    
    def return_vehicle(self):
        self.is_available = True

    def __str__(self):
        return f"Vehicle: {self.vehicle_id}, {self.brand}, {self.model}"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, num_doors):
        super().__init__(vehicle_id, brand, model)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__} (Doors: {self.num_doors})"
    
class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, cartype):
        super().__init__(vehicle_id, brand, model)
        self.cartype = cartype

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id=customer_id
        self.name=name
        self.rented_vehicles=[]

    def rent_vehicle(vehicle_id):
        pass
    def return_vehicle(vehicle_id):
        pass
    def display_rentals():
        pass

class RentalService:
    def __init__(self):
        self.vehicle = []
        self.customers = []

    def add_vehicle(self, vehicle):
        pass

    def add_customer(self, customer):
        pass

    def find_vehicle_by_id(self, vehicle_id):
        pass

    def find_customer_by_id(self,customer_id):
        pass

    def rent_vehicle(self, customer_id, vehicle_id):
        pass

    def return_vehicle(self, customer_id, vehicle_id):
        pass

    def display_all_vehicles():
        pass

    def display_available_vehicles():
        pass