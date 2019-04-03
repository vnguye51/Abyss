import json
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


class Character:
    def __init__(self,x,y,id,writer):
        self.x = x
        self.y = y 
        self.id = id
        self.writer = writer

class Player(Character):
    def player_input(self,input_map):
        if input_map["up"] == 1:
            self.y -= 4
        if input_map["left"] == 1:
            self.x -= 4
        if input_map["down"] == 1:
            self.y += 4
        if input_map["right"] == 1:
            self.x += 4