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
                "y": enemy.y,
                "frame": enemy.frame,
                "vfx" : enemy.vfx
            }
        return res

    def instantiate(self,Enemy,x,y, attack_handler):
        self.enemy_array.append(Enemy(x,y,self.id_assignment,attack_handler))
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
    def __init__(self,x,y,id,attack_handler):
        self.id = id
        self.hp = 5
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
        self.vfx_timer = 10
        self.invuln_to_attacks = []
        self.flag_for_removal = False
        self.attack_handler = attack_handler
        self.attack_handler.instantiate(GoblinAttack,self)

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
                if self.xvel > 0:
                    self.frame = 0
                elif self.xvel < 0:
                    self.frame = 2
                elif self.yvel > 0:
                    self.frame = 1
                else:
                    self.frame = 3
                self.timer = 60
        self.timer = max(0,self.timer-1)
        if self.vfx_timer > 0:
            self.vfx_timer = max(0,self.timer-1)
            if self.vfx_timer == 0:
                self.vfx = 0
        self.x += self.xvel
        self.y += self.yvel

        for attack in self.invuln_to_attacks:
            attack[1] = max(0,attack[1]-1)

        self.invuln_to_attacks = [attack for attack in self.invuln_to_attacks if attack[1] > 0]
            

        self.momentum = abs(self.xvel) + abs(self.yvel) + self.weight

        if self.hp <= 0:
            self.flag_for_removal = True

    def receive_attack(self,attack):
        if isinstance(attack,PlayerAttack):
            for invuln in self.invuln_to_attacks:
                if invuln[0] is attack:
                    return
            self.hp -= attack.atp
            self.overlay = 1
            self.vfx = 1
            self.vfx_timer = 15
            self.invuln_to_attacks.append([attack,15])
class Players:
    def __init__(self):
        self.player_array = []
    
    def get_data(self):
        res = {}
        for player in self.player_array:
            res[str(player.id)] = {
                "x": player.x,
                "y": player.y,
                "frame": player.frame
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
        self.frame = 0
        self.attacktimer = 5
        self.attack_handler = attack_handler
        self.prev_input = {}
        self.flag_for_removal = False

class Player(Character):
    def __init__(self,x,y,id,writer,attack_handler):
        Character.__init__(self,x,y,id,writer,attack_handler)
        self.hp = 10
        

    def player_input(self,input_map):
        if self.control:
            change_direction = True
            if input_map["left"]+input_map["right"]+input_map["down"]+input_map["up"] > 1:
                change_direction = False

            if input_map["left"] == 1:
                if change_direction:
                    self.direction = "W"
                    self.frame = 2
                self.xvel = -4
            elif input_map["right"] == 1:
                if change_direction:
                    self.direction = "E"
                    self.frame = 0
                self.xvel = 4
            else: 
                self.xvel = 0
            if input_map["up"] == 1:
                if change_direction:
                    self.direction = "N"
                    self.frame = 3
                self.yvel = -4
            elif input_map["down"] == 1:
                if change_direction:
                    self.direction = "S"
                    self.frame = 1
                self.yvel = 4
            else:
                self.yvel = 0
            if input_map["space"] == 1:
                self.attack()
        self.prev_input = input_map

    def attack(self):
        # self.control = False
        self.attack_handler.instantiate(PlayerAttack,self)

    def update(self):
        self.prev_x = self.x
        self.prev_y = self.y
        self.momentum = self.weight+abs(self.xvel)+abs(self.yvel)
        self.x += self.xvel
        self.y += self.yvel
        if self.hp <= 0:
            self.flag_for_removal = True


    def receive_attack(self,attack):
        if isinstance(attack,EnemyAttack):
            self.hp -= attack.atp


class Attacks:
    def __init__(self):
        self.attack_array = []
        self.id_assignment = 0
        self.sub_image = 0
        self.atp = 0

    def get_data(self):
        res = {}
        for attack in self.attack_array:
            res[str(attack.id)] = {
                "x": attack.x,
                "y": attack.y,
                "frame": attack.frame
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
        self.frame = -1

    def update(self):
        pass

class EnemyAttack(Attack):
    def update(self):
        pass

class GoblinAttack(EnemyAttack):
    def __init__(self,owner,id):
        EnemyAttack.__init__(self,owner,id)
        self.x = owner.x 
        self.y = owner.y
        self.width = owner.width
        self.height = owner.height
        self.atp = 2

    def update(self):
        self.x = self.owner.x 
        self.y = self.owner.y
        if self.owner.hp <= 0:
            self.flag_for_removal = True

class PlayerAttack(Attack):
    def __init__(self,owner,id):
        self.id = id
        if owner.direction == "E":
            self.frame = 1
            offset_x = 16
            offset_y = -2
        elif owner.direction == "S":
            self.frame = 0
            offset_x = 2
            offset_y = 16
        elif owner.direction == "W":
            self.frame = 1
            offset_x = -16
            offset_y = 2
        else:
            self.frame = 0
            offset_x = -2
            offset_y = -16
        self.x = owner.x + offset_x
        self.y = owner.y + offset_y
        self.width = 8
        self.height = 12
        self.owner = owner
        self.flag_for_removal = False
        self.timer = 15
        self.atp = 1

    def update(self):
        self.timer = max(0,self.timer-1)
        if self.timer == 0:
            self.flag_for_removal = True
        
        
