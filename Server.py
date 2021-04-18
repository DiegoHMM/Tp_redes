import socket
import threading
import time

class TcpServer(object):

    list_addr = []

    def tcplink(self, sock, addr):
        #print('Accept new connection from %s:%s...' % addr)
        while True:
            try:
                data = sock.recv(1024)

                time.sleep(1)


                if data.decode("UTF-8").startswith('-'):
                    self.list_addr[0][0].send(data)
                elif data.decode("UTF-8").startswith('+'):
                    self.list_addr[1][0].send(data)

            except ConnectionResetError as cre:
                print('error', cre)
                break
        sock.close()
        print('Connection from %s:%s closed.' % addr)

    def create_sokcet(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind(("localhost", 4001))
        s.listen(2)
        print("Waiting for connection...")

        while True:

            sock, addr = s.accept()
            print("seccessful connect!")
            self.list_addr.append([sock,addr])
            t = threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()


if __name__ == '__main__':
    server = TcpServer()
    server.create_sokcet()
