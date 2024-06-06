class Hero:
#class variable 
    jumlah_hero = 0 

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #insatance variable 
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    #void function, method tanpa return, tanpa argumen
    def siapa(self):
        print('namaku ' + self.name)

    #method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up
        
    #mehtod dengan return
    def getHalth(self):
        return self.health


hero1 = Hero('lesley',100,10,5)
hero2 = Hero('dyroth',130,10,5)
hero3 = Hero('vale',100,5,10)

hero1.siapa()
hero2.healthUp(10)

print(hero2.getHalth())


