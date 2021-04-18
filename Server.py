import socket
import threading
import time
import sys
import random
from datetime import datetime

class TcpServer(object):

    list_addr_entrada = []
    list_addr_processo = []
    qnt_entradas = 0
    count_entradas = 0
    exit_flag = False
    closed = False
    s = None


    def tcplink(self, sock, addr):
        while True:
            if self.exit_flag:
                              
                break
            try:
                data = sock.recv(1024)

                time.sleep(0.2)

                

                if data.decode("UTF-8").startswith('*'):
                    data = data.decode("UTF-8")
                    data = str(data).replace('*','')
                    print("Serão " + data + " entradas\n")
                    self.qnt_entradas = int(data)

                elif data.decode("UTF-8").startswith('-'):
                    random.seed(datetime.now())
                    aleat = random.choice(self.list_addr_processo)
                    aleat[0].send(data)
                    self.count_entradas += 1
                    print("Recebendo Dado para ser Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                    print("Enviando Dado para ser Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                    

                elif data.decode("UTF-8").startswith('+'):
                    self.list_addr_entrada[0][0].send(data)
                    self.count_entradas += 1

                    print("Recebendo Dado Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                    print("Enviando Dado Tratado")
                    print(data.decode("UTF-8"))
                    print('\n')

                if(self.qnt_entradas*2 == self.count_entradas):
                    exit_socket = "exit"
                    for i in self.list_addr_processo:
                        i[0].send(exit_socket.encode("UTF-8"))
                    self.exit_flag = True
                    if not self.closed:
                        self.closed = True
                        self.s.close()
                        break
                    
                
            except ConnectionResetError as cre:
                break

    def create_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.bind(("localhost", 4001))
        self.s.listen(2)
        print("Waiting for connection...")

        while True:
            
            if self.exit_flag:
                break
            try:
                sock, addr = self.s.accept()
                print("successful connect!")
                data = sock.recv(1024)
                if data.decode("UTF-8").startswith('$'): # client entrada
                    self.list_addr_entrada.append([sock,addr])
                if data.decode("UTF-8").startswith('#'): # client entrada
                    self.list_addr_processo.append([sock,addr])
                t = threading.Thread(target=self.tcplink, args=(sock, addr))
                t.start()
            except:
                print("Encerrando Servidor! ...")


if __name__ == '__main__':
    server = TcpServer()
    server.create_socket()
    
