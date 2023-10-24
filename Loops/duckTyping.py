def Driver(car):
    car.drive()
    
class Creta:
    def drive(self):
        print('Creta is driving')
    
class Ciaz:
    def drive(self):
        print('Ciaz is driving')
        
c1 = Creta()
c2 = Ciaz()
Driver(c1)
Driver(c2)