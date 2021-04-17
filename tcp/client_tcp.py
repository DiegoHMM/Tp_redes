import socket
import threading
from main import contador_de_letras
from main import le_arquivo


class TcpClient(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr

    def create_client(self):
        self.sock.connect(self.addr)
        print(self.sock.recv(1024).decode("UTF-8"))

        l = le_arquivo("modelo_entrada")

        print("please enter message(enter 'exit' to quit the chat)")

        for i, ele in enumerate(l):
            
            #ENVIA MENSAGEM CRUA
            message = '-'+str(l[i])
            if (message == "exit"):
                print('quit from the chatroom.....')
                break
            
            self.sock.send(message.encode("UTF-8"))
            #print(message)
            
            resposta_servidor = self.sock.recv(1024).decode("UTF-8")
            
            if resposta_servidor.startswith('-'):
                resposta_servidor.replace('-','')
                palavra, cont_consoante, cont_vogal, cont_numeros = contador_de_letras(resposta_servidor)
                consoante = "C=" + str(cont_consoante)
                vogal = "V=" + str(cont_vogal)
                numero = "N=" + str(cont_numeros)
                if cont_consoante == 0 and cont_vogal == 0 and cont_numeros == 0:
                    resposta_Final  = '+'+'erro'
                else:
                    resposta_Final = '+'+consoante+';'+vogal+';'+numero

                print(resposta_Final)
                print(palavra)
                self.sock.send(resposta_Final.encode("UTF-8"))

            # recebi a mensagem final com contadores''
            else:
                print(' ')
                #print(resposta_servidor.replace('+',''))
                
            #print("response is >>>" + self.sock.recv(1024).decode("UTF-8"))


    def thread_run(self):
        lock = threading.Lock()
        try:
            lock.acquire()
            self.create_client()
        finally:
            lock.release()


if __name__ == '__main__':
    client = TcpClient(('127.0.0.1', 8089))
    client.create_client()

'''
import socket
import threading

class TcpClient(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr

    def create_client(self):
        self.sock.connect(self.addr)
        print(self.sock.recv(1024).decode("UTF-8"))
        print("please enter message(enter 'exit' to quit the chat)")
        while True:
            message = input(">>>")
            if (message == "exit"):
                print('quit from the chatroom.....')
                break
            self.sock.send(message.encode("UTF-8"))
            print("response is>>>" + self.sock.recv(1024).decode("UTF-8"))

    def thread_run(self):
        lock = threading.Lock()
        try:
            lock.acquire()
            self.create_client()
        finally:
            lock.release()


if __name__ == '__main__':
    client = TcpClient(('127.0.0.1', 8089))
    client.create_client()

'''