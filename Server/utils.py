from objects.tiles import Impassable

class SpatialMap:
    def __init__(self,tiled_json):
        #The first layer should be the tilemap with collidables
        self.width = tiled_json["width"]
        self.height = tiled_json["height"]
        self.spatial_map = {(x,y):{"objects":[]} for x in range(0,self.width*16,16) for y in range(0,self.height*16,16)}
        objects = tiled_json["layers"][0]["objects"]
        self.tiles = []
        for obj in objects:
            self.tiles.append(Impassable(obj["x"],obj["y"]-obj["height"]))



    def update_map(self,players,enemies):
        """Update map should be called each tick. Takes in the list of all game objects and places them into the spatial map"""
        ##Reset map
        objects = players.player_array + enemies.enemy_array + self.tiles
        for key in self.spatial_map.keys():
            self.spatial_map[key]["objects"] = []

        #For each object place a reference to them inside each tile they overlap
        for obj in objects:
            # obj.pos_lock = False
            # print(obj.x,obj.y)
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
                        #If objects[j] is faster replace speed with its speed and flip the tuple so the faster element is first
                        if objects[i].momentum < objects[j].momentum:
                            collision = (collision[1],collision[0])
                        inserted = False
                        for k in range(0,len(collisions)):
                            if collision[0].momentum >= collisions[k][0].momentum:
                                collisions.insert(k,collision)
                                break
                        if not inserted:
                            collisions.append(collision)

    def collision_resolution(self):
        collisions = []
        
        #initialize collision with all collisions
        
        self.get_collisions(collisions,self.spatial_map.keys())
        print(collisions)
        while collisions:
            #pop collision from stack
            collision = collisions.pop(0)
            a,b = collision[0],collision[1]
            #If the collision is no longer valid continue to the next iteration
            if not AABB(a,b):
                continue
            self.resolve_collision_between(a,b)
            b.momentum = a.momentum
            # b.xvel = a.xvel
            # b.yvel = a.yvel
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

        #move remove from map to collision resolution?
        self.remove_from_map(a)
        self.remove_from_map(b)

        if a.momentum >= b.momentum:
            heavy_obj = a
            light_obj = b
        else:
            light_obj = a
            heavy_obj = b

        direction = collision_direction(heavy_obj,light_obj)
        ##If the light object collides with the heavy object from the right
        if direction == "left":
            while AABB(light_obj,heavy_obj):
                light_obj.x -= 1
        if direction == "right":
            while AABB(light_obj,heavy_obj):
                light_obj.x += 1
        if direction == "top":
            while AABB(light_obj,heavy_obj):
                light_obj.y -= 1
        if direction == "bottom":
            while AABB(light_obj,heavy_obj):
                light_obj.y += 1


def AABB(a,b):
    if(a.x < b.x + b.width and
        a.x + a.width > b.x and 
        a.y < b.y + b.height and
        a.y + a.height > b.y):
        return True
    else:
        return False

def collision_direction(heavy,light):
    ##if the left edge is greater then the right edge of the other object
    if light.prev_x >= heavy.prev_x + heavy.width:
        return "right"
    if light.prev_x + light.width <= heavy.prev_x:
        return "left"
    if light.prev_y >= heavy.prev_y + heavy.height:
        return "bottom"
    if light.prev_y + light.height <= heavy.prev_y:
        return "top"
    raise ValueError