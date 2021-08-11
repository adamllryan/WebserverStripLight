import socket

whitelist = ['192.168.0.216']
HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
temp = 0
while True: 
    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            ip, port = conn.getpeername()
            for i in whitelist: 
                if (i == ip):
                    temp = 1
            try: #i do not know how to close the socket so i am doing a controlled crash because i do not know what i am doing
                if (temp == 0):
                    socket.close()
            except: 
                print("closed connection from", ip, "dude tried to connect to my server lol get fucked")


"""
i do not know python i will test what this tutorial code does later



class MySocket:
    demonstration class only
      - coded for clarity, not efficiency
    

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
"""