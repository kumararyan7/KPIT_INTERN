import random 

class BatteryCell:
    def __init__(self,voltage, current , temperature):
        self.voltage= voltage
        self.current = current 
        self.temperature = temperature

    def get_status(self):
        return{
        "voltage": self.voltage,
        "current ":self.current,
        "temperature": self.temperature,
    }

class BatteryPack:
    def __init__(self,num_cells):
        self.cells = [BatteryCell(random.uniform(3.5,4.2),
                                random.uniform(0,2.0),
                                random.uniform(25,40))
                     for _ in range(num_cells)]             
                      
    def total_voltage(self):
        return sum(cell.voltage for cell in self.cells)
    
    def average_current(self):
        return sum(cell.current for cell in self.cells)/len(self.cells)
    
    def max_temperature (self):
        return max(cell.temperature for cell in self.cells)
    
    def get_cells_status(self):
        return [cell.get_status() for cell in self.cells]

    def balance_cells(self):
        # Simplified voltage balancing logic
        avg_voltage = self.total_voltage() / len(self.cells)
        for cell in self.cells:
            if cell.voltage > avg_voltage + 0.05:
                cell.voltage -= 0.01  # simulate discharging
            elif cell.voltage < avg_voltage - 0.05:
                cell.voltage += 0.01  # simulate charging

class BMSSystem:
    def __init__(self,battery_pack):
        self.pack = battery_pack

    def monitor(self):
        print("Monitoring Battery Pack...")
        for idx, cell in enumerate(self.pack.get_cells_status(), 1):
            print(f"Cell {idx} - Voltage: {cell['voltage']:.2f}V, "
                  f"Current: {cell['current']:.2f}A, "
                  f"Temp: {cell['temperature']:.1f}°C")

    def control_charging_discharging(self, energy_demand_kw):
        if energy_demand_kw > 0:
            print(f"Discharging battery at {energy_demand_kw}kW.")
        else:
            print(f"Charging battery at {-energy_demand_kw}kW.")

    def thermal_management(self):
        max_temp = self.pack.max_temperature()
        if max_temp > 45:
            print("Warning: High battery temperature! Activating cooling system.")
        elif max_temp < 10:
            print("Warning: Low battery temperature! Activating heating system.")
        else:
            print("Battery temperature within optimal range.")

    def balance_cells(self):
        print("Balancing cells...")
        self.pack.balance_cells()
        print("Cells balanced.")

# Example Usage
def main():
    pack = BatteryPack(num_cells=6)
    bms = BMSSystem(pack)

    bms.monitor()
    bms.balance_cells()
    bms.control_charging_discharging(energy_demand_kw=30)  # Example demand
    bms.thermal_management()

if __name__ == "__main__":
    main()