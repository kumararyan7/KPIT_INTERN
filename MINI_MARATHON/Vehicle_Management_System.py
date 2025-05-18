from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle:
    def __init__(self, make, model , year , mileage,fuel_consumed):
        self.make = make
        self.model= model
        self.year = year 
        self.mileage = mileage
        self.fuel_consumed = fuel_consumed

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

    def get_info(self):
        return {
            'type': self.__class__.__name__,
            "Make": self.make,
            "Model": self.model,
            "Year": self.year,
            "Mileage": self.mileage,
            "Fuel consumed": self.fuel_consumed

        } 
    def calculate_fuel_efficiency(self):
        if self.fuel_consumed== 0:
            return 0
        return round (self.mileage/self.fuel_consumed,2)

    @abstractmethod 

    def estimate_maintenance_cost (self):
        pass

# Car Class


class Car(Vehicle):
    def estimate_maintenance_cost(self):
        return 200+ (self.get_age() * 50 )+ (self.mileage/10000*100)
    
#Truck
# 
class Truck(Vehicle):
    def estimate_maintenance_cost(self):
        return 500+ (self.get_age() * 100 )+ (self.mileage/10000*200)
        

class Motorcycle(Vehicle):
    def estimate_maintenance_cost(self):
        return 100+ (self.get_age() * 30 )+ (self.mileage/10000*50)
 
#Example 

def display_vehicle_report(vehicle):
    print(vehicle.get_info())
    print(vehicle.calculate_fuel_efficiency())
    print (round(vehicle.estimate_maintenance_cost(),2))

#sample
vehicles = [
    Car("Toyota", "Corolla", 2018, 50000, 3000),
    Truck("Volvo", "FH", 2015, 150000, 25000),
    Motorcycle("Yamaha", "R15", 2020, 20000, 800)
]

# Display reports
for v in vehicles:
    display_vehicle_report(v)