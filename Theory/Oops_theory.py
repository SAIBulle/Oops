
'''
student
'''

class Student:
    #static variable
    college_name = "ssbn degree college"
    # define constructor
    def __init__(self, name, roll_no, std_id, country, age):
        self.name = name
        self.roll_no = roll_no
        self.std_id = std_id
        self.country = country
        self.age = age
    # methods
    def get_student_details(self):
        print(f"Student name is {self.name} and the roll number is {self.roll_no} and the student id {self.std_id} and the class {self.country}")
    @staticmethod    
    def stud_validity():
        age = student1.age 
        if age>18:
            print("your elgible to study in college")
        else:
            print("NOt elgible to study in the college")


# object creation
student1 = Student("sai",'Abc123', "SSbn123", "A-4567", 19)
student1.get_student_details()
student1.stud_validity()  