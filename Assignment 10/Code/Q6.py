class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        
    def charge(self, percent):
        self.battery_percentage = self.battery_percentage + percent
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print("Charged phone. Battery now at", self.battery_percentage, "%")
        
    def use_phone(self, minutes):
        drain = minutes // 10 
        self.battery_percentage = self.battery_percentage - drain
        if self.battery_percentage < 0:
            self.battery_percentage = 0
        print("Used phone for", minutes, "minutes. Battery now at", self.battery_percentage, "%")
        
    def show_status(self):
        print("Phone:", self.brand, self.model, "Battery:", self.battery_percentage, "%")

phone = MobilePhone("Apple", "iPhone 13", 50)
phone.show_status()
phone.use_phone(30)
phone.charge(20)