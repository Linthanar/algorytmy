class Counter():
    def __init__(self):
        self.number = 0

    def add(self, number):
        self.number = (self.number + number) % 10

        if number % 2 == 0:
            print(" {} Fizz".format(self.number))
        else:
            print(" {} Buzz".format(self.number))

    def reset(self):
        self.number = 0
        print(" {} reset".format(self.number))

myCounter = Counter()
myCounter.number = 0

myCounter.add(4) 
myCounter.add(1) 
myCounter.reset()
myCounter.add(4) 
myCounter.add(1) 
myCounter.add(4) 
myCounter.add(1) 