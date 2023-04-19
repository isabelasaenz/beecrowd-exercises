while True:
    try:
        a, b = map(int, input().split())

        # o operador % calcula o módulo da soma com 2^32, 
        # o que equivale a descartar quaisquer bits de overflow e retornar a zero, se necessário.
        
        result = (a ^ b) % (1 << 32)

        print(result)

    except EOFError:
        break
