# Initialize 
vehicles = {}

def add_vehicle(vehicle_id, make, model, year, mileage, fuel_mileage_):
    #  a new dictionary 
    vehicle = {
        "make": make,
        "model": model,
        "year": year,
        "mileage": mileage,
        "fuel_mileage_": fuel_mileage_
    }
    # Add the vehicle to the dictionary
    vehicles[vehicle_id] = vehicle
    print(f"Vehicle with ID {vehicle_id} added successfully")

def remove_vehicle(vehicle_id):
    # if vehicle already exists in the dictionary
    if vehicle_id in vehicles:
        # Remove the vehicle from the dictionary
        del vehicles[vehicle_id]
        print(f"Vehicle with ID {vehicle_id} removed successfully")
    else:
        print(f"Vehicle with ID {vehicle_id} not found")

def find_vehicles_by_make(make):
    # Check if the dictionary is empty
    if not vehicles:
        print("No vehicles in the database")
    else:
        # Find vehicles by make
        found_vehicles = [vehicle_id for vehicle_id, vehicle in vehicles.items() if vehicle["make"] == make]
        if found_vehicles:
            print(f"Vehicles found with make {make}:")
            for vehicle_id in found_vehicles:
                print(vehicle_id)
        else:
            print(f"No vehicles found with make {make}")

def find_vehicles_by_model(model):
    # Check if the dictionary is empty
    if not vehicles:
        print("No vehicles in the database")
    else:
        # Find vehicles by model
        found_vehicles = [vehicle_id for vehicle_id, vehicle in vehicles.items() if vehicle["model"] == model]
        if found_vehicles:
            print(f"Vehicles found with model {model}:")
            for vehicle_id in found_vehicles:
                print(vehicle_id)
        else:
            print(f"No vehicles found with model {model}")



def display_vehicles():
    # Check if the dictionary is empty
    if not vehicles:
        print("No vehicles in the database")
    else:
        # Print each vehicle in the dictionary
        for vehicle_id, vehicle in vehicles.items():
            print(f"Vehicle ID: {vehicle_id}")
            print(f"Make: {vehicle['make']}")
            print(f"Model: {vehicle['model']}")
            print(f"Year: {vehicle['year']}")
            print(f"Mileage: {vehicle['mileage']}")
            print(f"Fuel mileage_: {vehicle['fuel_mileage_']}")
            print("------------------------")

def search_vehicle(vehicle_id):
    # Check if the vehicle exists in the dictionary
    if vehicle_id in vehicles:
        # Print the vehicle information
        vehicle = vehicles[vehicle_id]
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
    if not vehicles:
        print("No vehicles in the database")
    else:
        # Calculate the average fuel mileage_
        total_fuel_mileage_ = sum(vehicle["fuel_mileage_"] for vehicle in vehicles.values())
        average_fuel_mileage_ = total_fuel_mileage_ / len(vehicles)
        print(f"Average fuel mileage_: {average_fuel_mileage_}")

def calculate_total_mileage():
    # Check if the dictionary is empty
    if not vehicles:
        print("No vehicles in the database")
    else:
        # Calculate the total mileage
        total_mileage = sum(vehicle["mileage"] for vehicle in vehicles.values())
        print(f"Total mileage: {total_mileage}")


# Test the functions
add_vehicle("1234567890", "Toyota", "Camry", 2020, 20000, 25)
add_vehicle("234567890", "Honda", "Civic", 2019, 30000, 30)
add_vehicle("456789012", "Tesla", "Model3", 2021, 40000, 28)
display_vehicles()
search_vehicle("V1")
calculate_average_fuel_mileage_()
calculate_total_mileage()
find_vehicles_by_make("Toyota")
find_vehicles_by_model("Civic")
remove_vehicle('1234567890')