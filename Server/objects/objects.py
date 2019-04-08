import json
from random import randint
import utils

class Enemies:
    def __init__(self):
        self.enemy_array = []
        self.id_assignment = 0

    def get_data(self):
        res = {}
        for enemy in self.enemy_array:
            res[str(enemy.id)] = {
                "name": enemy.name,
                "x": enemy.x,
                "y": enemy.y
            }
        return res

    def instantiate(self,Enemy,x,y):
        self.enemy_array.append(Enemy(x,y,self.id_assignment))
        self.id_assignment += 1

class Enemy: 
    def __init__(self,x,y,id):
        self.id = id
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.pos_lock = False
        self.width = 16
        self.height = 16

class Goblin(Enemy):
    def __init__(self,x,y,id):
        self.id = id
        self.name = "GoblinObj"
        self.x = x
        self.y = y
        self.prev_x=0
        self.prev_y=0
        self.xvel = 0
        self.yvel = 0
        self.pos_lock = False
        self.width = 16
        self.height = 16
        self.timer = 0
        self.pattern = 1
        self.momentum = 999
        self.weight = 10

    def collide(self):
        pass

    def update(self):
        self.xvel = 0
        self.yvel = 0
        self.prev_x = self.x
        self.prev_y = self.y
        # if self.pattern == 1:
        #     if self.timer == 0:
        #         self.timer = 30
        #         self.xvel = 0
        #         self.yvel = 0
        #         self.pattern = 2
        # else:
        #     if self.timer == 0:
        #         self.pattern = 1
        #         self.xvel = 1*randint(-1,1)
        #         self.yvel = 1*randint(-1,1)
        #         self.timer = 60
        # self.timer = max(0,self.timer-1)
        self.x += self.xvel
        self.y += self.yvel
        self.momentum = abs(self.xvel) + abs(self.yvel) + self.weight

class Players:
    def __init__(self):
        self.player_array = []
    
    def get_data(self):
        res = {}
        for player in self.player_array:
            res[str(player.id)] = {
                "x": player.x,
                "y": player.y
            }
        return res

class Character:
    def __init__(self,x,y,id,writer):
        self.x = x
        self.prev_x = 0
        self.y = y 
        self.prev_y = 0
        self.xvel = 0
        self.yvel = 0
        self.momentum = 0
        self.weight = 1
        self.pos_lock = False
        self.width = 16
        self.height = 16
        self.id = id
        self.writer = writer
        self.direction = "N" #NSWE cardinal directions

class Player(Character):
    def attack(self):
        pass

    def collide(self, obj):
        pass

    def player_input(self,input_map):
        if input_map["left"] == 1:
            self.xvel = -4
        elif input_map["right"] == 1:
            self.xvel = 4
        else: 
            self.xvel = 0
        if input_map["up"] == 1:
            self.yvel = -4
        elif input_map["down"] == 1:
            self.yvel = 4
        else:
            self.yvel = 0

        if input_map["space"] == 1:
            self.attack()
