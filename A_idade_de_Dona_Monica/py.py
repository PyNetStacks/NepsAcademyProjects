m = int(input())
a = int(input())
b = int(input())
c = m - (a+b)

if 40 <= m <= 110 and 1 <= a < m and 1 <= b < m and a != b:
    print(c)