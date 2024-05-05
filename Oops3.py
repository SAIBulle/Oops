class Bank():
    Bank_name = "State bank of India"
    def __init__(self, Branch, Accno, Balance, Custid, IFC, Name, Address, Phoneno, Email, Debit, Credit, Tranctions, Accounttype):
        self.Branch = Branch
        self.Accno = Accno
        self.Balance = Balance
        self.Custid = Custid
        self.IFC = IFC
        self.Name = Name
        self.Address = Address
        self.Phoneno = Phoneno
        self.Email = Email
        self.Debit = Debit
        self.Credit = Credit
        self.Tranctions = Tranctions
        self.Accounttype = Accounttype
        
    def get_branch(self):
        print("~`"*8, f"{self.Bank_name}","~`"*8)
        print(f"Bank branch is: {self.Branch}")
    def get_accno(self):
        print(f"Account number is: {self.Accno}")
    def get_balance(self):
        print(f"Account Balance is: {self.Balance}")
    def get_custid(self):
        print(f"Custom Id is: {self.Custid}")
    def get_ifc(self):
        print(f"Banl ifc code is: {self.IFC}")
    def get_name(self):
        print(f"Customer name is: {self.Name}")
    def get_address(self):
        print(f"Customer address is: {self.Address}")
    def get_phone(self):
        print(f"Customer Phone number: {self.Phoneno}")
    def get_email(self):
        print(f"Customer email id is: {self.Email}")
    def get_debit(self):
        print(f"Amount debit {self.Debit} from the account to account {self.Accno}")
    def get_credit(self):
        print(f"Amount credited {self.Credit} to the account")
    def get_tranctions(self):
        print(f"Tracton Type {self.Tranctions} fund transfer")
    def get_acctype(self):
        print(f"Account type: {self.Accounttype}")
                  


B1 = Bank("ATP", "235689741", 40000, "231564897", "SBI2356", "SAI", "PLK", "9874563210", "sai@gmail.com", "2000/-", "25000/-", "Instant", "savings")
B1.get_branch()
B1.get_accno()
B1.get_balance()
B1.get_custid()
B1.get_ifc()
B1.get_name()
B1.get_address()
B1.get_phone()
B1.get_email()
B1.get_debit()
B1.get_credit()
B1.get_tranctions()
B1.get_acctype()