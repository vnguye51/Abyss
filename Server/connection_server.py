


async def echo_server(reader, writer):
    addr = writer.get_extra_info('peername')
    
    while True:
        try:
            ##main loop for socket
            data = await reader.read(1024)  # Max number of bytes to read
            decoded_data = data.decode("utf-8").split("\x00")
            client_message = json.loads(decoded_data[0])["messages"]
            for message in client_message:

            if not data:
                print('breaking connection to %s' % addr[1])
                break
            export_objects(player,players.get_data(),enemies.get_data(),attacks.get_data(),items.get_data())
            player.export_packet()
            await writer.drain()
        except ConnectionError:
            on_disconnect(player)
            print("Lost Connection to (%s,%s)" % (addr[0],addr[1]))
            break 
    writer.close()


async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await asyncio.gather(server.serve_forever(),game_loop())



asyncio.run(main(HOST,PORT))