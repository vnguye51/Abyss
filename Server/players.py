import json
import utils
class Players:
    def __init__(self):
        self.player_array = []
    
    def get_player_data(self):
        res = {}
        for player in self.player_array:
            res[str(player.id)] = {
                "x": player.x,
                "y": player.y
            }
        return res

    def export_packet(self):
        player_data = self.get_player_data()
        data = {
            "id": 3,
            "message": player_data
        }
        return json.dumps(data).encode()

    def is_colliding(self):
        #Returns list of colliding players
        res = []
        for i in range(0,len(self.player_array)):
            char1 = self.player_array[i]
            for j in range(i+1,len(self.player_array)):
                char2 = self.player_array[j]
                if utils.AABB(char1,char2):
                    res.append((char1,char2))
        return res

class Character:
    def __init__(self,x,y,id,writer):
        self.x = x
        self.y = y 
        self.xvel = 0
        self.yvel = 0
        self.width = 16
        self.height = 16
        self.id = id
        self.writer = writer


        


class Player(Character):
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