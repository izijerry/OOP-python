class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showinfo(self):
        print("{} dengan health: {}".format(self.name,self.health))


class Hero_intteligent(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        super().showinfo()
class Hero_strength(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        super().showinfo()

lina = Hero_intteligent("lina",100)
invoker = Hero_intteligent("invoker", 80)
axe = Hero_strength("axe",200)

