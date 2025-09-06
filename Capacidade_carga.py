caminhões = 0
toneladas = 0
quantidade = 0
toneladas = int(input("Digite a quantidade de toneladas: "))
caminhões = toneladas // 10
quantidade = 10-(toneladas % 10)
print(f"Serão necessarios {caminhões} caminhões")
print(f"Sobrarão {quantidade} toneladas")
print(f"Precisamos de {caminhões} caminhões cheios e 1 caminhão com {quantidade} toneladas restante.")