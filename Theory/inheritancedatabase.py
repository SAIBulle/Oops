import pymysql

# Function to create a MySQL connection
def create_connection():
    try:
        # Update the following details with your MySQL server information
        con = pymysql.connector.connect(host="localhost", user="root", password="oracle", database="saidb")
        cursor = con.cursor()
        cursor.execute("create table vehical (id int auto_increment primary key, make varchar(255) not null, model varchar(20) not null, year int not null, mileage int, fuel_type varchar(15))")
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

            query="insert into vechicles1(id,make,model,year,mileage) VALUSE(%s,%s,%s,%s,%s))"

        class Car(Vehical):
            Registration_format = "CARXX00XX0000"
            def __init__(self, Fuel_type, Transmission_type, Make, Year, Mileage):
                super().__init__(Make, Year, Mileage)
                self.fuel_type = Fuel_type
                self.transmission_type = Transmission_type
                cursor.execute("create table car(Fuel_type varchar(10), Transmission_type varchar(20), Make varchar(20), Year int, Mileage varchar(10)")

       
            def calculate_tax(self):
                return 0.05 * self.year
            def calculate_insurance_premium(self):
                return 500 + 0.01 * self.mileage
            
            query="insert into vechicles1(Fuel_type, Transmission_type, Make, Year, Mileage) VALUSE(%s,%s,%s,%s,%s))"


    except pymysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    car1 = Car("Petrol", "Passinger", "Tyota", 2024, 2500)
    car2 = Car("EV", "Personal", "Honda", 2023, 3500)
    print(car1.calculate_maintenance_cost())
    print(car2.calculate_maintenance_cost())
    print(car1.calculate_tax())
    print(car1.calculate_insurance_premium())
    Vehical1 = Vehical("Honda", "2023", 2500)
    Vehical1.display_info()