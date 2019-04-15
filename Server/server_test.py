import asyncio,time,struct,json
from objects.objects import *
from items.main import Item_Drop_Handler, Gold
from utils import SpatialMap, AABB

##Assign Port and IP of Host
HOST = '127.0.0.1'
PORT = 8080

##Grab map data
map_file = open("../maps/test_map.json")
map_json = json.load(map_file)
map_file.close()

players = Players()
enemies = Enemies()
attacks = Attacks()
items = Item_Drop_Handler()

items.instantiate(Gold, 80, 80, 50)
enemies.instantiate(Goblin, 64, 64, attacks)
id_assignment = 0
spatial_map = SpatialMap(map_json)

def first_connect(writer,client_id):
    global players
    message ={
        "id": 0,
        "message": {
            "client_id": client_id,
            "players": players.get_data(),
            "enemies": enemies.get_data(),
            "items": items.get_data()
        }
    }
    encoded_message = json.dumps(message).encode()
    writer.write(encoded_message)

def add_player(new_player):
    #Send a message to all clients that are not the new player
    global players
    message ={
        "id": 1,
        "message":{
            "new_player_id": new_player.id,
            "x": new_player.x,
            "y": new_player.y
        }
    }
    encoded_message = json.dumps(message).encode()
    for player in players.player_array:
        if player.id != new_player.id:
            player.writer.write(encoded_message)

def on_disconnect(disc_player):
    global players
    message = {
        "id": 2,
        "message":{
            "player_id": disc_player.id
        }
    }
    encoded_message = json.dumps(message).encode()
    #Send a message to all clients that are not the disconnected player
    delete_flag = -1
    for i,player in enumerate(players.player_array):
        if player.id != disc_player.id:
            player.writer.write(encoded_message)
        else:
            delete_flag = i

    players.player_array.pop(delete_flag)
            
    
def export_objects(player_data,enemy_data,attack_data,item_data):
    """Encode a message containing player and enemy info"""
    data = {
        "id": 3,
        "message": {
            "player_data": player_data,
            "enemy_data": enemy_data,
            "attack_data": attack_data,
            "item_data": item_data
        }
    }
    return json.dumps(data).encode()

async def echo_server(reader, writer):
    global id_assignment, players
    addr = writer.get_extra_info('peername')
    print("Client connected at (%s,%s)" % (addr[0],addr[1]))
    ##instantiate new player
    player = Player(16,16,id_assignment,writer,attacks)
    id_assignment += 1
    #append player to the list of all players
    players.player_array.append(player)
    first_connect(writer,player.id)
    add_player(player)
    while True:
        try:
            ##main loop for socket
            data = await reader.read(1024)  # Max number of bytes to read
            decoded_data = data.decode("utf-8").split("\x00")
            inputs = json.loads(decoded_data[0])
            player.player_input(inputs)
            if not data:
                print('breaking connection to %s' % addr[1])
                break
            writer.write(export_objects(players.get_data(),enemies.get_data(),attacks.get_data(),items.get_data()))
            await writer.drain()
        except ConnectionError:
            on_disconnect(player)
            print("Lost Connection to (%s,%s)" % (addr[0],addr[1]))
            break 
    writer.close()

async def game_loop():
    while True:
        start = time.time()
        print('------------')
        #Move players
        for player in players.player_array:
            player.update()           
        players.player_array = list(filter(lambda player: not player.flag_for_removal, players.player_array))
            
        #Move Enemies
        for enemy in enemies.enemy_array:
            enemy.update()
        enemies.enemy_array = list(filter(lambda enemy: not enemy.flag_for_removal,enemies.enemy_array))

        #Check for objects and attack collisions
        for attack in attacks.attack_array:
            attack.update()
        attacks.attack_array = list(filter(lambda attack: not attack.flag_for_removal,attacks.attack_array))

        #Check for items that need to be removed
        for item in items.item_array:
            item.update()
        items.item_array = list(filter(lambda item: not item.flag_for_removal,items.item_array))

        #Resolve any attacks
        spatial_map.resolve_attacks()

        #Update the spatial map of all objects
        spatial_map.update_map(players,enemies,attacks,items)

        #If there are any objects left that should not be colliding move them apart from each other
        spatial_map.collision_resolution()

        time_elapsed = time.time() - start
        await asyncio.sleep(max(1.0/30.0-time_elapsed,0))
    
async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await asyncio.gather(server.serve_forever(),game_loop())



asyncio.run(main(HOST,PORT))