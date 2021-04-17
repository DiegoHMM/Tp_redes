def contador_de_letras(palavra):
    palavra = str(palavra)
    vogal = ['a','e','i','o','u']
    consoante = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    palavra = palavra.lower()

    cont_vogal = 0
    cont_consoante = 0
    cont_numeros = 0
    tam_palavra = len(palavra)

    #retira o b' enviado com a mensagem 
    if "b'" in palavra: 
        palavra = palavra.replace("b'",'')

    #contador
    for i in palavra:
        if i in vogal:
            cont_vogal = cont_vogal + 1
        elif i in consoante:
            cont_consoante = cont_consoante + 1
        elif i in numeros:
            cont_numeros = cont_numeros + 1
    return palavra, tam_palavra,  cont_vogal, cont_consoante, cont_numeros

