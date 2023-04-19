# nível 3

while True:
    try:
        # lê o número de lesmas e suas velocidades
        L = int(input())
        vels = list(map(int, input().split()))

        # encontra a lesma mais veloz
        max_vel = max(vels)

        # verifica em qual nível de velocidade ela se encaixa
        if max_vel < 10:
            print(1)
        elif max_vel < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break
