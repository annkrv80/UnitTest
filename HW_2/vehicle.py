
class Vehicle:
    def __init__(self,company:str, model:str, yearRelease:int, numWheel=0 ,speed=0):
        self.company = company
        self.model = model
        self.yearRelease = yearRelease
        self.numWheel = numWheel
        self.speed = speed

    def testDrive(self):
        pass
        
    def park(self):
        pass

    def __repr__(self):
        return f"Транспортное средство {self.company}, '{self.model}', {self.yearRelease}, {self.numWheel},{self.speed}"
    
class Car(Vehicle):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numWheel = 4   
             
        


    def testDrive(self):
        speed_drive = 60
        self.speed = speed_drive
        
    def park(self):
        speed_parking = 0
        self.speed = speed_parking
    
class Motorcycle(Vehicle):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numWheel = 2   
           
        

    def testDrive(self):
        speed_drive = 75
        self.speed = speed_drive
        
    def park(self):
        speed_parking = 0
        self.speed = speed_parking      

