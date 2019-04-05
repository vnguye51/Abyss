class SpatialMap:
    def __init__(self,tiled_json):
        #The first layer should be the tilemap with collidables
        self.width = tiled_json["width"]
        self.height = tiled_json["height"]
        self.spatial_map = {(x,y):{"objects":[],"impassable":False} for x in range(0,self.width*16,16) for y in range(0,self.height*16,16)}
        objects = tiled_json["layers"][0]["objects"]
        for obj in objects:
            self.spatial_map[(obj["x"],obj["y"])]["impassable"] = True

    def update_map(self,players,enemies):
        """Update map should be called each tick. Takes in the list of all game objects and places them into the spatial map"""
        ##Reset map
        objects = players.player_array + enemies.enemy_array
        for key in self.spatial_map.keys():
            self.spatial_map[key]["objects"] = []

        #For each object place a reference to them inside each tile they overlap
        for obj in objects:
            for x in range(obj.x,obj.x+obj.width+16,16):
                for y in range(obj.y,obj.y+obj.height+16,16):
                    x_floored_16 = x-x%16
                    y_floored_16 = y-y%16
                    self.spatial_map[(x_floored_16,y_floored_16)]["objects"].append(obj)

    def get_collisions(self):
        #Returns list of colliding objects
        res = []
        for key in self.spatial_map.keys():
            #For each tile in the spatial map if there is a collision add the two objects to the collisions list
            objects = self.spatial_map[key]["objects"]
            for i in range(0,len(objects)):
                for j in range(i+1,len(objects)):
                    if AABB(objects[i],objects[j]):
                        res.append((objects[i],objects[j]))
        return res

    def collision_resolution(self):
        collisions = self.get_collisions()
        for a,b in collisions:
            #resolve horizontal collision
            if a.xvel != 0 or b.xvel != 0:
                if abs(a.xvel) == abs(b.xvel):
                    #!!!!!!!possible optimization only need to calculate horizontal/vertical collisions not both at once
                    while AABB(a,b):
                        if a.x <= b.x:
                            a.x -= 1
                            b.x += 1
                        else:
                            a.x += 1
                            b.x -= 1
                elif abs(a.xvel) >= abs(b.xvel):
                    while AABB(a,b):
                        if a.x <= b.x:
                            b.x += 1
                        else:
                            b.x -= 1
                else:
                    while AABB(a,b):
                        if b.x <= a.x:
                            a.x += 1
                        else:
                            a.x -= 1
            #resolve vertical collision
            if a.yvel != 0 or b.yvel != 0:
                if a.yvel == b.yvel and a.yvel != 0:
                    #!!!!!!!possible optimization only need to calculate horizontal/vertical collisions not both at once
                    while AABB(a,b):
                        if a.y <= b.y:
                            a.y -= 1
                            b.y += 1
                        else:
                            a.y += 1
                            b.y -= 1
                elif abs(a.yvel) >= abs(b.yvel):
                    while AABB(a,b):
                        if a.y <= b.y:
                            b.y += 1
                        else:
                            b.y -= 1
                else:
                    while AABB(a,b):
                        if b.y <= a.y:
                            a.y += 1
                        else:
                            a.y -= 1
                            
def AABB(a,b):
    if(a.x < b.x + b.width and
        a.x + a.width > b.x and 
        a.y < b.y + b.height and
        a.y + a.height > b.y):
        return True
    else:
        return False


