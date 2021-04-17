
import socket
import threading
import time

class TcpServer(object):

    list_addr = []

    def tcplink(self, sock, addr):
        #print('Accept new connection from %s:%s...' % addr)
        sock.send("Welcome to chatroom!".encode("UTF-8"))
        while True:
            try:
                data = sock.recv(2048)
                time.sleep(1)
                if data:
                    '''
                    #É PORQUE TENHO QUE ENVIAR PARA PROCESSAMENTO
                    if not str(data.decode("UTF-8")).startswith('-'):
                        resp = '-'+data.decode("UTF-8")
                    #É PORQUE O DADO DE SAIDA ESTA PRONTO
                    elif str(data.decode("UTF-8")).startswith('+'):
                        resp = str(data.decode("UTF-8")).replace('+','')
                    '''

                    resp = str(data.decode("UTF-8"))
                else: 
                    break
                print(resp)
                sock.send(resp.encode("UTF-8"))
            except ConnectionResetError as cre:
                print('error', cre)
                break
        sock.close()
        print('Connection from %s:%s closed.' % addr)

    def create_sokcet(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind(("127.0.0.1", 8089))
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





