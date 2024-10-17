import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)
client_socket.sendto('hi'.encode('utf-8'), server_address)

data, addr = client_socket.recvfrom(1024)
print(f"서버: {data.decode('utf-8')}")
