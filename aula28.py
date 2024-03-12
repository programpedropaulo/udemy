nome =  input("Qual e o seu nome? ")

if nome == "": 
    print("Desculpe voce deixou os campos vazios")
else:
    print(f"Seu nome é {nome}")
    print(f"seu nome invertido é {nome[-1::-1]}")
    if " " in nome:
        print ("seu nome tem espaços")
    else:
        print("nao contem espaços") 
    print(f"seu nome tem {nome.__len__():} numeros")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print (f"a ultima letra do seu nome é {nome[-1]}")   

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""