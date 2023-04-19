# nível 9 - runtime error na plataforma

def calcula_frequencia(nota):
    # cria um dicionário com as frequências das notas básicas
    frequencias = {'A': 440, 'B': 494, 'C': 523, 'D': 587, 'E': 659, 'F': 698, 'G': 784}

    # verifica se a nota possui sustenido ou bemol e calcula a frequência correspondente
    if '#' in nota:
        return frequencias[nota[0]] * 2 ** (1/12)
    elif 'b' in nota:
        return frequencias[nota[0]] / 2 ** (1/12)
    else:
        return frequencias[nota]
        
def verifica_plagio(musica, trecho):
    # converte as notas da música e do trecho em frequências
    frequencias_musica = [calcula_frequencia(nota) for nota in musica]
    frequencias_trecho = [calcula_frequencia(nota) for nota in trecho]

    # verifica se o trecho ocorre em algum tom da música
    for i in range(len(frequencias_musica) - len(frequencias_trecho) + 1):
        if all(abs(frequencias_musica[i+j] - frequencias_trecho[j]) <= 0.5 for j in range(len(frequencias_trecho))):
            return 'S'
    return 'N'

while True:
    # lê os valores de M e T
    M, T = map(int, input().split())
    if M == 0 and T == 0:
        break

    # lê as notas da música e do trecho
    musica = input().split()
    trecho = input().split()

    # verifica se o trecho ocorre em algum tom da música e imprime o resultado
    print(verifica_plagio(musica, trecho))
