
class Employee():
    company_name = "Tcs company" # Static Variable
    def __init__(self, EName, Eid, Enumber, Eaddress, Esalary, Department): # Instance Variable
        self.ename = EName         
        self.eid = Eid
        self.enumber = Enumber
        self.eaddress = Eaddress
        self.esalary = Esalary
        self.department = Department
    def get_name(self):
        print(f"Employee Name is: {self.ename}")
    def get_eid(self):
        print(f"Employee Id is: {self.eid}")
    def get_number(self):
        print(f"Employee Number is: {self.enumber}")
    def get_address(self):
        print(f"Employee Address is: {self.eaddress}")
    def __get_salary(self):
        print(f"Employee salary is: {self.esalary}")
    def get_company_name(self):
        print(f"Employee Company Name is: {self.company_name}")
    def get_department(self):
        print(f"Employee Department is: {self.department}")
Employee1 = Employee("Sai","ABC123",7894563210,"ATP, D, M",30000, "IT")
Employee2 = Employee("Raju","ABC124",9874563210,"ATP,D,M",35000, "IT")

Employee1.get_name()
Employee1.get_eid()
Employee1.get_number()
Employee1.get_address()
getattr(Employee1,'_Employee__get_salary')()
Employee1.get_company_name()
Employee1.get_department()
print()
print("~`"*20)
print()
Employee2.get_name()
Employee2.get_eid()
Employee2.get_number()
Employee2.get_address()
getattr(Employee2,'_Employee__get_salary')()
Employee2.get_company_name()
Employee2.get_department()