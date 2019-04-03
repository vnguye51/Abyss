import asyncio,time,struct,json
from players import *

HOST = '127.0.0.1'
PORT = 8080


players = Players()
id_assignment = 0


def first_connect(writer,client_id):
    global players
    message ={
        "id": 0,
        "message": {
            "client_id": client_id,
            "players": players.get_player_data()
        }
    }
    encoded_message = json.dumps(message).encode()
    writer.write(encoded_message)

def add_player(new_player):
    #Send a message to all clients that are not the 
    global players
    print('adding new player!')
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
        ##main loop for socket
        data = await reader.read(1024)  # Max number of bytes to read
        decoded_data = data.decode("utf-8").split("\x00")
        inputs = json.loads(decoded_data[0])
        player.player_input(inputs)
        if not data:
            print('breaking connection to %s' % addr[1])
            break
        try:
            writer.write(players.export_packet())
        except ConnectionError:
            break
        await writer.drain()
    writer.close()
    
    
async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await server.serve_forever()

asyncio.run(main(HOST,PORT))