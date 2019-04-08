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

    def hurt(self,atp):
        print("i'm hit!")
        pass

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
        # self.xvel = 0
        # self.yvel = 0
        self.prev_x = self.x
        self.prev_y = self.y
        if self.pattern == 1:
            if self.timer == 0:
                self.timer = 30
                self.xvel = 0
                self.yvel = 0
                self.pattern = 2
        else:
            if self.timer == 0:
                self.pattern = 1
                self.xvel = 1*randint(-1,1)
                self.yvel = 1*randint(-1,1)
                self.timer = 60
        self.timer = max(0,self.timer-1)
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
    def __init__(self,x,y,id,writer,attack_handler):
        self.control = True
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
        self.attacktimer = 5
        self.attack_handler = attack_handler

class Player(Character):
    def collide(self, obj):
        pass

    def player_input(self,input_map):
        if self.control:
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

    def attack(self):
        # self.control = False
        self.attack_handler.instantiate(PlayerAttack,self)

    def update(self):
        self.prev_x = self.x
        self.prev_y = self.y
        self.momentum = self.weight+abs(self.xvel)+abs(self.yvel)
        self.x += self.xvel
        self.y += self.yvel

class Attacks:
    def __init__(self):
        self.attack_array = []
        self.id_assignment = 0

    def get_data(self):
        res = {}
        for attack in self.attack_array:
            res[str(attack.id)] = {
                "x": attack.x,
                "y": attack.y
            }
        return res

    def instantiate(self,Attack,owner):
        self.attack_array.append(Attack(owner,self.id_assignment))
        self.id_assignment += 1

class Attack:
    def __init__(self,owner,id):
        self.id = id
        self.owner = owner
        self.flag_for_removal = False
    
    def collide(self,obj):
        pass
    def update(self):
        pass
class PlayerAttack(Attack):
    def __init__(self,owner,id):
        self.id = id
        self.x = owner.x - 2
        self.y = owner.y + 12
        self.width = 8
        self.height = 12
        self.owner = owner
        self.flag_for_removal = False
        self.timer = 30

    # def collide(self,obj):
    #     if isinstance(obj,Enemy):
    #         obj.hurt(1)

    def update(self):
        self.timer = max(0,self.timer-1)
        if self.timer == 0:
            self.flag_for_removal = True
        
        
