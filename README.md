# Tp_redes
## Pasta Bat:
      * Contém os scripts .bat para execução dos diferentes cenarios de entrada.
      * Cada arquivo .bat cria uma lista de clientes sendo que um cliente deve passar o nome do arquivo de entrada como parâmetro.
      * Cada client + servidor abrirá sua respectiva janela de terminal.

## Pasta Entradas:
      * Contém todos os arquivos que serão utilizados na execução do trabalho
      * Caso queira alterar um arquivo deve se informar a quantidade de linhas válidas(com pelo menos algum caractere) e adicionar as linhas de caracteres
      
 
## Gerando um novo cenário:
    * Deve se inserir o arquivo de entrada na pasta "Entradas" e alterar ou criar um novo arquivo .bat na pasta "Bat", dentro do arquivo bat deve ser informado o nome do arquivo de entrada no último cliente instanciado.
    * Exemplo:
    
          cd..
          start /min cmd /c cd python Server.py
          start /min cmd /c cd python Client.py
          start /min cmd /c cd python Client.py
          start /min cmd /c cd python Client.py
          start /min cmd /c cd python Client.py
          start /min cmd /c cd python Client.py
          start /min cmd /c cd python Client.py nomeDoArquivo
