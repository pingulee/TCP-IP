import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

broadcast_address = ('<broadcast>', 12345)
print('브로드캐스트 메시지 전송 시작')

while True:
    server_socket.sendto(b'이 메시지는 브로드캐스트 전송됩니다.', broadcast_address)
    print("브로드캐스트 메시지 전송 중...")
