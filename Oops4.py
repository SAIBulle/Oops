class super_market():
    Name = "Village mart"

    def __init__(self, kitchen, electronics, vegtables, fruits):
        self.kitchen = kitchen
        self.electronics = electronics
        self.vegtables = vegtables
        self.fruits = fruits
    def name(self):
        print("`~"*8,self.Name,"`~"*8)
    def get_kitchen(self):
        print(f"Kitchen items: {self.kitchen}")
    def get_electronics(self):
        print(f"Electronics avalible in the market: {self.electronics}")
    def get_vegtables(self):
        print(f"Fresh Vegtables available in the market: {self.vegtables}")
    def get_fruits(self):
        print(f"Fresh fruits available in the market: {self.fruits}")

market1 = super_market("Mixers", "Tv, Fan, Home, theater", "tomato, chilly", "Apple, Banana, Orange")
market1.name()
market1.get_kitchen()
market1.get_electronics()
market1.get_vegtables()
market1.get_fruits()
print()
print("`~"*10)
print()