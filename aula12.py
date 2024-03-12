nome = input("Qual é o seu nome? ")
altura_cm = float(input("Qual é a sua altura (em centímetros)? "))
peso = float(input("Qual é o seu peso (em kg)? "))

# Convertendo altura para metros (1 metro = 100 centímetros)
altura_metros = altura_cm / 100

imc = peso / (altura_metros ** 2)

print(f"Nome: {nome}")
print(f"Altura: {altura_metros:.2f} metros")
print(f"Peso: {peso} kg")
print(f"IMC: {imc:.2f}")
