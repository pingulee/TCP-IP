import socket
import struct
import time

multicast_group = ('224.1.1.1', 5007)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

print('멀티캐스트 데이터 전송 시작')

while True:
    message = b'이 메시지는 멀티캐스트 그룹에 전송됩니다.'
    server_socket.sendto(message, multicast_group)
    print("멀티캐스트 메시지 전송 중...")
    time.sleep(2)
