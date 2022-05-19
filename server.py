import random
import socket


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        conn, addr = server.accept()
        print(f"Server is listening in {HOST} : {PORT}")
        number_list = []
        number_random = random.randint(1, 9)
        number_random = str(number_random)
        for i in range(4):
            while True:
                if number_random in number_list:
                    number_random = random.randint(1, 9)
                    number_random = str(number_random)
                else:
                    conn.sendall(number_random.encode())
                    number_list.append(number_random)
                    break


