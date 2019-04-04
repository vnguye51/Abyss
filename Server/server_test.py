import asyncio,time,struct,json
from objects.objects import *

HOST = '127.0.0.1'
PORT = 8080


players = Players()
enemies = Enemies()
id_assignment = 0


def first_connect(writer,client_id):
    global players
    message ={
        "id": 0,
        "message": {
            "client_id": client_id,
            "players": players.get_data()
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
    # coroutines = [write_and_drain(player.writer,encoded_message) for player in players.player_array if player.id != new_player.id ]
    # await asyncio.create_task(*coroutines)

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
            
    
def export_objects(player_data,enemy_data):
    """Encode a message containing player and enemy info"""
    data = {
        "id": 3,
        "message": {
            "player_data": player_data,
            "enemy_data": enemy_data
        }
    }
    return json.dumps(data).encode()

async def echo_server(reader, writer):
    global id_assignment, players
    addr = writer.get_extra_info('peername')
    print("Client connected at (%s,%s)" % (addr[0],addr[1]))
    ##instantiate new player
    player = Player(0,0,id_assignment,writer)
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
            writer.write(export_objects(players.get_data(),enemies.get_data()))
            await writer.drain()
        except ConnectionError:
            on_disconnect(player)
            print("Lost Connection to (%s,%s)" % (addr[0],addr[1]))
            break 
    writer.close()

async def game_loop():
    while True:
        #Move players based on their velocity
        for player in players.player_array:
            player.x += player.xvel
            player.y += player.yvel
        for enemy in enemies.enemy_array:
            enemy.update()
        #Resolve collisions between players
        collisions = players.is_colliding()
        utils.collision_resolution(collisions)

        await asyncio.sleep(1.0/30.0)
    
async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await asyncio.gather(server.serve_forever(),game_loop())



asyncio.run(main(HOST,PORT))