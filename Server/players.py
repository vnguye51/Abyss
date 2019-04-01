import json
class Players:
    def __init__(self):
        self.player_array = []
    
    def export_packet(self):
        player_data = [{"id": player.id, "x": player.x,"y": player.y} for player in self.player_array]
        data = {
            "id": 1,
            "message": player_data
        }
        return json.dumps(data).encode()


class Character:
    def __init__(self,x,y,id):
        self.x = x
        self.y = y 
        self.id = id

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