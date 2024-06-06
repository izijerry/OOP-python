class Hero:
    #private class variable 
    __jumlah = 0

    def __init__(self,name,health,attdamage,armor):
        self.__name = name
        self.__healthstandar = health
        self.__attdamagestandar = attdamage
        self.__armorstandar = armor
        self.__exp = 0
        self.__level = 1

        self.__healthmax = self.__healthstandar*self.__level
        self.__attmax = self.__attdamagestandar*self.__level
        self.__armor = self.__armorstandar*self.__level

        self.__health = self.__healthmax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{}\n\tattack = {}\n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthmax,self.__attmax,self.__armor)
    
    @property
    def gainExp():
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1 
            self.__exp -= 100

            self.__healthmax = self.__healthstandar*self.__level
            self.__attmax = self.__attdamagestandar*self.__level
            self.__armor = self.__armorstandar*self.__level

    def attack(self, musuh):
        self.gainExp = 50

zeus = Hero("zeus", 100, 5, 10)
invoker = Hero("invoker", 100,5 , 20)
print(zeus.info)

zeus.attack(invoker)
zeus.attack(invoker)
zeus.attack(invoker)
print(zeus.info)