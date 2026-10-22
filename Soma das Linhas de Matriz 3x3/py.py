#    -  -  -
#    -  -  -
#    -  -  -

def matriz3x3():
    linha0 = 0
    linha1 = 0
    linha2 = 0

    for i in range(1,4,1):
        num = int(input())
        linha0 += num
    for i in range(1,4,1):
        num = int(input())
        linha1 += num
    for i in range(1,4,1):
        num = int(input())
        
        linha2 += num
    
    print(f"Linha 0: {linha0}")
    print(f"Linha 1: {linha1}")
    print(f"Linha 2: {linha2}")

matriz3x3()
    
