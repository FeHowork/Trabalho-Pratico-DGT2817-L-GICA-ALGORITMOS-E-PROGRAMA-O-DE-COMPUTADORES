saida = ""
def soma(a, b):
    resultado = a + b
    print(f"O resultado da soma é: {resultado}")

def subtracao(a, b):
    resultado = a - b
    print(f"O resultado da subtração é: {resultado}")

def multiplicacao(a, b):
    resultado = a * b
    print(f"O resultado da multiplicação é: {resultado}")

def divisao(a, b):
    if b == 0:
        print("Não foi possível realizar a divisão por 0")
    else:
        resultado = a / b
        print(f"O resultado da divisão é: {resultado}")

def calculadora(a, b, operacao):
    if operacao == "+" or operacao == "soma":
        soma(a, b)
    elif operacao == "-" or operacao == "subtracao":
        subtracao(a, b)
    elif operacao == "*" or operacao == "multiplicacao":
        multiplicacao(a, b)
    elif operacao == "/" or operacao == "divisao":
        divisao(a, b)
    else:
        print("Operação inválida")

while saida.lower() != "n":  # O loop continua enquanto a resposta não for 'n'
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(num1, num2, operacao)
  
    saida = input("Deseja continuar? (S/N): ")  # Pergunta ao usuário se deseja continuar

print("Programa encerrado.")

