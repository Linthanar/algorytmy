
class Human: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print('I\'m',self.name,'I\'m',self.age)

class Druid(Human):
    def __init__(self,name,age,mana):
        super().__init__(name,age)
        self.mana = mana
    def useHeal(self):
        print(self.name, 'healing...')

class Warior(Human):
    def __init__(self,name,age,damage):
        self.name = name
        self.age = age
        self.damage = damage
    
    def cut(self):
        print(self.name,'cuting...',self.damage)

hum1 = Human('Jakub',71)
hum1 = Druid('Jakub',71,25)
# print(hum2.mana)
hum1.intro()
hum1.useHeal()

hum2 = Warior('Geralt',50,999)

hum2.intro()
hum2.cut()
