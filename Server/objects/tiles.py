class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.prev_x = x
        self.prev_y = y
        self.width = 16
        self.height = 16
        self.xvel = 0
        self.yvel = 0
        self.momentum = 9999999
        self.weight = 9999999

    def collide(self,obj):
        ###Define what happens to the obj if it collides with this tile.
        pass

        
class Impassable(Tile):
    def collide(self,obj):
        pass