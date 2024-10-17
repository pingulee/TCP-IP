import socket
import struct

multicast_group = '224.1.1.1'
server_address = ('', 5007)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.bind(server_address)
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print('멀티캐스트 그룹 가입 완료')

while True:
    data, addr = client_socket.recvfrom(1024)
    print(f"수신한 데이터: {data.decode()}")
