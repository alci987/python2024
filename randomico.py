"""
importando a biblioteca ramdom
import random - importa a bilioteca toda
from random import choice - importa  apenas a função choice, do pacote random (é mais econômico)
"""
import random

# from random import choice, random

valor_entre_0_e_1 = random.random()  # mostra valore aletórios entre 0 e 1
print("Valores aleatórios entre 0 e 1:", valor_entre_0_e_1)

valor_decimal_entre_10_e_100 = random.uniform(10, 100)  # uniform é para float
print(f"Valor decimal de igual probabilidade entre valores: {valor_decimal_entre_10_e_100: .2f}")

valor_inteiro_entre_100_e_100 = random.randint(10, 100)  # randint é para inteiros
print("Valor inteiro de igual probabilidade entre valores:", valor_inteiro_entre_100_e_100)

print("Sorteado valores predefinidos")
ticket = ['Mateus', 'Marcos', 'João', 'Levi', 'Lucas', 'Kaleb', 'Manoel']
nome_escolhido = random.choice(ticket)
print(nome_escolhido)
