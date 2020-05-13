import socket
import sys

HOST, PORT = "121.151.120.199", 9999
data = " ".join(sys.argv[1:])

# 소켓을 만듭니다 (SOCK_STREAM은 TCP 소켓을 의미합니다)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # 서버에 연결하고 데이터를 전송합니다
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # 서버에서 데이터를 수신하고 종료합니다
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))