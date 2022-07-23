from mazda import Mazda
from bmw import BMW


if __name__=="__main__":
    pass

class Vehicle(object):
    def __init__(self,BMW,Mazda):
        self.BMWcar=BMW()
        self.Mazdacar=Mazda()
        
        
    def enginepower(self):
        if self.BMWcar.enginepower()>1900 and self.Mazdacar.enginepower()>1900:
            print("Engine power of BMW is 2000 and Mazda power is 22000")
        
        
        
    