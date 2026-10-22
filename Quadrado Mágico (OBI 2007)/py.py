def quadrado_magico():
    n = int(input())

    matriz = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(*linha)
    print(*matriz)

quadrado_magico()