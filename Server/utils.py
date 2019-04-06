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
            obj.pos_lock = False
            self.update_single_obj(obj)
            
    def update_single_obj(self,obj):
        res = []
        x_floored_16 = obj.x-obj.x%16
        y_floored_16 = obj.y-obj.y%16
        for x in range(x_floored_16,obj.x+obj.width,16):
            for y in range(y_floored_16,obj.y+obj.height,16):
                key = (x,y)
                res.append(key)
                self.spatial_map[key]["objects"].append(obj)
        return res

    def get_collisions(self,collisions,keys):
        #Returns list of colliding objects
        for key in keys:
            #For each tile in the spatial map if there is a collision add the two objects to the collisions list
            objects = self.spatial_map[key]["objects"]
            for i in range(0,len(objects)):
                for j in range(i+1,len(objects)):
                    if AABB(objects[i],objects[j]):
                        #Insert into the collision array by highest speed
                        collision = (objects[i],objects[j])
                        speed = abs(objects[i].xvel)+abs(objects[i].yvel)
                        speedJ = abs(objects[j].xvel)+abs(objects[j].yvel)
                        #If objects[j] is faster replace speed with its speed and flip the tuple so the faster element is first
                        if speed < speedJ:
                            speed = speedJ
                            collision = (collision[1],collision[0])
                        for k in range(0,len(collisions)):
                            speedK = abs(collisions[k][0].xvel)+abs(collisions[k][1].yvel)
                            if speed >= speedK:
                                collisions.insert(k,collision)
                                return
                        collisions.append(collision)

    def collision_resolution(self):
        collisions = []
        #initialize collision with all collisions
        self.get_collisions(collisions,self.spatial_map.keys())
        while collisions:
            #pop collision from stack
            collision = collisions.pop(0)
            a,b = collision[0],collision[1]
            #If the collision is no longer valid continue to the next iteration
            if not AABB(a,b):
                continue
            self.resolve_collision_between(a,b)
            #The faster object gets to lock its place and the slower one inherits the velocity of the faster one
            a.pos_lock = True
            b.xvel = a.xvel
            b.yvel = a.yvel
            self.update_single_obj(a)
            new_keys = self.update_single_obj(b)
            #insert any collisions that were generated from the move
            #collisions
            self.get_collisions(collisions,new_keys)


    def remove_from_map(self,obj):
        x_floored_16 = obj.x-obj.x%16
        y_floored_16 = obj.y-obj.y%16
        for x in range(x_floored_16,obj.x+obj.width,16):
            for y in range(y_floored_16,obj.y+obj.height,16):
                key = (x,y)
                i = self.spatial_map[key]["objects"].index(obj)
                self.spatial_map[key]["objects"].pop(i)

    def resolve_collision_between(self,a,b):
        #resolve horizontal collision
        self.remove_from_map(a)
        self.remove_from_map(b)
        if a.pos_lock:
            print('aaaa')
            if b.pos_lock: raise ValueError
            if a.x <= b.x:
                while AABB(a,b):
                    b.x += 1
            else:
                while AABB(a,b):
                    b.x -= 1
            if a.y <=  0:
                while AABB(a,b):
                    b.y += 1
            else:
                while AABB(a,b):
                    b.y -= 1

        elif a.xvel != 0 or b.xvel != 0:
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
        elif a.yvel != 0 or b.yvel != 0:
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
        else:
            while AABB(a,b):
                b.y += 1

def AABB(a,b):
    if(a.x < b.x + b.width and
        a.x + a.width > b.x and 
        a.y < b.y + b.height and
        a.y + a.height > b.y):
        return True
    else:
        return False


