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
        print("Verifique o número de caracteres")
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
        print("Verifique o número de caracteres")
        return False

    # Calcula os dígitos verificadores
    nove_digitos = cpf[:9]
    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf == cpf_gerado_pelo_calculo:
        return True
    else:
        return False

while True:
    cpf = input("Qual é o seu CPF? ")
    cpf_formatado = formata_cpf(cpf)  

    if cpf_formatado:
        print(f"Seu CPF é {cpf_formatado} correto?")

        resposta_do_cpf = input("(Sim/Não): ").lower()

        if resposta_do_cpf == "sim":
            if valida_cpf(cpf):  # Chama a função para validar o CPF
                print("CPF válido")
            else:
                print("CPF inválido")
        elif resposta_do_cpf == "nao" or resposta_do_cpf == "não":  
            print("CPF inválido")
        else:
            print("Resposta inválida")
