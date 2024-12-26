import socket
import json
import random
import time
import logging

logging.basicConfig(filename='piu.log', level=logging.INFO)


def generate_random_data():
    """Генерирует случайные данные для отправки на сервер."""
    return {
        "time": int(time.time() * 1_000_000_000),  # GPS время в наносекундах
        "packetType": 1,  # Тип команды обнаружения
        "deviceID": random.randint(1, 100),  # Идентификатор устройства
        "deviceType": random.randint(1, 10),  # Тип устройства
        "deviceLatitude": random.uniform(-90, 90),  # Широта
        "deviceLongitude": random.uniform(-180, 180),  # Долгота
        "deviceAltitude": random.uniform(0, 10000),  # Высота
        "signalType": random.randint(1, 10),  # Тип радиосигнала
        "signalFrequency": random.randint(1000, 5000),  # Частота сигнала
        "signalAmplitude": random.randint(-150, 20),  # Амплитуда сигнала
        "signalWidth": random.randint(1, 100),  # Ширина сигнала
        "signalDetectionType": random.randint(1, 2),  # Тип обнаружения
        "uav": {
            "uavType": "Drone",  # Тип БПЛА
            "serialNumber": f"SN{random.randint(1000,9999)}",  # Серийный номер
            "startUavLatitude": random.uniform(-90, 90),
            "startUavLongitude": random.uniform(-180, 180),
            "uavLatitude": random.uniform(-90, 90),
            "uavLongitude": random.uniform(-180, 180),
            "uavAltitude": random.uniform(0, 10000),
            "operatorLatitude": random.uniform(-90, 90),
            "operatorLongitude": random.uniform(-180, 180)
        }
    }

def main():
    server_address = ('127.0.0.1', 6000)  
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect(server_address)  
                data = generate_random_data()  
                client_socket.sendall(json.dumps(data).encode('utf-8'))  
                logging.info(f"Отправлено: {data}")
                response = client_socket.recv(1024)  
                print(f'Received: {response.decode("utf-8")}')
                logging.info(f"Ответ от сервера: {response.decode('utf-8')}")
            except ConnectionRefusedError:
                print("Server not available. Retrying...")
                time.sleep(8)  

if __name__ == "__main__":
    main()
