import socket
import threading
from main import contador_de_letras
from main import le_arquivo
import sys


class TcpClient(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        

    def create_client(self):
        self.sock.connect(self.addr)


        if len(sys.argv) > 1: #cliente de requisicao
            arquivo = open("texto.txt", "w")
            arquivo.close()
            # ---------------------------------------       client one ----------------------------------------------------------
            print(sys.argv[1])
            l = le_arquivo(str(sys.argv[1]))

            for i, ele in enumerate(l):
                
                message = '-'+str(l[i])

                print("Enviando para o servidor")
                print(message)
                print("---------------------")
                self.sock.send(message.encode("UTF-8"))

                

                while True:
                    resposta_servidor = self.sock.recv(1024).decode("UTF-8")
                    if resposta_servidor:
                        arquivo = open("saida.txt", "a")
                        print(resposta_servidor)
                        resposta_servidor = resposta_servidor.replace('+','')
                        
                        arquivo.write(resposta_servidor+'\n')
                        break
                    print(resposta_servidor)
            
             # -------------------------------------------------------------------------------------------------

        else: #cliente processador
            #-------------------------------------------------------client dois ----------------------------------------
            while True:
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
                    self.sock.send(resposta_Final.encode("UTF-8"))

    def thread_run(self):
        lock = threading.Lock()
        try:
            lock.acquire()
            self.create_client()
        finally:
            lock.release()


if __name__ == '__main__':
    client = TcpClient(('localhost', 4001))
    client.create_client()
