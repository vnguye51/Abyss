
import asyncio,time,struct,json
from Database.actions import Authentication

##Assign Port and IP of Host
HOST = '127.0.0.1'
PORT = 8081

authentication = Authentication()

def write_to_buffer(writer,message):
    writer.buffer.append(message)

def export_packet(writer):
    encoded_message = json.dumps(writer.buffer).encode()
    writer.write(encoded_message)
    writer.buffer = []

def create_character(writer,message):
    print("creating character")
    authentication.create_new(message["username"],message["password"])

def login(writer,message):
    print("logging in")
    if authentication.login(message["username"],message["password"]):
        message = {
            "id": 0,
            "message":{
                #should be replaced with a generated session key instead 
                "account_id": 1
            }
        }
    else:
        message={
            "id": 1
        }
    write_to_buffer(writer,message)
    export_packet(writer)
        


async def echo_server(reader, writer):
    addr = writer.get_extra_info('peername')
    print("Client connected at (%s,%s)" % (addr[0],addr[1]))
    writer.buffer = []
    while True:
        try:
            ##main loop for socket
            data = await reader.read(1024)  # Max number of bytes to read
            decoded_data = data.decode("utf-8").split("\x00")
            client_message = json.loads(decoded_data[0])["messages"]
            print(client_message)
            for message in client_message:
                if message["id"] == 1:
                    create_character(writer,message)
                elif message["id"] == 2:
                    login(writer,message)
            if not data:
                print('breaking connection to %s' % addr[1])
                break
            await writer.drain()
        except ConnectionError:
            print("Lost Connection to (%s,%s)" % (addr[0],addr[1]))
            break
        except Exception as e:
            print(e)
            break
    writer.close()


async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await asyncio.gather(server.serve_forever())

asyncio.run(main(HOST,PORT))