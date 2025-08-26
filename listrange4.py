N=int(input("escreva o número de jogadores:"))
soma=0
for i in range(N):
    altura=float(input("escreva a altura do jogador:"))
soma+=altura
print("a altura média dos jogadores é:",soma/N)