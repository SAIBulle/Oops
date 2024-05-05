class Bike():
    Company_name = "Hero"
    def __init__(self, Bike_name, Model_name, Brike_type, Disk, Engine_capacity, Mileage, Fual_tank_capacity, Fual_type, Color):
        self.bike_name = Bike_name
        self.model_name = Model_name
        self.brike_type = Brike_type
        self.disk = Disk
        self.engine_capacity = Engine_capacity
        self.mileage = Mileage
        self.fual_tank_capacity = Fual_tank_capacity
        self.fual_type = Fual_type
        self.color = Color
    
    def get_bike_name(self):
        print(f"The company name is {self.Company_name} bike name is {self.bike_name}")
    def get_model_name(self):
        print(f"The Model name is {self.model_name}")
    def get_brike_type(self):
        print(f"The brike type {self.brike_type}")
    def get_disk(self):
        print(f"The Disk is {self.disk}")
    def get_engine_capacity(self):
        print(f"The Engine capacity is {self.engine_capacity}")
    def get_mileage(self):
        print(f"Bike Mileage is {self.mileage}")
    def get_fual_tank_capacity(self):
        print(f"The fual tank capacity is {self.fual_tank_capacity}")
    def get_fual_type(self):
        print(f"The fual type is {self.fual_type}")
    def get_color(self):
        print(f"The bike color is {self.color}")

bike = Bike("Hero Splender Plus", "Bs6", "Drum type", "Not present", "92.cc", "60kmpl", "9.2L", "Petrol", "Blue Black")

bike.get_bike_name()
bike.get_model_name()
bike.get_brike_type()
bike.get_disk()
bike.get_engine_capacity()
bike.get_mileage()
bike.get_fual_tank_capacity()
bike.get_fual_type()
bike.get_color()