"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print("selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    
    if opcao == "i":
        print("i")
        os.system('clear')
        valor = input ("valor: ")
        lista.append(valor)
    elif opcao == 'a' :
        indice_str = input("escolha o indice para apagar:")
        try:
            indice = int (indice_str)
            del lista[indice]
            print("elemento removido com sucesso")
        except:
            print ("nao foi possivel apagar esse indice")
    
    elif opcao == "l" :
        os.system("clear")
        if len (lista) == 0:
           print ("Nada para listar")
        for  i, valor in enumerate(lista)
        print(f'{i}:{valor}')
    else:
        print("por favor, escolha i, a  ou l")    
