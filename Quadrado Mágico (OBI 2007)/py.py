def quadrado_magico():
    n = int(input()) 
    
    matriz = []

    for _ in range(n):
        num = list(map(int, input().split()))
        matriz.append(num)

    linha0 = matriz[0]
    linha1 = matriz[1]
    linha2 = matriz[2]
    num_desejado= sum(linha0)

    condicoes = (
    sum(linha0) == num_desejado and
    sum(linha1) == num_desejado and
    sum(linha2) == num_desejado and
    (linha0[0] + linha1[0] + linha2[0]) == num_desejado and
    (linha0[1] + linha1[1] + linha2[1]) == num_desejado and
    (linha0[2] + linha1[2] + linha2[2]) == num_desejado and
    (linha0[0] + linha1[1] + linha2[2]) == num_desejado and
    (linha0[2] + linha1[1] + linha2[0]) == num_desejado
    )

    if condicoes:
        print(num_desejado)
    else: 
        print("-1")

quadrado_magico()
