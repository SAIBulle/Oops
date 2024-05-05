class Laptop():
    Name = "Electronic"
    def __init__(self, Divce_name, Ram, Disk_type, Disk_size, Display_type, Display_size, Drivers, Model_name, Processer, Graphic_card, Screen_type, Battery_type):
        self.divce_name = Divce_name
        self.ram = Ram
        self.disk_type = Disk_type
        self.disk_size = Disk_size
        self.display_type = Display_type
        self.display_size = Display_size
        self.drivers = Drivers
        self.model_name = Model_name
        self.processer = Processer
        self.graphic_card = Graphic_card
        self.screen_type = Screen_type
        self.battery_type = Battery_type
    def get_divce_name(self):
        print(f"The {self.Name} divce name is : {self.divce_name}")
    def get_ram(self):
        print(f"The Divce ram is : {self.ram}")
    def get_disk_type(self):
        print(f"The disk type is : {self.disk_type}")
    def get_disk_size(self):
        print(f"The Disk size : {self.disk_size}")
    def get_display_type(self):
        print(f"Dispaly type is : {self.display_type}")
    def get_display_size(self):
        print(f"Display Size is : {self.display_size}")
    def get_drivers(self):
        print(f"The {self.divce_name} drivers is : {self.drivers}")
    def get_model_name(self):
        print(f"The {self.divce_name} model name is : {self.model_name}")
    def get_processer(self):
        print(f"The {self.divce_name} processer is : {self.processer}")
    def get_graphic_card(self):
        print(f"The {self.graphic_card} graphic card is : {self.graphic_card}")
    def get_screen_type(self):
        print(f"The {self.divce_name} screen type is : {self.screen_type}")
    def get_battery_type(self):
        print(f"The {self.divce_name} battery type is : {self.battery_type}")

electronic = Laptop("Lenovo", "16GB", "SSD", "520TB", "Qled", "15 inchs", "Lenovo drivers", "ideapad 3 slim 3", "intel core i5", "intel iRISxe", "No touch", "In-Built")
electronic.get_divce_name()
electronic.get_ram()
electronic.get_disk_type()
electronic.get_disk_size()
electronic.get_display_type()
electronic.get_display_size()
electronic.get_drivers()
electronic.get_model_name()
electronic.get_processer()
electronic.get_graphic_card()
electronic.get_screen_type()
electronic.get_battery_type()

print()
print("`~"*10)
print()

electronic1 = Laptop("HP", "8GB", "SSD", "1TB", "Qled", "12 inchs", "HP Drivers", "Pavalin", "intel core i5", "intel Graphics", "Touch", "In-Built")
electronic1.get_divce_name()
electronic1.get_ram()
electronic1.get_disk_type()
electronic1.get_disk_size()
electronic1.get_display_type()
electronic1.get_display_size()
electronic1.get_drivers()
electronic1.get_model_name()
electronic1.get_processer()
electronic1.get_graphic_card()
electronic1.get_screen_type()
electronic1.get_battery_type()