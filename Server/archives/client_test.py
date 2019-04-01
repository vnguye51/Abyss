#!/usr/bin/env python3

import socket,time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        id = '5'.encode('utf-8')
        s.sendall(id)
time.sleep(1)