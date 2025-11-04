# Testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

try:
    palavra = input("Digite uma palavra: ").strip() 
except Exception as e:
    print("Ocorreu um erro na entrada:", e)
    exit(1)
palavra_invertida = palavra[::-1]
if palavra.lower() == palavra_invertida.lower():
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")    