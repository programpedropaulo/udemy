"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

enquanto contador <= 100:
    contador += 1

    se contador == 6:
        print('Não vou mostrar o 6'.)
        continuar

    se contador >= 10 e contador <= 27:
        print('Não vou mostrar o', contador)
        continuar

    impressão(contador)

    se contador == 40:
        quebrar


print('Acabou')