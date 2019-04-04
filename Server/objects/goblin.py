from .objects import Enemy
from random import randint

class Goblin(Enemy):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.busy = False
        self.busy_timer = 0
        
    def update(self):
        if self.busy == False:
            self.busy_timer = 90
            self.xvel = 4 if randint(0,1) else 0
            self.yvel = 4 if randint(0,1) else 0
        else:
            self.busy_timer -= 1
            if self.busy_timer == 0:
                self.busy = False
                self.busy_timer = 90