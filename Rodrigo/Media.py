
nota1 = float(input("Digite a primeiro nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

média = (nota1 + nota2 + nota3 + nota4) / 4
print("sua média é", média)

if média >= 5:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")
