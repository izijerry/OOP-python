class Hero:
    #private class vairable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
        
    #method ini hanya berlaku untuk objek
    def getjumlah(self):
        return Hero.__jumlah
    #method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah1():
        return Hero.__jumlah
    #method static (decorator) nempel ke objek dan class
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah


layla = Hero('layla')
melisa = Hero('melisa')
lesley = Hero('lesley')

print(Hero.getjumlah3())
print(Hero.getjumlah2())