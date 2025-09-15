numero_um = float(input("Digite o primeiro numero: "))
numero_dois = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao matematica: ")

if operacao == "soma" or operacao == "edicao":
    print(numero_um + numero_dois)
elif operacao == "multiplicacao" or operacao == "multiplicacao":
    print(numero_um * numero_dois)
elif operacao == "dividir" or operacao == "divisao":
    print(numero_um / numero_dois)
elif operacao == "diminuir" or operacao == "subtracao":
    print(numero_um - numero_dois)

print("Fim da calculadora")