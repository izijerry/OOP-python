class Hero: 
    def __init__(self, name, health):
        self.name = name 
        self.health = health 

    def showinfo(self):
        print("{} dengan health {}". format(self.name, self.health))

class hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        super().showinfo()

class hero_strength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 100)
        super().showinfo()
        

lina = hero_intelligent('lina')
axe = hero_strength('axe')

