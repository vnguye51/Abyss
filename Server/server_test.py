import asyncio,time,struct,json

HOST = '127.0.0.1'
PORT = 8080

class Player:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y 

    def player_input(self,input_map):
        if input_map["up"] == 1:
            self.y -= 4
        if input_map["left"] == 1:
            self.x -= 4
        if input_map["down"] == 1:
            self.y += 4
        if input_map["right"] == 1:
            self.x += 4

    def export_packet(self):
        pos_data = {
            "x": self.x,
            "y": self.y
        }
        return json.dumps(pos_data).encode()

players_list = []

async def echo_server(reader, writer):
    addr = writer.get_extra_info('peername')
    print("Client connected at %s" % addr[0])
    player = Player()
    players_list.append(player)
    while True:
        data = await reader.read(1024)  # Max number of bytes to read
        decoded_data = data.decode("utf-8").split("\x00")
        inputs = json.loads(decoded_data[0])
        player.player_input(inputs)
        if not data:
            print('breaking connection to %s' % addr[1])
            break
        writer.write(player.export_packet())
        await writer.drain()  # Flow control, see later
    writer.close()
    
    
async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await server.serve_forever()

asyncio.run(main(HOST,PORT))