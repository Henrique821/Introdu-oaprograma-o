Svalor=0
contneg=0
some=0
while Svalor+contneg < 20:
  valor=int(input("digite um valor: "))
  if valor>0:
   Svalor+=1
   some+=valor
  elif valor <0:
   contneg += 1
print("a soma dos valores positivos é:",some)
print(" a quantidade de valores negativos é: ",contneg)