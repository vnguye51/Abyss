import asyncio,time,struct,json
from players import *

HOST = '127.0.0.1'
PORT = 8080


players = Players()
id_assignment = 0

def first_connect(reader,writer,client_id):
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
    writer.drain()

async def echo_server(reader, writer):
    global id_assignment, players
    
    addr = writer.get_extra_info('peername')
    print("Client connected at (%s,%s)" % (addr[0],addr[1]))
    ##instantiate new player
    player = Player(0,0,id_assignment)
    id_assignment += 1
    #append player to the list of all players
    players.player_array.append(player)

    first_connect(reader,writer,player.id)

    while True:
        ##main loop for socket
        data = await reader.read(1024)  # Max number of bytes to read
        decoded_data = data.decode("utf-8").split("\x00")
        inputs = json.loads(decoded_data[0])
        player.player_input(inputs)
        if not data:
            print('breaking connection to %s' % addr[1])
            break
        writer.write(players.export_packet())
        await writer.drain()  # Flow control, see later
    writer.close()
    
    
async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await server.serve_forever()

asyncio.run(main(HOST,PORT))