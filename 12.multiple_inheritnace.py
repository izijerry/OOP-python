'''multiple inheritance'''
# class A:
#     def method_A(self):
#         print("method A")

# class B:
#     def method_B(self):
#         print("method B")


# class tes(A,B):
#     pass

# objek = tes()

# objek.method_A()
# objek.method_B()

'''contoh'''

class team:
    def setTeam(self, team):
        self.team = team

    def showteam(self):
        print(self.team)

class tipe_hero:
    def setTipe_hero(self, tipe_hero):
        self.tipe_hero = tipe_hero

    def showTipe_hero(self):
        print(self.tipe_hero)
   

class Hero(team, tipe_hero):
    def __init__(self, name, health):
        self.name = name
        self.health = health

qop = Hero("qop", 100)
qop.setTeam("dire")
qop.setTipe_hero("intelligence")

qop.showteam()
qop.showTipe_hero()