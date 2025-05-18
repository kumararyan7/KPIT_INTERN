import random

class BatteryCell:
    def __init__(self,voltage,current,temperature,capacity):
        self.voltage = voltage
        self.current = current
        self.temperature = temperature
        self.capacity = capacity 
        self.charge=capacity
    
    def discharge(self,amount):
        self.charge = max(0,self.charge- amount)

    def charge_cell (self, amount ):
        self.charge= min (self.capacity,self.charge +amount)

    def get_soc (self):
        return round((self.charge/self.capacity)*100,2)
    
    def get_soh(self):
        nominal_capacity =100.00
        return round ((self.cpacity/nominal_capacity)*100,2)
    
class BMS:
    def __init__(self,cell:BatteryCell):
        self.cell = cell

    def monitor(self):
        return {
            self.cell.voltage,
            self.cell.current,
            self.cell.temperature,
            self.cell.get_soc(),
            self.cell.get_soh()
        }
    
    def temperature (self):
        if self.cell.temperature < -20:
            return "Heating req"
        elif self.cell.temperature>40:
            return "Cooling req"
        return "temp within safe range"    
    
    def safety_check(self) :
        alerts =[]
        if self.cell.voltage > 4.2:
            alerts.append("overcharge detected")
        return alerts
    
    def communicate (self):
        data = self.monitor()
        return f"Sending the data too vehicle unit :{data}"

# Example usage
cell = BatteryCell(voltage=random.uniform(3.0, 4.2),
                   current=random.uniform(0.5, 2.5),
                   temperature=random.uniform(-30, 50),
                   capacity=95.0)

bms = BMS(cell)

print("Battery Monitoring:", bms.monitor())
print("Temperature Control:", bms.temperature_control())
print("Safety Check:", bms.safety_check())
print("Communication:", bms.communicate())