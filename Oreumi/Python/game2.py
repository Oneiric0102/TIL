class magician:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def skill(self):
        print(f"magician skill {self.level} activate!")
    
    def level_up(self):
        self.level+=1
        print("magician level up!!!")

class worrior:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def skill(self):
        print(f"worrior skill {self.level} activate!")
    
    def level_up(self):
        self.level+=1
        print("worrior level up!!!")

oreumi_1 = magician("est")
oreumi_2 = worrior("soft")

oreumi_1.skill()
oreumi_2.skill()
print("{}, now level ={}".format(oreumi_1.name, oreumi_1.level))
oreumi_1.level_up()
print("{}, now level ={}".format(oreumi_1.name, oreumi_1.level))
oreumi_1.skill()