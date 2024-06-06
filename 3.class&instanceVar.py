class Hero: # template
    #class variable
    jumlah = 0
    
    def __init__(self,inputName,inputHealth,inputdamage):
            #instance variable
        self.name = inputName
        self.health = inputHealth
        self.damage = inputdamage
        Hero.jumlah += 1 
        print("membuat hero dengan nama " +inputName)


hero1 = Hero("monkey king",200,100)
print(Hero.jumlah)
hero2 = Hero("sven",500,200)
print(Hero.jumlah)
hero3 = Hero("templar assassin",100,200)
print(Hero.jumlah)

