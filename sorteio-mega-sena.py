import random

numero_aleatorio = []

for n in range(1, 60 + 1):
    numero_aleatorio.append(n)

    if len(numero_aleatorio) > 60:
        break

contador = 1
numero_sorteado = []
while contador <= 7:
    sorteio = random.choice(numero_aleatorio)
    
    if sorteio in numero_sorteado:
        sorteio = random.choice(numero_aleatorio)
    else:
        numero_sorteado.append(sorteio) 
    contador +=1

print(sorted(numero_sorteado))