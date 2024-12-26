
import time
import socket
import json
import logging

logging.basicConfig(filename='ppo.log', level=logging.INFO)

def start_server():
    """Запуск сокет-сервера для приема данных от ПИУ."""
    server_address = ('127.0.0.1', 6000)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()
        print("Socket Server is listening...")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f'Connected by {addr}')
                data = conn.recv(1024)
                if data:
                    logging.info(f'Ответ от клиента: {data.decode("utf-8")}')
                    conn.sendall(b'ACK') 
                    time.sleep(5)
            server_socket.settimeout(10)  


if __name__ == "__main__":
    start_server()
