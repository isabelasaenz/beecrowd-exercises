# nível 1
# não roda em versões anteriores ao python 3.6 por causa do f-string

quantidade = int(input())

dentro = 0
fora = 0

for i in range(quantidade):
    valor = int(input())
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out")
