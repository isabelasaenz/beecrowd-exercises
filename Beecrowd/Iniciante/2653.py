# nível 2

joias = {}
while True:
    try:
        joia = input()
    except EOFError:
        break
    
    if joia not in joias:
        joias[joia] = 1
    else:
        joias[joia] += 1

print(len(joias))
