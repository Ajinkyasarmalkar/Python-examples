class Vehical:
    def __init__(self, cost, milage):
        self.cost = cost
        self.milage = milage

    def Vehical_details(self):
        print("cost of vehical is:", self.cost)
        print("milage of vehical is:", self.milage)

class Car(Vehical):
    # def __init__(self, model, color):
    #     self.model = model
    #     self.color = color

    def car_details(self):
        print("This is an Audi")



# Vehical1 = Vehical(500, 100)    
# Vehical1.Vehical_details()    


car1 = Car("2000 $", "400")
car1.car_details()
car1.Vehical_details()

           

