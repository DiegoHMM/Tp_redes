# TP-Redes
TP referente a disciplina de Redes de Computadores pela UFOP

# Implementação TCP
Implementar um par de programas que operem no modelo cliente-servidor sobre o protocolo TCP.
O serviço a ser implementado é o de um contador de vogais, consoantes e números seguindo as
especificações abaixo: 

### Servidor:
* O servidor deve começar em modo passivo em uma porta específica para receber solicitações de
um cliente.
* O servidor ao receber uma mensagem que um cliente está ativo deve registrar esse cliente, o
número de solicitações que ele enviará, e também passa a contar com ele como um colaborador.
* Ao receber uma solicitação de um cliente, o servidor seleciona, aleatoriamente, outro cliente
ativo e transmite uma mensagem para que ele realize o processamento da string. O servidor
deve registrar esta solicitação, e voltar a aguardar uma nova mensagem.
* Ao receber a resposta de uma solicitação de processamento de um cliente, o servidor deve
identificar quem a solicitou e encaminhar a resposta ao mesmo.
* Após todas as solicitações aguardadas pelo servidor serem atendidas, o servidor deve enviar uma
mensagem notificando os clientes que eles devem encerrar sua execução, terminando em seguida
a sua própria execução.
### Cliente:
* Um cliente quando iniciado deve enviar uma mensagem ao servidor notificando que ele está ativo
e o número de solicitações que ele enviará ao servidor. Ao receber esta notificação.
* Após notificar o servidor, o cliente envia a primeira string a ser processada, e fica aguardando
uma mensagem do servidor.
* Ao receber a mensagem do servidor para realizar algum processamento de uma string deve-se:

... 1. Verificar se a string não é vazia e se contém caracteres alfa numéricos.

... 2. Se a string estiver no formato correto, o servidor deve retornar como resultado a quantidade
de vogais, consoantes e n´umeros da string enviada. Por exemplo: Pedro5: C=3,V=2,N=5.

... 3. Se a string não possuir caracteres alfa numéricos, o servidor deve indicar ao cliente uma
situação de erro, enviando uma mensagem avisando ao servidor que não é posível processar
a string.

* Nota-se que o cliente pode receber três tipos de mensagens:

... 1. Resposta de uma solicitação enviada ao servidor: neste caso, ele deve imprimir o resultado
na tela e enviar uma nova solicitação ao servidor. O cliente deve receber como entrada
um conjunto de mensagens, a quantidade de mensagens definidas deve estar contida na
primeira mensagem enviada ao servidor.

... 2. Solicitação de processamento de uma string: neste caso, o cliente responde o servidor e
aguarda uma nova mensagem.

... 3. Notificação de encerramento: neste caso, todas as solicitações foram atendidas e o cliente
pode encerrar sua execução.
As informações que serão enviadas pelos clientes quantos as que serão salvas (saída) devem seguir o 
padrão de dois arquivos em anexo. Os arquivos são exemplos que deverão ser rigorosamente seguidos 
para avaliação, uma vez que que os arquivos de outros grupos serão usados para testar a sua implementação.




