import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    서버의 요청 처리기 클래스.

    서버 연결마다 한 번 인스턴스화되며, 클라이언트와의 통신을 구현하기 위해 handle()
    메서드를 재정의해야 합니다.
    """

    def handle(self):
        # self.request는 클라이언트에 연결된 TCP 소켓입니다
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # 단지 같은 데이터를 다시 보내지만, 대문자로 변환합니다
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "121.151.120.199", 9999

    # 포트 9999에서 localhost에 바인딩하여 서버를 만듭니다
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # 서버를 활성화합니다; Ctrl-C를 사용하여 프로그램을 중단할 때까지 계속
        # 실행됩니다.
        server.serve_forever()