Svalor=0
contnegativo=0
for i in range(20):
    valor=int(input("digite o valor: "))
    if valor>=0:
        Svalor+=valor
    else:
        contnegativo+=1
print("A soma dos valores positivos é: ",Svalor)
print(" a quantidade de valores negativos é: ",contnegativo)