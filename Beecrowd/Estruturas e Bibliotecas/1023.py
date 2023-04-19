# nível 10
# otimizado devido ao limite de tempo da plataforma

cidade = 0

while True:
    n = int(input())
    if n == 0:
        break
    
    print(f"Cidade# {cidade}:")
    cidade += 1
    
    consumo_total = 0
    pessoas = []
    
    for i in range(n):
        x, y = map(int, input().split())
        consumo_total += y
        pessoas.append({'quantidade': x, 'consumo': y})
    
    pessoas = sorted(pessoas, key=lambda p: p['consumo'])
    
    for p in pessoas:
        print(f"{p['quantidade']}-{p['consumo']}", end=' ')
    
    consumo_medio = consumo_total / sum(p['quantidade'] for p in pessoas)
    print(f"\nConsumo medio: {consumo_medio:.2f} m3.\n")
