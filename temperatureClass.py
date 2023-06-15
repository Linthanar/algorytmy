class Celsius():
    # def __init__(self):
    #     self = self


    def __init__(self,height,temperature = 0):
        self.temperature = temperature 
        self.height = height

    def toFar(self):
        
        self.temperature = float((9 * self.temperature) / 5 + 32)
    def FarAway(self):
        self.temperature =  float((self.temperature-32)*5/9)
# class init
human = Celsius(150,37)
human.toFar()
print(human.temperature)
human.FarAway()


# human.temperature = 37

# print(human.height)
print(human.temperature)