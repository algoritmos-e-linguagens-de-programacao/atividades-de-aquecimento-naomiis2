from calendar import c


l = input().split()
c1 = int(l[0])
n1 = int(l[1])
v1 = float(l[2])

l2 = input().split()
c2 = int(l[0])
n2 = int(l[1])
v2 = int(l[2])

vt = n1 * v1 + n2 * v2
print("Valor a pagar = R$ %.2f"%vt)