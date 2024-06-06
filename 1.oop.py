class Hero: # template
    pass


hero1 = Hero() # object / instance
hero2 = Hero()
hero3 = Hero()

hero1.Name = "Sniper"
hero1.Health = 200

hero2.Name = "Marci"
hero2.Health = 500

hero3.Name = "Phantom Assassin"
hero3.Health = 300

print(hero1)
print(hero1.__dict__)
print(hero1.Name)
print(hero1.Health)