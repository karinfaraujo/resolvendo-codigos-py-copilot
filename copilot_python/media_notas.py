# Calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
except ValueError:
    print("Entrada inválida. Use números para as notas.")
    exit(1)
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")