import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))

print('유니캐스트 서버 시작')

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"클라이언트: {data.decode()} from {addr}")
    server_socket.sendto('ok'.encode('utf-8'), addr)
