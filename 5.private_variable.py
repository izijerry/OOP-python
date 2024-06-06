class Hero:
    #class variable
    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health,attack):
        self.name = name
        self.health = health 
        self.attack = attack

        #variable instance private 
        self.__private = "private"
        #variable instance protected 
        self._protected = "protected"

lina = Hero("lina",100,10)

print(lina.__dict__)
print("\n")
print(Hero.__dict__)