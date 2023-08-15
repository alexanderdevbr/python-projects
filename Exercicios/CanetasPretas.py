# Analise o codigo abaixo
L=[3,5,1,7]
while len(L) < 8:
    L.append(L[-2] - L[-1])
print(L)

# O valor do último número exibido no print será
# A) -51
# B) -6
# C) 7
# D) 19
# E) 32

'''
1) 1-7 > [3,5,1,7,-6]
2) 7+6 > [3,5,1,7,-6,13]
3) -6-13 > [3,5,1,7,-6,13,-19]
4) 13+19 > [3,5,1,7,-6,13,-19,32]
'''