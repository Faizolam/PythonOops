class Vehicle:
    def __init__(self, vehicle_id, brand, model):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
        else:
            print(f"{self} is already rented.")

    def return_vehicle(self):
        if not self.is_available:
            self.is_available = True
        else:
            print(f"{self} is already available.")

    def __str__(self):
        return f"Vehicle: {self.brand} {self.model} (ID: {self.vehicle_id})"




class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, num_doors, price_per_day=5):
        super().__init__(vehicle_id, brand, model)
        self.num_doors = num_doors
        self.price_per_day = price_per_day

    def __str__(self):
        return f"Car - {self.brand} {self.model}, Doors: {self.num_doors} (ID: {self.vehicle_id})"

    

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, bike_type, price_per_day=5):
        super().__init__(vehicle_id, brand, model)
        self.bike_type = bike_type
        self.price_per_day = price_per_day

    def __str__(self):
        return f"Bike - {self.brand} {self.model}, Type: {self.bike_type} (ID: {self.vehicle_id})"


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id=customer_id
        self.name=name
        self.rented_vehicles={}

    def rent_vehicle(self, vehicle, number_of_days):
        if vehicle not in self.rented_vehicles and number_of_days and vehicle.is_available:
            vehicle.rent()
            self.rented_vehicles.append(vehicle, number_of_days)
            print(f"{self.name} has rented {vehicle.vehicle_id} for {number_of_days} days")
        else:
            print(f"{vehicle.vehicle_id} is not available.")
        

    def return_vehicle(self, vehicle, total_cost):
        if vehicle in self.rented_vehicles:
            vehicle.return_vehicle()
            self.rented_vehicles.remove(vehicle)
            print(f"{self.name} has returned {vehicle.vehicle_id}. Total cost: {total_cost}")
        else:
            print(f"{self.name} has not rented {vehicle.vehicle_id}.")

    def display_rentals(self):
        if self.rented_vehicles:
            for rental_vehicle in self.rented_vehicles:
                print(f"{self.name}'s rented vehicles {rental_vehicle.vehicle_id} for {self.rented_vehicles.number_of_days}")
                # print(f"- {rental_vehicle.vehicle_id}")
        else:
            print(f"{self.name} has not rented any vehicles.")


class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle:Vehicle):
        if self.find_vehicle_by_id(vehicle.vehicle_id) is None:
            self.vehicles.append(vehicle)
            print(f"Vehicle {vehicle.brand} model {vehicle.model} added successfully!")


    def add_customer(self, customer:Customer):
        if self.find_customer_by_id(customer.customer_id) is None:
            self.customers.append(customer)
            print(f"Customer name {customer.name} with id {customer.customer_id} registered successfully!")

    def find_vehicle_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle_id == vehicle.vehicle_id:
                return vehicle
        return None
    

    def find_customer_by_id(self,customer_id):
        for customer in self.customers:
            if customer_id == customer.customer_id:
                # print(customer)
                return customer
        return None

    def rent_vehicle(self, customer_id, vehicle_id, number_of_days):
        customer = self.find_customer_by_id(customer_id)
        vehicle = self.find_vehicle_by_id(vehicle_id)
        # print(customer)

        if customer and vehicle:
            if vehicle.is_available:
                customer.rent_vehicle(vehicle, number_of_days)
            else:
                print("Sorry, Car not available.")
        else:
            print("Invalid customer ID or vehicle ID.")


    def return_vehicle(self, customer_id, vehicle_id, number_of_days):
        customer =  self.find_customer_by_id(customer_id)
        vehicle = self.find_vehicle_by_id(vehicle_id)

        if customer and vehicle:
            total_cost = vehicle.price_per_day *  number_of_days
            customer.return_vehicle(vehicle, total_cost)
        else:
            print("Customer or Vehicle not found.")

    # def total_cost()


    def display_all_vehicles(self):
        print("All Vehicles:")
        for vehicle in self.vehicles:
            print(f"- {vehicle.vehicle_id}")

    def display_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(f"- {vehicle.vehicle_id}")


# Initialize service
service = RentalService()


# Create vehicles
car1 = Car("C101", "Toyota", "Corolla", 4, 60)
bike1 = Bike("B202", "Yamaha", "MT-15", "Sport", 40)
car2 = Car("C103", "Honda", "Civic", 4, 50)

# Add to service
service.add_vehicle(car1)
service.add_vehicle(bike1)
service.add_vehicle(car2)

# Create customers
cust1 = Customer("U1", "Ali")
cust2 = Customer("U2", "Sara")

# Add customers
service.add_customer(cust1)
service.add_customer(cust2)

# Rent and return
service.rent_vehicle("U1", "C101", 3)
service.rent_vehicle("U2", "B202", 2)
service.display_available_vehicles()

cust1.display_rentals()
cust2.display_rentals()

service.return_vehicle("U1", "C101", 3)
# service.display_all_vehicles()
service.display_available_vehicles()
