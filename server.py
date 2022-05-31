from http import client
import random
import socket
import time
import threading

def randomNum(clientMessage):
    if clientMessage != 4:
        number_random = random.randint(1, 9)
        number_random = str(number_random)
        return number_random

def sendNum(clientMessage, number_random):
    if clientMessage < 5:
        conn.sendall(number_random.encode())
        time.sleep(1)

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        conn, addr = server.accept()
        print(f"Server is listening in {HOST} : {PORT}")
        clientMessage = 0
        thread_1 = threading.Thread(target=randomNum, args=(clientMessage))
        thread_1.start() 
        number_random = randomNum(clientMessage)
        thread_2 = threading.Thread(target=sendNum, args=(clientMessage, number_random))
        thread_2.start()
        while True:
            while clientMessage != 4:
                number_list = []
                number_list.append(number_random)
                number_random = randomNum(clientMessage)
                for i in range(4):
                    while True:
                        if number_random in number_list:
                            number_random = randomNum(clientMessage)
                        else:
                            sendNum(clientMessage, number_random)
                            number_list.append(number_random)
                            clientMessage += 1
                            break
                number_list.clear()
                
            clientMessage = conn.recv(1024).decode()
            clientMessage = int(clientMessage)
            if clientMessage == 4:
                print("disconnected")
                break
