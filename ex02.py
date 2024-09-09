#2 Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contar_a(string):
    return string.lower().count('a')

# Entrada de uma string
texto = input("Informe uma string: ")

# Contar a quantidade de 'a' na string
quantidade = contar_a(texto)

# Informar o resultado
print(f"A letra 'a' aparece {quantidade} vez(es) na string.")