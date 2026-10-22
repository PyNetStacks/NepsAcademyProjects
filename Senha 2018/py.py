def senha():
    senha = 2018
    tentativas = 0 

    while True:
        chute = int(input())
        if chute == senha:
            print(tentativas)
            break
        else:
            tentativas += 1

senha()    