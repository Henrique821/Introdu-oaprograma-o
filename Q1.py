numero=int(input("Digite um número: "))
resto=0
resultado=0
contador=0
while(numero%10!=0):
    resto=numero%10
    numero=numero//10
    for i in range(1, resto+1):
        if resto%i==0:
            contador+=1
    if contador==2:
        resultado+=resto
    contador=0
print(resultado)