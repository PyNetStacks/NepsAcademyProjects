def quadrado_magico():
    n = int(input())
    
    matriz = []
    for _ in range(n):
        num = list(map(int, input().split()))
        matriz.append(num)
    
    num_desejado = sum(matriz[0])
    
    for i in range(n):
        if sum(matriz[i]) != num_desejado:
            print("-1")
            return

    for j in range(n):
        soma_coluna = sum(matriz[i][j] for i in range(n))
        if soma_coluna != num_desejado:
            print("-1")
            return

    soma_diagonal_principal = sum(matriz[i][i] for i in range(n))
    if soma_diagonal_principal != num_desejado:
        print("-1")
        return

    soma_diagonal_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
    if soma_diagonal_secundaria != num_desejado:
        print("-1")
        return

    print(num_desejado)

quadrado_magico()
