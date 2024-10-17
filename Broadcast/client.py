import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('', 12345))

print('브로드캐스트 메시지 수신 대기 중...')

while True:
    data, addr = client_socket.recvfrom(1024)
    print(f"브로드캐스트 메시지: {data.decode()} from {addr}")
