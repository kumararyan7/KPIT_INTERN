class Vehicle:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage}")

class Car(Vehicle):
    def __init__(self, make, model, year, color, mileage, engine_size, transmission_type):
        super().__init__(make, model, year, color, mileage)
        self.engine_size = engine_size
        self.transmission_type = transmission_type

# Vehicle = [
#     Car("Toyota", "Camry", 2020, "Blue", 30000, 2.5, "Automatic"),
#     Car("Honda", "Civic", 2012, "White", 100000, 1.8, "Manual"),
    
    
# ]

# # Test functionality
# for vehicle in Vehicle:
#     vehicle.display_details()
   

  def find_Vehicle_by_make(make):
    # Check if the dictionary is empty
    if not Vehicle:
        print("No Vehicle in the database")
    else:
        # Find Vehicle by make
        found_Vehicle = [vehicle_id for vehicle_id, vehicle in Vehicle.items() if vehicle["make"] == make]
        if found_Vehicle:
            print(f"Vehicle found with make {make}:")
            for vehicle_id in found_Vehicle:
                print(vehicle_id)
        else:
            print(f"No Vehicle found with make {make}")

def find_Vehicle_by_model(model):
    # Check if the dictionary is empty
    if not Vehicle:
        print("No Vehicle in the database")
    else:
        # Find Vehicle by model
        found_Vehicle = [vehicle_id for vehicle_id, vehicle in Vehicle.items() if vehicle["model"] == model]
        if found_Vehicle:
            print(f"Vehicle found with model {model}:")
            for vehicle_id in found_Vehicle:
                print(vehicle_id)
        else:
            print(f"No Vehicle found with model {model}")



def display_Vehicle():
    # Check if the dictionary is empty
    if not Vehicle:
        print("No Vehicle in the database")
    else:
        # Print each vehicle in the dictionary
        for vehicle_id, vehicle in Vehicle.items():
            print(f"Vehicle ID: {vehicle_id}")
            print(f"Make: {vehicle['make']}")
            print(f"Model: {vehicle['model']}")
            print(f"Year: {vehicle['year']}")
            print(f"Mileage: {vehicle['mileage']}")
            print(f"Fuel mileage_: {vehicle['fuel_mileage_']}")
            print("------------------------")

def search_vehicle(vehicle_id):
    # Check if the vehicle exists in the dictionary
    if vehicle_id in Vehicle:
        # Print the vehicle information
        vehicle = Vehicle[vehicle_id]
        print(f"Vehicle ID: {vehicle_id}")
        print(f"Make: {vehicle['make']}")
        print(f"Model: {vehicle['model']}")
        print(f"Year: {vehicle['year']}")
        print(f"Mileage: {vehicle['mileage']}")
        print(f"Fuel mileage_: {vehicle['fuel_mileage_']}")
    else:
        print(f"Vehicle with ID {vehicle_id} not found")

def calculate_average_fuel_mileage_():
    # Check if the dictionary is empty
    if not Vehicle:
        print("No Vehicle in the database")
    else:
        # Calculate the average fuel mileage_
        total_fuel_mileage_ = sum(vehicle["fuel_mileage_"] for vehicle in Vehicle.values())
        average_fuel_mileage_ = total_fuel_mileage_ / len(Vehicle)
        print(f"Average fuel mileage_: {average_fuel_mileage_}")

def calculate_total_mileage():
    # Check if the dictionary is empty
    if not Vehicle:
        print("No Vehicle in the database")
    else:
        # Calculate the total mileage
        total_mileage = sum(vehicle["mileage"] for vehicle in Vehicle.values())
        print(f"Total mileage: {total_mileage}")


# Test the functions
Vehicle("1234567890", "Toyota", "Camry", 2020, 20000, 25)
# add_vehicle("234567890", "Honda", "Civic", 2019, 30000, 30)
# add_vehicle("456789012", "Tesla", "Model3", 2021, 40000, 28)
display_Vehicle()
search_vehicle("V1")
calculate_average_fuel_mileage_()
calculate_total_mileage()
find_Vehicle_by_make("Toyota")
find_Vehicle_by_model("Civic")
