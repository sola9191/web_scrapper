class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def sleep(self):
        print("zzzzzzz........")

class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, age=5)
        self.aggressive = True
    
    def rrr(self):
        print("stay away!")

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, age=1)
        self.aggresive = False

    def woof_woof(self):
        print("Woof Woof!")
    
    def introduce(self):
        self.woof_woof()
        print(f"my name is {self.name} and I'm a baby {self.breed}")
    
happy = Puppy("Happy", "Beagle")
bibi = GuardDog("Bibi", "Dalmatian")

print(happy.name, happy.aggresive)
print(bibi.name, bibi.aggressive)
happy.introduce()
happy.sleep()
bibi.sleep()