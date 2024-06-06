class Hero:

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name {}: \nhealth: {}".format(self.name,self.__health)
    
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None
axe = Hero('axe',100,10)

print("merubah info")
print(axe.info)
axe.name = "zeus"
print(axe.info)

print("\n" + "=" * 50 + "\n")

print("getter dan setter untuk __armor: ")
print(axe.armor)
print(axe.__dict__)
axe.armor = 10000
print(axe.armor)
del axe.armor
print(axe.__dict__)
