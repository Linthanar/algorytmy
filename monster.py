class Monster():
    
    def __init__(self,hp,sr):
        self.hp = hp
        self.sr = sr

    def __str__(self):
        return str(self.hp)

    def setHp(self, hp):
        self.hp += hp

    def getHp(self):
        return self.hp
        
    # def attack(self):
    #     demage = 
    #     self.setHp(demage)
    #     pass


spider = Monster(30,10)
skeleton = Monster(4,90)
print('spider hp', spider)

print('drinking potion...')
spider.setHp(10)
print('spider hp',spider)

print('getter hp',spider.getHp())


# spider.setHp(-skeleton.sr)

if spider.hp < skeleton.hp:
    print('skeleton has more hp', skeleton.hp)
else:
    print('spider has more hp', spider.hp)