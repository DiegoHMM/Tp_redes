import re

def contador_de_letras(palavra):
    vogal = ['a','e','i','o','u']
    consoante = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    palavra = palavra.lower()

    cont_vogal = 0
    cont_consoante = 0
    cont_numeros = 0
    tam_palavra = len(palavra)
    for i in palavra:
        if i in vogal:
            cont_vogal = cont_vogal + 1
        elif i in consoante:
            cont_consoante = cont_consoante + 1
        elif i in numeros:
            cont_numeros = cont_numeros + 1
    return  palavra, cont_consoante, cont_vogal, cont_numeros


def le_arquivo(nome_arquivo):
    f = open('Entradas/'+nome_arquivo+'.txt', "r")
    l = []
    for line in f:
        
        if(len(line) >= 2):
            if line[0]+line[1] == '//':
                print(" ")
            elif line != '\n':
                line = line.replace('\n','')
                line = re.sub('[^a-zA-Z0-9\n\.]', ' ', line)
                l.append(line)
        elif line != '\n':
            line = re.sub('[^a-zA-Z0-9\n\.]', ' ', line)
            l.append(line)
    return l