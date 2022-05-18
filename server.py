from cgitb import handler
from concurrent.futures import thread
from http import server
import socket
import threading

IP = socket.gethostbyname(socket,socket.gethostbyname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        msg = f"MSG recieved: {msg}"
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("Server id starting...")
    server = socket.socke(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening in {IP} : {PORT}")

    while True:
        conn ,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACIVE CONNECTION] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()