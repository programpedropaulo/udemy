"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("digite um número: ")


try:
    conta = int(numero) % 2 == 0
    if conta is True:
        print("Esse número e par")
    else :
        print("Esse número e impar")
except ValueError :
    print("Esse nao e um numero inteiro,")

print(" ")
print(" ")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = float (input ("Por favor me informe as horas. "))
if  0<= horas  < 12 :
    print("estamos no periodo da manhã , bom dia!!")
elif  12 <= horas < 18 :
    print("estamos no periodo da tarde , boa tarde!")
else:
    print("estamos no periodo da noite , boa noite")

print(" ")
print(" ")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("digite seu nome por favor, ")
nome01 = len(nome)

if nome01 <= 4:
    print("seu nome e curto")
elif  5<= nome01 <= 6:
    print("seu nome e normal")
else:
    print ("seu nome e muito grande!")