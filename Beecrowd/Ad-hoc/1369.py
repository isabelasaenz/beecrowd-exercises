#nível 10 - runtime error


while True:
    n = int(input())
    if n == 0:
        break
    
# recebe o tamanho do disco em unidades e sua unidade de medida (Mb ou Gb) e converte para bytes
d, unit = input().split()
d = int(d)
if unit == 'Mb':
    d *= 1024
elif unit == 'Gb':
    d *= 1024 * 1024

# inicializa o disco como uma lista de -1's, representando que todos os blocos estão livres
# o primeiro item da lista é o tamanho do disco em blocos
disk = [-1] * (d // 8)
disk[0] = d // 8

# loop pelas operações a serem realizadas no disco
for i in range(n):
    # recebe a operação a ser realizada e divide em suas partes (insere, remove, otimiza)
    op = input().split()
    
    # inserção de arquivos no disco
    if op[0] == 'insere':
        name = op[1]  # nome do arquivo a ser inserido
        size = int(op[2][: -2])  # tamanho do arquivo em unidades
        if op[2].endswith('Mb'):
            size *= 1024
        elif op[2].endswith('Gb'):
            size *= 1024 * 1024
        
        free = -1  # índice do primeiro bloco livre encontrado
        # loop pelos blocos do disco para encontrar espaço suficiente para o arquivo
        for j in range(len(disk)):
            if disk[j] == -1:
                if free == -1:
                    free = j
                elif j - free + 1 >= size // 8:
                    break
        else:
            # caso não seja encontrado espaço suficiente, imprime mensagem de erro e passa para a próxima operação
            print('ERRO: disco cheio')
            continue
        
        # preenche os blocos com o nome do arquivo
        for j in range(free, free + size // 8):
            disk[j] = name
        
        # define os blocos restantes como livres
        disk[j + 1: ] = [-1] * (len(disk) - j - 1)
        
    # remoção de arquivos do disco
    elif op[0] == 'remove':
        name = op[1]  # nome do arquivo a ser removido
        # loop pelos blocos do disco para encontrar o arquivo e removê-lo
        for j in range(len(disk)):
            if disk[j] == name:
                disk[j] = -1
                
    # otimização do disco
    elif op[0] == 'otimiza':
        last = -1  # último bloco ocupado encontrado
        # loop pelos blocos do disco para encontrar blocos vazios e preencher com arquivos que estão divididos em mais de um bloco
        for j in range(len(disk)):
            if disk[j] != -1:
                if last != -1 and j - last > 1:
                    # move o arquivo para o início do espaço livre encontrado
                    for k in range(j - last):
                        disk[last + k] = disk[j - (j - last) + k

                        disk[last + k] = disk[j - (j - last) + k + 1]
                        disk[j - (j - last) + k + 1] = -1
                last = j

        # marca o restante dos blocos como vazios
        disk[last + 1: ] = [-1] * (len(disk) - last - 1)
        
    # verifica o espaço livre no disco e imprime a representação gráfica
    blocks = [0] * 8
    for i in range(len(disk)):
        if disk[i] == -1:
            blocks[i % 8] += 1
    for i in range(8):
        free = blocks[i] / (d // 8 / 100)
        if free > 75:
            print




