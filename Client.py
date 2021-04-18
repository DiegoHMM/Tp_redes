import socket
import threading
from utils import contador_de_letras
from utils import le_arquivo
import sys


class TcpClient(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        self.c_entrada = '$'
        self.c_processo = '#'
        

    def create_client(self):
        self.sock.connect(self.addr)

        if len(sys.argv) > 1:
            self.sock.send(self.c_entrada.encode("UTF-8"))

            arquivo = open("saida.txt", "w")
            arquivo.close()
            l = le_arquivo(str(sys.argv[1]))

            qnt_entradas = '*'+l[0]
            self.sock.send(qnt_entradas.encode("UTF-8"))

            iter_messages = iter(l)
            next(iter_messages)
            for ele in iter_messages:
                
                message = '-'+str(ele)

                print("Enviando dado CRU Para o Servidor")
                print(message)
                print('\n')
                self.sock.send(message.encode("UTF-8"))

                

                while True:
                    resposta_servidor = self.sock.recv(1024).decode("UTF-8")
                    if resposta_servidor:
                        arquivo = open("saida.txt", "a")
                        print("Recebendo Resposta Final do Servidor'")
                        print(resposta_servidor)
                        print('\n')
                        resposta_servidor = resposta_servidor.replace('+','')
                        
                        arquivo.write(resposta_servidor+'\n')
                        break   
                    print(resposta_servidor)

        else:
            self.sock.send(self.c_processo.encode("UTF-8"))
            while True:
                resposta_servidor = self.sock.recv(1024).decode("UTF-8")
                print("Recebendo do Servidor para Tratamento")
                print(resposta_servidor)
                print('\n')

                if(resposta_servidor == 'exit'):
                    print("Fim do processamento")
                    print("Encerrando client...")
                    self.sock.send(resposta_servidor.encode("UTF-8"))
                    self.sock.close()
                    break

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

                    print("Enviando dado tratado para Servidor")
                    print(resposta_Final)
                    print('\n')
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
