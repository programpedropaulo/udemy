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
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11: 
        return None
        
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Formata o CPF com pontos e traços 
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        
    return cpf_formatado

def valida_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos após remover caracteres não numéricos
    if len(cpf) != 11:
        return False

    # Calcula os dígitos verificadores
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    # Verifica se os dígitos verificadores são iguais aos dígitos do CPF
    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        return True
    else:
        return False

while True:
    cpf = input("Qual é o seu CPF? ")
    cpf_formatado = formata_cpf(cpf)  

    if cpf_formatado:
        print(f"Seu CPF é {cpf_formatado} correto?")

        resposta_do_cpf = input("(Sim/Não): ").lower()  # Corrigido para input() ao invés de uma string fixa

        if resposta_do_cpf == "sim":
            if valida_cpf(cpf):  # Chama a função para validar o CPF
                print("CPF válido")
            else:
                print("CPF inválido")
        elif resposta_do_cpf == "nao" or resposta_do_cpf == "não":  
            print("CPF inválido")
        else:
            print("Resposta inválida")




        

    