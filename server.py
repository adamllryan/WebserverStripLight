#!/usr/bin/env python3

import socket

HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:https://github.com/home-assistant/operating-system/releases/download/6.1/haos_rpi4-64-6.1.img.xz
                break
            conn.sendall(data)