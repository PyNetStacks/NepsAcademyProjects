inteiros = []
y = list(map(int, input().split()))
inteiros.extend(y)    

def busca_simples():
    x = int(input())
    if x in inteiros:
        return "SIM"
    else:
        return "NAO"

print(busca_simples())