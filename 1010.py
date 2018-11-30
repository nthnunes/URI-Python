info1 = input().split(" ")
info2 = input().split(" ")

P1, Q1, V1 = info1
P2, Q2, V2 = info2

x = (int(Q1) * float(V1)) + (int(Q2) * float(V2))

print("VALOR A PAGAR: R$ %0.2f" %x)
