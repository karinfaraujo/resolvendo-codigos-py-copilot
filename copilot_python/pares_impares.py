# Como entrada, receber um número inteiro e verificar se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit(1)
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")