# Entrada de dados
massa = float(input("Digite a massa do material (em kg): "))
volume = float(input("Digite o volume de material: "))

# Processamento
densidade = massa / volume

# Saída
if densidade > 5:
    print("Material muito denso")
elif 2 <= densidade <= 5:
    print("Material com densidade mádia")
else:
    print("Material com pouca densidade")
