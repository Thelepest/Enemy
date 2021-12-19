class Enemy:
    def __init__(self,lifepoints=10,strength=10):
        self.lifepoints = lifepoints
        self.strength = strength
        self.attack = 10*strength

class Skeleton(Enemy):
    def __init__(self,lifepoints,strength,attack):
        super().__init__(lifepoints,strength,attack)
    
    def Scream():
        return("All enemies ran away!")

class Dragon(Enemy):
    def __init__(self,lifepoints,strength,attack):
        super().__init__(lifepoints,strength,attack)
    
    def Flyaway():
        return("You escaped from the battlefield!")
