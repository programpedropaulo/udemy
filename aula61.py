"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


def formata_cpf(cpf):
    # verifica se o cpf possui 11 digitos
    if  len(cpf) != 11: 

        return None
    
    #formata o CPF com pontos e traços 
    cpf_formatado =  f" {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    return cpf_formatado
 
cpf = input("Qual e o seu CPF?")
cpf_formatado = formata_cpf(cpf)   

print(f"Seu CPF é {cpf_formatado} correto?")
resposta_do_cpf = ("(Sim/Não): ").lower()

if resposta_do_cpf == "sim":
   #verificaçao se o numero do cpf e valido
    pass
elif resposta_do_cpf == "nao" or resposta_do_cpf =="não":
    print ("CPF inválido")
    #retorna ao inicio do codigo
else:
    print("Resposta inválida")
