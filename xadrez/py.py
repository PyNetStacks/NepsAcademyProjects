def xadrez():
    l = int(input())
    c = int(input())
    
    condicoes_brancas= (
        l == c or
        (l % 2 == 0 and c % 2 == 0) or
        (l % 2 != 0 and c % 2 != 0)
    )
    
    if condicoes_brancas:
        print("1")
    else:
        print("0")
        
xadrez()