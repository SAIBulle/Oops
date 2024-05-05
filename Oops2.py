class Person():
    def __init__(self, name, sex, Aadhar, profession, study, work):
        self.name = name
        self.sex = sex
        self.aadhar = Aadhar
        self.profession = profession
        self.study = study
        self.work = work

    def display_personal_info(self):
        print("Name: ", self.name)
        print("Gender: ", self.sex)
        print("Aadhar: ", self.aadhar)
        print("Profession: ", self.profession)
        print("Studying: ", self.study)
        print("Work : ", self.work)
p1 = Person('SAI', 'Male', 987456321012,'Software Engineer', 'CSE', 'He works in one company XYZ company')
p1.display_personal_info()
print()
print("`~"*10)
print()
p2= Person('RAJU', 'Male', 789456321032, 'Software Engineer', 'CSE', 'He works in one company ABC company')
p2.display_personal_info()