def busca():
    lista = list(map(int, input().split()))
    x = int(input())

    if x in lista:
        quantidade = lista.count(x)
        indices = [i for i, num in enumerate(lista) if num == x]
        print(quantidade)
        print(*indices)
    else:
        print("Mia x")

busca()