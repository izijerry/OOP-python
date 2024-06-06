class Hero: 

    def __init__(self,name,health,attack):
        self.__name = name
        self.__health = health
        self.__attack = attack 
    
    #getter 
    def gethealth(self):
        return self.__health
    
    def getname(self):
        return self.__name
    
    #setter
    def diserang(self,attackpower):
        self.__health -= attackpower
    
    def power(self,nilai):
        self.__attack = nilai
#awal dari game 
invoker = Hero("invoker",100,10)

#game berjalan
print(invoker.getname())
print(invoker.gethealth())
invoker.diserang(10)
print(invoker.gethealth())
