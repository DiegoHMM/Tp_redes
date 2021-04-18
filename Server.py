import socket
import threading
import time

class TcpServer(object):

    list_addr = []
    qnt_entradas = 0
    count_entradas = 0

    def tcplink(self, sock, addr):
        while True:
            try:
                data = sock.recv(1024)

                time.sleep(1)
                if data.decode("UTF-8").startswith('*'):
                    data = data.decode("UTF-8")
                    data = str(data).replace('*','')
                    print("Serão " + data + " entradas\n")
                    self.qnt_entradas = int(data)
                elif data.decode("UTF-8").startswith('-'):
                    self.list_addr[0][0].send(data)
                    self.count_entradas += 1
                    print("Recebendo Dado para ser Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                    print("Enviando Dado para ser Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                    

                elif data.decode("UTF-8").startswith('+'):
                    self.list_addr[1][0].send(data)
                    self.count_entradas += 1

                    print("Recebendo Dado Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                    print("Enviando Dado Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                if(self.qnt_entradas*2 == self.count_entradas):
                    exit_socket = "exit"
                    self.list_addr[0][0].send(exit_socket.encode("UTF-8"))
                    break
                
            except ConnectionResetError as cre:
                break
    '''
        self.list_addr[1][0].close()
        self.list_addr[0][0].close()
        print('Closed'+ str(self.list_addr[1][0]))
        print(str(sock))
    '''


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
