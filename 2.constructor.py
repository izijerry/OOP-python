# hero1 == self

class Hero: # template
    
    def __init__(self,inputName,inputHealth,inputdamage):
        self.name = inputName
        self.health = inputHealth
        self.damage = inputdamage


hero1 = Hero("monkey king",200,100)
hero2 = Hero("sven",500,200)
hero3 = Hero("templar assassin",100,200)

print(hero1.name,hero1.health,hero1.damage)
print(hero2.name,hero2.health,hero2.damage)
print(hero3.name,hero3.health,hero3.damage)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)