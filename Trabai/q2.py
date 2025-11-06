#Murilo,Henrique,Gabriel Inácio Pereira Monteiro.
num= int(input("digite um numero decimal:"))
binario=0
base=1
while num > 0:
    resto=num%2
    binario=binario+resto*base
    num=num//2
    base=base*10
print("binario", binario)