"""
def create_player(name, xp, team):
    return  {
    "name" : name,
    "XP" : xp,
    "team" : team
}
def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

sola = create_player("sola", 10000, "samsung")
lynn = create_player("lynn", 10000, "LG")
"""
class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed

    def sleep(self):
        print("zzzzzzz........")

class GuardDog(Dog):

    def __init__(self, name, breed):
        super().__init__(name, breed, age=5)
        self.aggresive = True
    
    def rrr(self):
        print("stay away!")


class Puppy(Dog) :

    def __init__(self, name, breed):
        super().__init__(name, breed, age=0.1)
        self.aggresive = False

    def __str__(self): # 자동으로 호출
        return f"{self.breed} puppy named {self.name} "
    
    def woof_woof(self):
        print("Woof Woof!")
    
    def introduce(self):
        self.woof_woof()
        print(f"My name is {self.name} and I am a baby {self.breed}")
        self.woof_woof()
    
ruffus = Puppy(name = "Ruffus", breed = "Beagle")
bibi = GuardDog(name = "Bibi", breed = "Dalmatian")
print(ruffus.name, ruffus.age, ruffus.aggresive)
print(bibi.name, bibi.age, bibi.aggresive)
ruffus.sleep()
bibi.sleep()
