# Solicitar como entrada dois números e depois realizar uma operação simples entre eles.

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
except ValueError:
    print("Entrada inválida. Use números.")
    exit(1)

op = input("Escolha a operação (+, -, *, /): ").strip()

if op == "+":
    resultado = a + b
elif op == "-":
    resultado = abs(a - b)
elif op == "*":
    resultado = a * b
elif op == "/":
    if b == 0:
        print("Erro: divisão por zero.")
        exit(1)
    resultado = a / b
else:
    print("Operação inválida.")
    exit(1)

print(f"Resultado: {a} {op} {b} = {resultado}")