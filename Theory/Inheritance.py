# multilevel inheritance

# class Animal:
#     def eat(self):   
#         print(f"This animal eats food")
# class dog(Animal):
#     def bark(self):
#         print(f"Dog eat and bark")
# class frog(dog):
#     def swim(self):
#         print(f"Frog swim in the water jump in the land")

# animal1 = frog()
# animal1.bark()
# animal1.swim()
# animal1.eat()

class Vehical:
    Registration_format = "XX00XX0000"
    Total_count = 0
    def __init__(self, Make, Year, Mileage):
        self.make = Make
        self.year = Year
        self.mileage = Mileage
        Vehical.Total_count += 1
    def get_make(self):
        return self.make
    def get_model(self):
        return "Model is Now avilable"
    def get_year(self):
        return self.year
    def update_mileage(self):
        return self.mileage
    def calculate_maintenance_cost(self):
        return 100 + 0.1 * self.mileage
    
    def display_info(self):
        print(f"Make : {self.make}")
        print(f"Year : {self.year}")
        print(f"Mileage : {self.mileage} miles")

    @staticmethod
    def validate_registration(Registration_format):
        return Registration_format == "XX00XX0000"

    @classmethod
    def get_total_count(cls):
        return cls.Total_count

class Car(Vehical):
    Registration_format = "CARXX00XX0000"
    def __init__(self, Fuel_type, Transmission_type, Make, Year, Mileage):
        super().__init__(Make, Year, Mileage)
        self.fuel_type = Fuel_type
        self.transmission_type = Transmission_type
    def calculate_tax(self):
        return 0.05 * self.year
    def calculate_insurance_premium(self):
        return 500 + 0.01 * self.mileage

class Truck(Vehical):
    Registration_format = "TRKXX00XX0000"
    def __init__(self, Load_capacity, Fuel_efficiency,Make, Year, Mileage):
        super().__init__(Make, Year,Mileage)
        self.load_capacity = Load_capacity
        self.fuel_efficiency = Fuel_efficiency
    def calculate_fuel_cost(self):
        return 2 * self.load_capacity / self.fuel_efficiency
    
    def calculate_depreciation(self):
        return 1000 + 0.05 * self.mileage
    
class Motorcycle(Vehical):
    Registration_format = "MCXXX00XX0000"
    def __init__(self, Engine_capacity, Fuel_capacity,Make, Year, Mileage):
        super().__init__(Make, Year, Mileage)
        self.engine_capacity = Engine_capacity
        self.fuel_capacity = Fuel_capacity
    def check_engine_status(self):
        return "Engine is Good condition"
    def calculate_acceleration(self):
        return 10 * self.engine_capacity
    
class Bicycle(Vehical):
    Registration_format = "BICXX00XX0000"
    def __init__(self, Frame_material, Tire_size, Make, Year, Mileage):
        super().__init__(Make, Year, Mileage)
        self.frame_material = Frame_material
        self.tire_size = Tire_size
    def check_tire_pressure(self):
        return "All tire pressure is good condition"
    def calculate_speed(self):
        return 15 * self.tire_size
    


car1 = Car("Petrol", "Passinger", "Tyota", 2024, 2500)
car2 = Car("EV", "Personal", "Honda", 2023, 3500)
print(car1.calculate_maintenance_cost())
print(car2.calculate_maintenance_cost())
print(car1.calculate_tax())
print(car1.calculate_insurance_premium())
Vehical1 = Vehical("Honda", "2023", 2500)
Vehical1.display_info()

print(Car.get_total_count())