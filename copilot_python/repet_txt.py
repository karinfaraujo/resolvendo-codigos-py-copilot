#  Solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

def repetir_string(s: str, n: int) -> str:
    if n <= 0:
        return ""
    return " ".join([s] * n)

if __name__ == "__main__":
    s = input("Digite uma string: ")
    try:
        n = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida: o número deve ser um inteiro.")
    else:
        print(repetir_string(s, n))        