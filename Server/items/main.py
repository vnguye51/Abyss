import json
from random import randint
import utils

class Item_Drop_Handler:
    def __init__(self):
        self.item_array = []
        self.id_assignment = 0
    
    def get_data(self):
        res = {}
        for item in self.item_array:
            res[item.id] = {
                "x": item.x,
                "y": item.y,
            }
        return res

    def instantiate(self,Item,x,y):
        self.item_array.append(Item(self.id_assignment,x,y))

class Item_Drop:
    def __init__(self,item_handler,id,x,y):
        self.item_handler = item_handler
        self.id = id
        self.x = x
        self.y = y

    def on_pickup(self,char):
        pass

class Gold(Item_Drop):
    item_id = 0
    name = "Gold"

    def __init__(self,item_handler,id,x,y,val):
        Item_Drop.__init__(self,item_handler,id,x,y)
        self.val = val
    
    def on_pickup(self,char):
        char.gold += self.val

class Small_Health_Potion(Item_Drop):
    item_id = 1
    name = "Health Potion"
    power = 1


