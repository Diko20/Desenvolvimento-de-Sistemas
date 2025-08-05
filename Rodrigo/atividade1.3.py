distancia = float(input("Digite a distancia em km: "))
velocidade = float(input("Digite a velocidade média em km/h: "))

tempo = distancia / velocidade

print(f"tempo estimado de viagem: {tempo: .1f} horas")