def resolver_fita_colorida():
    n = int(input())
    fita = list(map(int, input().split()))
    
    distancias = [float('inf')] * n
    
    distancia_atual = float('inf')
    for i in range(n):
        if fita[i] == 0:
            distancia_atual = 0  
        else:
            distancia_atual += 1
        
        distancias[i] = distancia_atual

    distancia_atual = float('inf')
    for i in range(n - 1, -1, -1):
        if fita[i] == 0:
            distancia_atual = 0
        else:
            distancia_atual += 1
        
        distancias[i] = min(distancias[i], distancia_atual)
        

        if distancias[i] >= 9:
            distancias[i] = 9

    print(*(distancias))

if __name__ == "__main__":
    resolver_fita_colorida()
