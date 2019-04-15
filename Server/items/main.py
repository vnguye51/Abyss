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
                "name": item.name
            }
        return res

    def instantiate(self,Item,x,y,val=None):
        self.item_array.append(Item(self,self.id_assignment,x,y,val))

class Item_Drop:
    item_id = -1
    name = "N/A"
    def __init__(self,item_handler,id,x,y,val):
        self.item_handler = item_handler
        self.id = id
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.flag_for_removal = False

    def pickup(self,char):
        ##maybe move this function to the item_handler instead
        self.flag_for_removal = True
        self.on_pickup(char)

    def on_pickup(self,char):
        pass

    def update(self):
        pass

class Gold(Item_Drop):
    item_id = 0
    name = "GoldObj"

    def __init__(self,item_handler,id,x,y,val):
        Item_Drop.__init__(self,item_handler,id,x,y,val)
        self.val = val
    
    def on_pickup(self,char):
        char.items["Gold"] += self.val

class Small_Health_Potion(Item_Drop):
    item_id = 1
    name = "Health Potion"
    power = 1


